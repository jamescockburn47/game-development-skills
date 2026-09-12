"""Build an offline HTML decision review, or check a returned review response."""
import argparse
import json
import os
from pathlib import Path
import re
from review_document import validate_context, content_hash, check_archive, history_links, record_snapshot

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def string(value, name, limit=2000, empty=False):
    require(isinstance(value, str) and len(value) <= limit, f'Invalid {name}')
    require(empty or bool(value.strip()), f'Empty {name}')
    return value


def strings(value, name, limit=24):
    require(isinstance(value, list) and len(value) <= limit, f'Invalid {name}')
    return [string(item, name) for item in value]


def identifier(value, name):
    string(value, name, 100)
    require(bool(re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]*', value)), f'Invalid {name}')
    return value


def validate_review(data):
    require(isinstance(data, dict) and type(data.get('schema_version')) is int and data['schema_version'] in (1, 2, 3), 'Expected review schema 1, 2 or 3')
    fields = {'schema_version', 'review_id', 'revision', 'title', 'summary', 'scope', 'example',
              'decisions', 'next_steps', 'acceptance', 'boundaries', 'risks', 'open_questions'}
    if data['schema_version'] >= 2:
        fields |= {'game', 'inspirations', 'development'}
    require(not set(data) - fields, 'Unknown review fields')
    identifier(data.get('review_id'), 'review_id')
    require(type(data.get('revision')) is int and data['revision'] > 0, 'Invalid revision')
    for key in ('title', 'summary', 'scope'):
        string(data.get(key), key)
    require(type(data.get('example', False)) is bool, 'Invalid example flag')
    for key in ('acceptance', 'boundaries', 'risks', 'open_questions'):
        strings(data.get(key), key)
    require(bool(data['acceptance']) and bool(data['boundaries']), 'Include acceptance and scope boundaries')
    steps = data.get('next_steps')
    require(isinstance(steps, list) and 1 <= len(steps) <= 16, 'Expected next build steps')
    for step in steps:
        require(isinstance(step, dict) and set(step) == {'title', 'detail'}, 'Invalid step fields')
        string(step.get('title'), 'step title')
        string(step.get('detail'), 'step detail')
    references = {f'step:{i + 1}' for i in range(len(steps))} | {
        f'check:{i + 1}' for i in range(len(data['acceptance']))}
    decisions = data.get('decisions')
    require(isinstance(decisions, list) and 1 <= len(decisions) <= 32, 'Expected 1–32 decisions')
    ids = set()
    for decision in decisions:
        require(isinstance(decision, dict), 'Invalid decision')
        require(not set(decision) - {'id', 'label', 'value', 'rationale', 'source', 'editable', 'affects', 'options'}, 'Unknown decision fields')
        key = identifier(decision.get('id'), 'decision id')
        require(key not in ids, f'Duplicate decision: {key}')
        ids.add(key)
        for field in ('label', 'value', 'rationale'):
            string(decision.get(field), field)
        require(decision.get('source') in ('user', 'agent', 'assumption'), 'Invalid decision source')
        require(type(decision.get('editable', True)) is bool, 'Invalid editable flag')
        affects = strings(decision.get('affects'), 'affected step/check references', 12)
        require(set(affects) <= references and len(affects) == len(set(affects)), 'Unknown or duplicate affected reference')
        require(any(ref.startswith('step:') for ref in affects) and any(ref.startswith('check:') for ref in affects),
                'Each material decision must identify an affected build step and acceptance check')
        options = decision.get('options', [])
        require(isinstance(options, list) and len(options) <= 16, 'Invalid options')
        values = set()
        for option in options:
            require(isinstance(option, dict) and set(option) == {'value', 'label', 'impact'}, 'Invalid option fields')
            for field in ('value', 'label', 'impact'):
                string(option.get(field), field)
            require(option['value'] not in values, 'Duplicate option')
            values.add(option['value'])
        require(not options or decision['value'] in values, f'Unknown selected option: {key}')
    require('fingerprint' not in data, 'Fingerprint is generated, not an input field')
    if data['schema_version'] >= 2:
        validate_context(data)
    return data


def fingerprint(data):
    return content_hash(data)


def read_json(path):
    require(path.stat().st_size <= 200_000, 'Review/response file exceeds 200 KB')
    return json.loads(path.read_text(encoding='utf-8-sig'))


def check_response(review, response):
    validate_review(review)
    expected = {'schema_version', 'review_id', 'revision', 'fingerprint', 'decision', 'values', 'notes', 'example'}
    user_description = review['schema_version'] == 3
    if user_description:
        expected.add('game_description')
    require(isinstance(response, dict) and set(response) == expected, 'Unexpected response fields')
    require(type(response['schema_version']) is int and response['schema_version'] == (2 if user_description else 1), 'Unknown response schema')
    for key in ('review_id', 'revision'):
        require(type(response[key]) is type(review[key]) and response[key] == review[key], f'Stale/wrong {key}')
    require(response['fingerprint'] == fingerprint(review), 'Response belongs to different review content')
    require(type(response['example']) is bool and response['example'] == review.get('example', False), 'Wrong example flag')
    require(response['decision'] in ('approve', 'request_changes'), 'Unknown review decision')
    string(response['notes'], 'notes', 3000, empty=True)
    values = response['values']
    require(isinstance(values, dict) and set(values) == {d['id'] for d in review['decisions']}, 'Missing/unknown decision values')
    changed = []
    if user_description:
        description = string(response['game_description'], 'user game description', 12000, empty=True)
        if description != review['game']['description']:
            changed.append('game_description')
    for decision in review['decisions']:
        value = string(values[decision['id']], 'decision value')
        options = decision.get('options', [])
        require(not options or value in {o['value'] for o in options}, 'Unknown choice')
        if value != decision['value']:
            require(decision.get('editable', True), 'A locked constraint was changed')
            changed.append(decision['id'])
    if response['decision'] == 'approve':
        require(user_description, 'Legacy plans need the actual user-written description before a new build approval')
        require(bool(review['game']['description'].strip()) and review['game']['recorded_from'] is not None,
                'The user must supply the game description before approval')
        require(review.get('development', {}).get('purpose') != 'update', 'A progress update is for feedback, not a new build approval')
        require(not changed and not response['notes'].strip(), 'Changes require a revised review before approval')
        require(not review['open_questions'], 'Blocking questions remain')
        require(not review.get('example', False), 'Example reviews cannot authorize a game build')
    return {'valid': True, 'decision': response['decision'], 'changed_decisions': changed,
            'user_authorization_verified': False,
            'next': 'Confirm this response came from the user through the task or a verified host interaction. '
                    'This structural check alone does not authorize building.'}


def render_html(review, output, archive_folder, current_output):
    assets = ROOT / 'assets'
    html = (assets / 'design-review.html').read_text(encoding='utf-8')
    content = dict(review, fingerprint=fingerprint(review), history_links=history_links(review, output, archive_folder),
                   archived_view=output != current_output,
                   current_url=os.path.relpath(current_output, output.parent).replace(os.sep, '/'))
    data = json.dumps(content, ensure_ascii=True).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    replacements = {'__REVIEW_CSS__': (assets / 'design-review.css').read_text(encoding='utf-8'),
                    '__REVIEW_SECTIONS_CSS__': (assets / 'design-review-sections.css').read_text(encoding='utf-8'),
                    '__REVIEW_DATA__': data,
                    '__REVIEW_JS__': (assets / 'design-review-content.js').read_text(encoding='utf-8') + '\n' +
                    (assets / 'design-review.js').read_text(encoding='utf-8')}
    for marker in replacements:
        require(html.count(marker) == 1, f'Expected one template marker: {marker}')
    return re.sub(r'__REVIEW_(?:CSS|SECTIONS_CSS|DATA|JS)__', lambda match: replacements[match.group()], html)


def build(review, output):
    validate_review(review)
    archived_source, archived_html = check_archive(review, output)
    html = render_html(review, output, archived_source.parent, output)
    archived_source.parent.mkdir(parents=True, exist_ok=True)
    if not archived_source.exists():
        archived_source.write_text(json.dumps(review, ensure_ascii=False, indent=2), encoding='utf-8', newline='\n')
    if not archived_html.exists():
        archived_html.write_text(render_html(review, archived_html, archived_source.parent, output), encoding='utf-8', newline='\n')
        record_snapshot(archived_source, archived_html)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding='utf-8', newline='\n')
    return {'output': str(output.resolve()), 'review_id': review['review_id'],
            'revision': review['revision'], 'fingerprint': fingerprint(review), 'archived': str(archived_html.resolve())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('review', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--check-response', type=Path)
    args = parser.parse_args()
    require(bool(args.output) != bool(args.check_response), 'Choose --output or --check-response')
    review = read_json(args.review)
    if args.output:
        require(args.output.resolve() != args.review.resolve(), 'Output cannot overwrite the review source')
        result = build(review, args.output)
    else:
        result = check_response(review, read_json(args.check_response))
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as error:
        raise SystemExit(f'Review error: {error}') from error
