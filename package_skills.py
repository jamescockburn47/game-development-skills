"""Package the two independent skills; optionally install the same payloads."""
from pathlib import Path
import argparse
import os
import re
import shutil
import zipfile

NAMES = ('evidence-led-game-development', 'open-world-game-development')
ROOT = Path(__file__).resolve().parent
SHARED = ('references/design-review.md', 'scripts/build_design_review.py',
          'scripts/review_document.py', 'assets/design-review-content.js', 'assets/design-review-sections.css',
          'assets/design-review.html', 'assets/design-review.css', 'assets/design-review.js',
          'assets/design-review-example.json')


def check_shared(sync=False):
    canonical = ROOT / 'skills' / NAMES[0]
    mirror = ROOT / 'skills' / NAMES[1]
    for relative in SHARED:
        source, target = canonical / relative, mirror / relative
        if sync:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        if not target.is_file() or target.read_bytes() != source.read_bytes():
            raise ValueError(f'Shared review resource differs: {target}; run --sync-shared after editing the canonical general skill')


def payload(name):
    source = ROOT / 'skills' / name
    files = [Path('SKILL.md'), Path('agents/openai.yaml'),
             *sorted(path.relative_to(source)
                     for path in (source / 'references').glob('*.md')),
             *(Path(name) for name in SHARED if not name.startswith('references/'))]
    result = {}
    for relative in files:
        path = source / relative
        if not path.resolve().is_relative_to(source.resolve()):
            raise ValueError(f'Payload escapes skill folder: {relative}')
        data = path.read_bytes()
        if not data.strip():
            raise ValueError(f'Empty payload file: {relative}')
        if path.suffix == '.md':
            for link in re.findall(r'\]\(([^)]+)\)', data.decode('utf-8')):
                if '://' in link or link.startswith('#'):
                    continue
                target = (path.parent / link.split('#')[0]).resolve()
                if not target.is_relative_to(source.resolve()) or not target.is_file():
                    raise ValueError(f'Nonportable or missing reference: {relative}: {link}')
                if target.relative_to(source.resolve()) not in files:
                    raise ValueError(f'Reference excluded from bundle: {relative}: {link}')
        result[f'{name}/{relative.as_posix()}'] = data
    return result


def archive(path, files):
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as bundle:
        for name, data in sorted(files.items()):
            entry = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o644 << 16
            bundle.writestr(entry, data)
    with zipfile.ZipFile(path) as bundle:
        if bundle.testzip() is not None or set(bundle.namelist()) != set(files):
            raise ValueError(f'Archive integrity failed: {path}')
        for name, data in files.items():
            if bundle.read(name) != data:
                raise ValueError(f'Archive content mismatch: {name}')
    print(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--install', action='store_true')
    parser.add_argument('--sync-shared', action='store_true', help='Regenerate the open-world review resources from the canonical general skill')
    args = parser.parse_args()
    check_shared(args.sync_shared)
    all_files = {}
    for name in NAMES:
        files = payload(name)
        archive(ROOT / 'dist' / f'{name}.zip', files)
        all_files.update(files)
    archive(ROOT / 'dist' / 'game-development-skills.zip', all_files)
    if args.install:
        codex_root = Path(os.environ.get('CODEX_HOME', Path.home() / '.codex'))
        for name, data in all_files.items():
            target = codex_root / 'skills' / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / 'skills' / name, target)
            if target.read_bytes() != data:
                raise ValueError(f'Installed content mismatch: {target}')
        print(f'Installed both skills in {codex_root / "skills"}')


if __name__ == '__main__':
    main()
