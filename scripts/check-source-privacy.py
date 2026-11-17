#!/usr/bin/env python3
"""Reject private-data file types from the shareable source tree."""
from pathlib import Path, PurePosixPath
import subprocess

ROOT = Path(__file__).resolve().parent.parent
PRIVATE_NAMES = {
    'key.bin', 'cookies', 'login data', 'web data', 'history', 'local state',
    'preferences', 'secure preferences', '.env',
}
PRIVATE_PARTS = {
    'identity-vault', 'user data', 'private-state-before', 'installation-before',
    'node_modules', 'windowsbrowser', 'linuxbrowser', 'browser.app',
}
PRIVATE_SUFFIXES = {
    '.pem', '.ppk', '.p8', '.p12', '.pfx', '.key', '.baga', '.bagapack',
    '.sqlite', '.sqlite3', '.sqlite-wal', '.sqlite-shm', '.har',
}


def private_path(name):
    path = PurePosixPath(name.lower())
    return (
        path.parts[0] in {'browser', 'backups', 'screenshots'}
        or bool(set(path.parts) & PRIVATE_PARTS)
        or path.name in PRIVATE_NAMES
        or path.suffix in PRIVATE_SUFFIXES
        or (path.name.startswith('.env.') and path.name != '.env.example')
        or path.name.startswith('identities.sqlite')
    )


if __name__ == '__main__':
    for sample in ('backup/identity.bagapack', 'Identity-Vault/key.bin',
                   'profile/Default/Cookies', 'config/.env.production',
                   'browser/config.json', 'backups/profile.zip',
                   'browser-runtime/WindowsBrowser/chrome.exe'):
        assert private_path(sample), sample
    for sample in ('.env.example', 'src/identities/store.rs',
                   'vendor/cromma-ui/LICENSE.pika.txt', 'browser-runtime/version.txt'):
        assert not private_path(sample), sample
    names = subprocess.check_output(
        ['git', '-C', str(ROOT), 'ls-files', '--cached', '--others',
         '--exclude-standard', '-z'],
    ).decode('utf-8').split('\0')
    files = sorted({name for name in names if name and (ROOT / name).is_file()})
    rejected = [name for name in files if private_path(name)]
    if rejected:
        raise SystemExit('Private files must not be shared:\n' + '\n'.join(rejected))
    for retired in ('.github/workflows/release.yml', 'packaging/arch/PKGBUILD'):
        assert not (ROOT / retired).exists(), f'Retired release entry restored: {retired}'
    print(f'Checked {len(files)} source files; no forbidden private-data paths. '
          'Contents and commit metadata still require separate review.')
