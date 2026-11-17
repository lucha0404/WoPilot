# WoPilot

[简体中文](README.zh-CN.md)

A branded source-code fork of [CCBaga](https://github.com/liseami/CCBaga), based on official `v0.2.50`. Local identity management, recovery, isolated profiles and fingerprint features remain in the source. This is not an official CCBaga release and does not promise protection from account restrictions.

## Source review only

**No approved WoPilot installer is available. This branch is not ready to install.**

- The old fingerprint engine is not included. Automatic engine downloads and normal packaging are blocked.
- Fingerprint Chromium 148 and upstream's current 150 binary have no verified mapping to current Chromium security fixes. A version bump or matching checksum does not establish patch coverage.
- Pika free-icon notices and provenance have been repaired. Cromma UI component redistribution terms still require confirmation; the top-level MIT notice does not settle that question.
- No maintainer account vault, browser profile, credentials or private backups are included. Private customization commits are not imported; new commits use a GitHub no-reply identity.

Read [release readiness and evidence](docs/release-readiness.md) before building or distributing anything. This fork uses its own application identifier and Windows browser registration namespace, with no automatic migration of existing app data.

## Source checks

Install Bun, Node.js and Python, then run:

```sh
bun install --frozen-lockfile
bun test
bun run build
python scripts/test-fetch-browser.py
python vendor/cromma-ui/verify-pika-source.py
python scripts/check-source-privacy.py
```

Browser preparation and packaging commands deliberately fail while the release blockers remain. Source checks do not launch Claude, access real account data, install apps or run the old browser. Native platform tests require the relevant platform toolchain and are separate from these checks.

## Updates and attribution

There is no official binary auto-updater in this fork. Future source and engine updates require review and fresh verification; see [maintenance](UPDATE-WOPILOT.md). Never share another person's app-data directory, identity exports, credentials, cookies or proxy configuration.

[LICENSE](LICENSE) retains the upstream MIT notice for original project work. [NOTICE.md](NOTICE.md) records separate third-party terms and unresolved provenance. No blanket third-party license claim is made. Upstream history and copyright notices are retained. The [upstream usage guide](docs/usage.md) explains the underlying features rather than promising this branch is installable.
