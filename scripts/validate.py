#!/usr/bin/env python3
"""Offline curation gate. Pattern checks are heuristics, not a privacy audit."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    '.gitignore', 'LICENSE', 'MANIFEST.sha256', 'README.md',
    'components/README.md', 'components/geometry.ts',
    'docs/ARCHITECTURE.md', 'docs/PROVENANCE.md', 'docs/ROADMAP.md',
    'docs/SECURITY.md', 'docs/VALIDATION.md', 'package.json',
    'provenance.json', 'scripts/validate.py', 'tests/geometry.test.mjs',
}
PATTERNS = {
    'machine-local home path': re.compile(r'/(?:Us' + r'ers|ho' + r'me)/[^\s/]+/'),
    'private key material': re.compile(r'-----BEGIN ' + r'(?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'common token prefix': re.compile(r'(?:gh' + r'[posu]_[A-Za-z0-9]{20,}|sk' + r'-[A-Za-z0-9]{20,})'),
    'email address': re.compile(r'[A-Za-z0-9_.+-]+' + r'@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_relative(value):
    if not isinstance(value, str) or not value or '\\' in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and all(p not in ('..', '.') for p in path.parts) and str(path) == value


def validate(source_root=None):
    errors = []
    actual = set()
    for path in ROOT.rglob('*'):
        rel = path.relative_to(ROOT)
        if rel.parts[0] == '.git':
            continue
        if path.is_symlink():
            errors.append(f'{rel}: symlink not allowed')
        if path.is_file() or path.is_symlink():
            actual.add(rel.as_posix())
    if actual != EXPECTED:
        errors.append(f'inventory mismatch: missing={sorted(EXPECTED - actual)}, extra={sorted(actual - EXPECTED)}')
    for name in sorted(actual & EXPECTED):
        path = ROOT / name
        if path.is_symlink():
            continue
        text = path.read_text(encoding='utf-8')
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                errors.append(f'{name}: sensitive-pattern rule: {label}')
        if any(line.rstrip(' \t') != line for line in text.splitlines()):
            errors.append(f'{name}: trailing whitespace')
        if not text.endswith('\n'):
            errors.append(f'{name}: missing final newline')
        if path.suffix == '.md':
            for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith('#'):
                    continue
                candidate = (path.parent / unquote(parsed.path)).resolve()
                if not candidate.is_relative_to(ROOT) or not candidate.is_file():
                    errors.append(f'{name}: broken or escaping local link')
    manifest = {}
    for line in (ROOT / 'MANIFEST.sha256').read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        if not match or not safe_relative(match[2]):
            errors.append('invalid manifest entry')
            continue
        expected_hash, name = match.groups()
        if name in manifest:
            errors.append(f'{name}: duplicate manifest entry')
        manifest[name] = expected_hash
        if name not in EXPECTED or not (ROOT / name).is_file() or (ROOT / name).is_symlink():
            errors.append(f'{name}: invalid manifest target')
        elif digest(ROOT / name) != expected_hash:
            errors.append(f'{name}: manifest hash mismatch')
    if set(manifest) != EXPECTED - {'MANIFEST.sha256'}:
        errors.append('manifest coverage mismatch')
    provenance = json.loads((ROOT / 'provenance.json').read_text())
    if provenance.get('schema_version') != 1 or provenance.get('fingerprint_algorithm') != 'SHA-256':
        errors.append('unsupported provenance schema')
    sources = {}
    for item in provenance['sources']:
        name, fingerprint = item['path'], item['sha256']
        if not safe_relative(name) or not re.fullmatch(r'[0-9a-f]{64}', fingerprint):
            errors.append('invalid provenance source')
            continue
        if name in sources:
            errors.append('duplicate provenance source')
        sources[name] = fingerprint
        if source_root is not None:
            original = (source_root / name).resolve()
            if not original.is_relative_to(source_root) or not original.is_file() or digest(original) != fingerprint:
                errors.append(f'{name}: private source fingerprint mismatch')
    if len(provenance['excerpts']) != 1:
        errors.append('unexpected excerpt count')
    for excerpt in provenance['excerpts']:
        name = excerpt['showcase_path']
        if name != 'components/geometry.ts' or excerpt['source_path'] != 'Code/lib/geometry.ts':
            errors.append('unexpected excerpt mapping')
            continue
        fingerprint = digest(ROOT / name)
        if excerpt.get('unchanged') is not True or fingerprint != excerpt['sha256'] or fingerprint != sources.get(excerpt['source_path']):
            errors.append('excerpt provenance mismatch')
    package = json.loads((ROOT / 'package.json').read_text())
    if package.get('private') is not True or package.get('license') != 'UNLICENSED':
        errors.append('package publication/license gate missing')
    if package.get('dependencies') or package.get('devDependencies'):
        errors.append('external package dependencies not allowed')
    if errors:
        for error in errors:
            print(f'FAIL: {error}', file=sys.stderr)
        return 1
    print(f'PASS: {len(actual)} curated files; {len(manifest)} manifest hashes; local links; provenance; pattern/whitespace checks')
    if source_root is not None:
        print(f'PASS: {len(sources)} private source fingerprints and unchanged excerpt verified')
    else:
        print('NOTE: private source fingerprint comparison not requested')
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, help='Optional private repository root; allowlisted sources only')
    args = parser.parse_args()
    try:
        return validate(args.source_root.resolve() if args.source_root is not None else None)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'FAIL: validation could not complete ({type(error).__name__})', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
