#!/usr/bin/env python3
# [INPUT]: 源码分支真实下载/打包入口、临时伪引擎与外部进程边界拦截。
# [OUTPUT]: 三平台下载前阻断、手工旧引擎不能绕过打包阻断且文件保持不变。
# [POS]: 不联网、不下载或运行真实引擎，不触碰用户资料。
# [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
import os
from pathlib import Path
import runpy
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent


class SourceOnlyTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='wopilot-source-only-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / 'scripts').mkdir()
        (self.root / 'browser-runtime').mkdir()
        self.fetch = self.root / 'scripts/fetch-browser.py'
        shutil.copyfile(ROOT / 'scripts/fetch-browser.py', self.fetch)

    def test_download_is_blocked_before_external_tools(self):
        for system in ('Windows', 'Linux', 'Darwin'):
            with self.subTest(system=system), \
                    patch('platform.system', return_value=system), \
                    patch('platform.machine', return_value='x86_64'), \
                    patch.object(subprocess, 'Popen', side_effect=AssertionError(
                        f'{system} requested an external process before the source-only gate')) as process:
                with self.assertRaisesRegex(SystemExit, r'docs/release-readiness\.md'):
                    runpy.run_path(str(self.fetch), run_name='__main__')
                process.assert_not_called()
                self.assertEqual(list((self.root / 'browser-runtime').iterdir()), [])

    @unittest.skipUnless(os.name == 'nt', 'Requires native Windows PowerShell')
    def test_windows_packaging_rejects_even_a_matching_old_engine(self):
        script = self.root / 'scripts/package-browser.ps1'
        shutil.copyfile(ROOT / 'scripts/package-browser.ps1', script)
        engine = self.root / 'browser-runtime/WindowsBrowser'
        engine.mkdir()
        (engine / 'chrome.exe').write_bytes(b'fixture, never execute')
        for path in (engine / 'version.txt', engine.parent / 'version.txt'):
            path.write_text('148.0.7778.215\n', encoding='utf-8')
        before = {path.relative_to(self.root): path.read_bytes()
                  for path in self.root.rglob('*') if path.is_file()}
        shells = [shell for shell in ('pwsh', 'powershell') if shutil.which(shell)]
        self.assertTrue(shells, 'Windows PowerShell is required to verify the packaging gate')
        for shell in shells:
            with self.subTest(shell=shell):
                result = subprocess.run(
                    [shell, '-NoLogo', '-NoProfile', '-NonInteractive', '-File', str(script)],
                    capture_output=True, text=True, timeout=30,
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('docs/release-readiness.md', result.stderr)
                self.assertEqual(before, {path.relative_to(self.root): path.read_bytes()
                                         for path in self.root.rglob('*') if path.is_file()})

    @unittest.skipUnless(shutil.which('sh'), 'Requires a POSIX shell')
    def test_unix_packaging_rejects_supplied_engines_without_changing_them(self):
        script = self.root / 'scripts/package-browser.sh'
        shutil.copyfile(ROOT / 'scripts/package-browser.sh', script)
        for name in ('LinuxBrowser/chrome', 'Browser.app/Contents/MacOS/chrome'):
            binary = self.root / 'browser-runtime' / name
            binary.parent.mkdir(parents=True)
            binary.write_bytes(b'#!/bin/sh\nexit 99\n')
            binary.chmod(0o755)
        for name in ('version.txt', 'LinuxBrowser/version.txt'):
            (self.root / 'browser-runtime' / name).write_text('148.0.7778.215\n', encoding='utf-8')
        (self.root / 'browser-runtime/Browser.zip').write_bytes(b'preserve existing archive')
        before = {path.relative_to(self.root): path.read_bytes()
                  for path in self.root.rglob('*') if path.is_file()}
        command = ('uname() { printf "%s\\n" "$FIXTURE_SYSTEM"; }; '
                   'python3() { echo "Unexpected packaging tool" >&2; return 97; }; '
                   'sh() { echo "Unexpected branding tool" >&2; return 98; }; . "$0"')
        for system in ('Linux', 'Darwin'):
            with self.subTest(system=system):
                result = subprocess.run(
                    [shutil.which('sh'), '-c', command, script.as_posix()],
                    env=os.environ | {'FIXTURE_SYSTEM': system}, cwd=self.root,
                    capture_output=True, text=True, timeout=30,
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('docs/release-readiness.md', result.stderr)
                self.assertEqual(before, {path.relative_to(self.root): path.read_bytes()
                                         for path in self.root.rglob('*') if path.is_file()})


if __name__ == '__main__':
    unittest.main(verbosity=2)
