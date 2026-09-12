"""Game-plan content validation and revision archives, independent of the HTML renderer."""
from datetime import date
import hashlib
import json
import os
from urllib.parse import urlsplit


def require(condition, message):
    if not condition:
        raise ValueError(message)


def fields(value, expected, label):
    require(isinstance(value, dict) and set(value) == set(expected.split()), f'Invalid {label} fields')


def text(value, label):
    require(isinstance(value, str) and bool(value.strip()) and len(value) <= 2000, f'Invalid {label}')


def dated(value):
    require(isinstance(value, str) and len(value) == 10, 'Expected date YYYY-MM-DD')
    date.fromisoformat(value)


def items(value, label, maximum=24, minimum=0):
    require(isinstance(value, list) and minimum <= len(value) <= maximum, f'Invalid {label}')
    return value


def content_hash(data):
    canonical = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()


def validate_context(data):
    game = data.get('game')
    if data['schema_version'] == 3:
        fields(game, 'description recorded_from', 'user-written game description')
        require(isinstance(game['description'], str) and len(game['description']) <= 12000, 'Invalid user game description')
        if game['description'].strip():
            text(game['recorded_from'], 'source of the user-written description')
        else:
            require(game['recorded_from'] is None, 'An absent description cannot claim a user source')
    else:
        fields(game, 'premise role goal session arc style', 'legacy game description')
        for key in ('premise', 'role', 'goal', 'arc', 'style'):
            text(game[key], key)
        for beat in items(game['session'], 'example play', 6, 1):
            fields(beat, 'title detail', 'play moment')
            text(beat['title'], 'play moment title')
            text(beat['detail'], 'play moment description')
    for source in items(data.get('inspirations'), 'research examples', 6):
        fields(source, 'title url checked observation lesson difference', 'research example')
        for key in ('title', 'url', 'observation', 'lesson', 'difference'):
            text(source[key], key)
        url = urlsplit(source['url'])
        require(url.scheme == 'https' and url.hostname and not url.username and not url.password
                and not any(char.isspace() or ord(char) < 32 for char in source['url']), 'Research links must be plain HTTPS URLs')
        dated(source['checked'])
    dev = data.get('development')
    fields(dev, 'purpose stage updated summary next approved_plan milestones change_note', 'development record')
    require(dev['purpose'] in ('proposal', 'update'), 'Invalid review purpose')
    require(dev['stage'] in ('idea', 'building', 'testing', 'released'), 'Invalid development stage')
    dated(dev['updated'])
    text(dev['summary'], 'progress summary')
    text(dev['next'], 'next action')
    text(dev['change_note'], 'what changed in this version')
    approved = dev['approved_plan']
    if approved is not None:
        fields(approved, 'revision fingerprint recorded_from', 'previous approval')
        require(type(approved['revision']) is int and 0 < approved['revision'] < data['revision'], 'Approval must refer to an earlier version')
        require(isinstance(approved['fingerprint'], str) and len(approved['fingerprint']) == 64
                and all(char in '0123456789abcdef' for char in approved['fingerprint']), 'Invalid approved fingerprint')
        text(approved['recorded_from'], 'approval source')
    require(dev['purpose'] != 'update' or approved is not None, 'A progress update must identify its previously approved plan')
    for milestone in items(dev['milestones'], 'progress entries'):
        fields(milestone, 'title status detail evidence', 'progress entry')
        for key in ('title', 'detail'):
            text(milestone[key], key)
        require(milestone['status'] in ('planned', 'in_progress', 'done', 'revisit'), 'Invalid progress status')
        if milestone['evidence'] is not None:
            text(milestone['evidence'], 'progress evidence')
        require(milestone['status'] != 'done' or milestone['evidence'] is not None, 'Finished work needs supporting evidence')


def archive_paths(review, output):
    folder = output.parent / 'history'
    stem = f"{review['review_id']}-r{review['revision']}"
    return folder / f'{stem}.json', folder / f'{stem}.html'


def check_archive(review, output):
    source, html = archive_paths(review, output)
    require(output.resolve() not in (source.resolve(), html.resolve()), 'Current output must be separate from its history')
    require(source.exists() or not (html.exists() or source.with_suffix('.sha256').exists()),
            'Incomplete history snapshot exists; inspect it before rebuilding this version')
    if source.exists():
        previous = json.loads(source.read_text(encoding='utf-8-sig'))
        require(previous == review, 'This version already exists with different content; increase revision')
    # Prevent an old version from replacing the current plan after newer work.
    for path in source.parent.glob(f"{review['review_id']}-r*.json"):
        old = verify_snapshot(path)
        require(old['revision'] <= review['revision'], 'A newer archived version exists; increase revision')
    approved = review.get('development', {}).get('approved_plan')
    if approved:
        prior = source.parent / f"{review['review_id']}-r{approved['revision']}.json"
        require(prior.is_file(), 'The approved source version is missing from history')
        previous = json.loads(prior.read_text(encoding='utf-8-sig'))
        require(content_hash(previous) == approved['fingerprint'], 'Approved content does not match the archived plan')
        require(not previous.get('example', False) or review.get('example', False), 'A sample plan cannot authorize real progress')
        require(previous.get('development', {}).get('purpose') != 'update', 'A progress report cannot be the approved design')
        if review['development']['purpose'] == 'update':
            for key in ('title', 'summary', 'scope', 'decisions', 'next_steps', 'acceptance', 'boundaries', 'game'):
                require(previous.get(key) == review.get(key), f'Progress updates cannot change {key}; create a new proposal')
            dev = review['development']
            require(not review['open_questions'], 'Unsettled design questions require a proposal, not a progress update')
            allowed_next = {'none'} | {f'step:{i + 1}' for i in range(len(previous['next_steps']))}
            require(dev['next'] in allowed_next, 'Progress next must point to an approved step or none')
            work = {(step['title'], step['detail']) for step in previous['next_steps']}
            work |= {(entry['title'], entry['detail']) for entry in previous.get('development', {}).get('milestones', [])}
            require(all((entry['title'], entry['detail']) in work for entry in dev['milestones']),
                    'Progress work must match an approved step or milestone; report new findings in evidence')
    return source, html


def record_snapshot(source, html):
    record = {'source_hash': hashlib.sha256(source.read_bytes()).hexdigest(),
              'html_hash': hashlib.sha256(html.read_bytes()).hexdigest()}
    source.with_suffix('.sha256').write_text(json.dumps(record), encoding='utf-8')


def verify_snapshot(source):
    html, receipt = source.with_suffix('.html'), source.with_suffix('.sha256')
    require(html.is_file() and receipt.is_file(), f'History copy or integrity record is missing: {source}')
    recorded = json.loads(receipt.read_text(encoding='utf-8'))
    require(recorded == {'source_hash': hashlib.sha256(source.read_bytes()).hexdigest(),
                         'html_hash': hashlib.sha256(html.read_bytes()).hexdigest()}, f'History content changed: {source}')
    return json.loads(source.read_text(encoding='utf-8-sig'))


def history_links(review, output, archive_folder):
    links = []
    for source in archive_folder.glob(f"{review['review_id']}-r*.json"):
        entry = json.loads(source.read_text(encoding='utf-8-sig'))
        if entry['revision'] >= review['revision']:
            continue
        verify_snapshot(source)
        dev = entry.get('development', {})
        links.append({'revision': entry['revision'], 'date': dev.get('updated'),
                      'summary': dev.get('change_note', entry['summary']),
                      'url': os.path.relpath(source.with_suffix('.html'), output.parent).replace(os.sep, '/')})
    return sorted(links, key=lambda entry: entry['revision'], reverse=True)
