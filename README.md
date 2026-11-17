# WoPilot

[简体中文](README.zh-CN.md)

WoPilot is an unofficial Windows customization of [CCBaga v0.2.50](https://github.com/liseami/CCBaga/releases/tag/v0.2.50), with its own name, artwork and application-data identifier. It retains local identity management, recovery, isolated profiles and fingerprint features. It does not promise protection from account restrictions.

## Download and install

Open [Releases](https://github.com/lucha0404/WoPilot/releases/latest) and download **WoPilot-0.2.50-windows-x86_64-setup.exe**. Run it on Windows 10 or 11, 64-bit. The installer includes the companion browser. If Microsoft WebView2 is missing, setup downloads its official runtime.

The installer is not Authenticode-signed, so Windows may show an unknown-publisher warning. Verify the GitHub download source and the SHA-256 checksum supplied with the release. Use your own account and network settings after installation. No maintainer profile or credentials are supplied.

## Known issues

- The bundled fingerprint browser remains **148.0.7778.215**. Coverage of recent Chromium security fixes has not been verified; this release does not fix that upstream limitation.
- Cromma UI's independent redistribution terms remain unconfirmed. Original MIT and third-party notices are preserved; the top-level MIT license is not a blanket license for every component.
- Pika free-icon attribution and drawings have been checked and repaired in this source. This does not resolve Cromma UI's component-code terms.
- Updates are manual through this fork's Releases. The official CCBaga binary updater is disabled to preserve WoPilot customization.

See [release status and evidence](docs/release-readiness.md) and the release notes for the exact build, checks and limitations. The earlier source-only pause has been replaced by an explicitly authorized manual Windows release with these issues disclosed. There is no automatic publishing workflow.

## Source checks

```sh
bun install --frozen-lockfile
bun test
bun run build
python scripts/test-fetch-browser.py
python vendor/cromma-ui/verify-pika-source.py
python scripts/check-source-privacy.py
```

Windows installers are built and tested in a disposable GitHub runner using the manually triggered `Build Windows installer` workflow. It has read-only repository permissions and uploads only the installer, checksum and public build information for review. Publishing a Release is a separate manual action.

## Data and attribution

This fork uses its own application-data identifier and Windows registration namespace, with no automatic migration of existing CCBaga data. Never share someone else's app-data directory, identity exports, credentials, cookies or proxy configuration. Private customization history is not imported and new commits use a GitHub no-reply identity.

[LICENSE](LICENSE) retains the upstream MIT notice for original project work. [NOTICE.md](NOTICE.md) records separate third-party terms and unresolved provenance. The [usage guide](docs/usage.md) describes the underlying features. [Maintenance notes](UPDATE-WOPILOT.md) describe future updates.
