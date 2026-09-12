"""Verify the public source, reproducible downloads and offline review example."""
import argparse
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote
import zipfile
import package_skills as packer

ROOT = Path(__file__).resolve().parent
SKILL = ROOT / 'skills' / packer.NAMES[0]
EXAMPLE = Path('examples/public/design-review.html')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def builder_module():
    scripts = SKILL / 'scripts'
    sys.path.insert(0, str(scripts))
    spec = importlib.util.spec_from_file_location('public_review_builder', scripts / 'build_design_review.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def generated_files():
    """Generate in isolation, so verification cannot silently repair stale artifacts."""
    result, combined = {}, {}
    packer.check_shared()
    with tempfile.TemporaryDirectory(prefix='game-skill-verify-') as temporary:
        folder = Path(temporary)
        for name in packer.NAMES:
            files = packer.payload(name)
            combined.update(files)
            target = folder / f'{name}.zip'
            with contextlib.redirect_stdout(io.StringIO()):
                packer.archive(target, files)
            result[Path('dist') / target.name] = target.read_bytes()
        target = folder / 'game-development-skills.zip'
        with contextlib.redirect_stdout(io.StringIO()):
            packer.archive(target, combined)
        result[Path('dist') / target.name] = target.read_bytes()
        review = json.loads((SKILL / 'assets/design-review-example.json').read_text(encoding='utf-8'))
        require(review['example'] is True and review['game'] == {'description': '', 'recorded_from': None},
                'Public example must be blank and unable to authorize a build')
        example_root = folder / 'example'
        builder_module().build(review, example_root / EXAMPLE.name)
        for path in example_root.rglob('*'):
            if path.is_file():
                result[EXAMPLE.parent / path.relative_to(example_root)] = path.read_bytes()
    return result


def source_files():
    files = {Path(name) for name in ('README.md', 'AGENTS.md', '.gitignore', '.gitattributes',
                                    'package_skills.py', 'verify_public.py', '.github/workflows/verify.yml',
                                    'public_tests/test_review.py')}
    if (ROOT / 'LICENSE').is_file():
        files.add(Path('LICENSE'))
    for name in packer.NAMES:
        files.update(Path('skills') / path for path in packer.payload(name))
    return files


def check_sources(files, published):
    secret = re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|'
                        r'gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|'
                        r'sk-(?:proj-)?[A-Za-z0-9_-]{40,}')
    local_path = re.compile(r'(?:[A-Z]:[\\/]Users[\\/]|/Users/|/home/)[A-Za-z0-9_.-]+')
    for relative in sorted(files):
        path = ROOT / relative
        require(path.is_file() and not path.is_symlink(), f'Missing or linked public source: {relative}')
        content = path.read_text(encoding='utf-8')
        require(not secret.search(content), f'Credential-shaped text in {relative}; inspect without printing it')
        require(not local_path.search(content), f'Personal machine path in {relative}')
        if path.suffix in ('.py', '.js', '.css', '.html'):
            require(sum(bool(line.strip()) for line in content.splitlines()) <= 300, f'Source exceeds 300 lines: {relative}')
        if path.suffix == '.py':
            compile(content, str(relative), 'exec')
        if path.suffix == '.md':
            for link in re.findall(r'\]\(([^)]+)\)', content):
                if '://' in link or link.startswith('#'):
                    continue
                target = (path.parent / unquote(link.split('#')[0])).resolve()
                require(target.is_relative_to(ROOT), f'Link leaves repository: {relative}')
                require(target.relative_to(ROOT) in published, f'Link points outside public files: {relative}: {link}')
    for name in packer.NAMES:
        text = (ROOT / 'skills' / name / 'SKILL.md').read_text(encoding='utf-8')
        require(text.startswith('---\n') and f'name: {name}\n' in text and '\ndescription: ' in text,
                f'Invalid skill frontmatter: {name}')


def check_git_paths(published):
    if not (ROOT / '.git').exists():
        print('No Git metadata: public source and artifacts checked; tracked-tree check not available.')
        return
    tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    unexpected = {Path(path) for path in tracked if path} - published
    require(not unexpected, 'Unexpected tracked paths: ' + ', '.join(str(path) for path in sorted(unexpected)))
    match = subprocess.run(['git', 'diff', '--quiet', '--'], cwd=ROOT)
    require(match.returncode == 0, 'Working files differ from the Git index; stage the intended public changes before verifying')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh-example', action='store_true', help='Intentionally regenerate only the blank public example')
    args = parser.parse_args()
    generated = generated_files()
    if args.refresh_example:
        for relative, content in generated.items():
            if relative.is_relative_to(EXAMPLE.parent):
                target = ROOT / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
        print('Regenerated the blank public example from the packaged source.')
    files = source_files()
    published = files | set(generated)
    check_sources(files, published)
    check_git_paths(published)
    for relative, expected in generated.items():
        target = ROOT / relative
        require(target.is_file() and target.read_bytes() == expected,
                f'Generated file differs: {relative}; regenerate packages/example explicitly')
    # Inspect every archive member too; generation must not introduce unreviewed material.
    for relative in generated:
        if relative.suffix == '.zip':
            with zipfile.ZipFile(ROOT / relative) as archive:
                require(archive.testzip() is None, f'Damaged archive: {relative}')
    subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'public_tests', '-p', 'test_*.py', '-v'],
                   cwd=ROOT, check=True)
    print(f'Public verification passed: {len(files)} source files, {len(generated)} generated files, focused behavior tests.')
    print('Browser interaction, visual quality and model compliance are not certified by this command.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(f'Public verification failed: {error}') from error
