# WoPilot release readiness

Reviewed 2026-11-16. This is a source-only fork of CCBaga v0.2.50. Fingerprint functionality remains in the source, but the old engine is neither distributed nor automatically fetched.

## Browser security: unresolved, release blocked

The upstream application pins Fingerprint Chromium 148.0.7778.215. The engine project's current latest official binary is 150.0.7871.186. Its source tag contains documentation rather than browser patches; the project says patches are published with a subsequent binary release.

Chrome's official CVE-2026-125350 record describes an XML use-after-free fixed in 157.0.8103.50, with active exploitation recorded by CISA. Both engine baselines predate that fix. No verifiable backport mapping was found. This is not a claim that an exploit has been reproduced against every fork binary, and neither browser is presented as patched.

Sources:

- [Official fingerprint engine release](https://github.com/adryfish/fingerprint-chromium/releases/latest)
- [150 source-tag tree](https://api.github.com/repos/adryfish/fingerprint-chromium/git/trees/150.0.7871.186?recursive=1)
- [Delayed patch-source policy](https://github.com/adryfish/fingerprint-chromium#build-from-source)
- [Chrome CNA record and CISA evidence](https://www.cve.org/CVERecord?id=CVE-2026-125350)
- [Google security release](https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html)

Checking a 150 binary's publisher hash would establish file provenance, not close this gap. BotBrowser and CloakBrowser were screened; their licensing and launch interfaces do not provide a simple, free, auditable drop-in replacement.

Normal engine-download and packaging entry points now fail explicitly. The inherited release workflow and Arch recipe that independently fetched the old engine are removed. Browser logic and synthetic transaction tests remain for review. No safe browser operation or fresh-install acceptance is claimed.

## Third-party terms: partly repaired

- Original CCBaga project work retains its MIT notice.
- Fingerprint Chromium retains BSD-3-Clause attribution. The existing Chromium resources contain an embedded credits page; absence of a separate LICENSE file does not establish missing attribution. A future engine's actual credits must be preserved and checked again.
- Pika free-icon license, fixed provenance and drawing replacements are recorded under `vendor/cromma-ui`. This repair does not license the surrounding component library.
- Cromma UI is a copied local library with references to other interface projects. No independent first-party redistribution terms were found. Obtain a rights-holder statement covering those sources, or replace the affected implementation, before binary distribution. Do not invent a license notice.
- LobeHub, GLib and Unicode notices remain present. Other dependencies keep their respective terms; no complete binary-notice audit is claimed for an installer that has not been built.

This is a source fork on GitHub. The platform's public-fork permission is distinct from permission to distribute every component in an installer; it cannot confer rights a contributor does not own.

Sources: [upstream third-party notice](https://github.com/liseami/CCBaga/blob/v0.2.50/NOTICE.md), [GitHub public-fork terms](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#5-license-grant-to-other-users).

## Personal data

The friend branch was reconstructed from the official tag and a reviewed final customization diff. Private local commits, personal author metadata and local update paths are not imported. New commits use a GitHub no-reply identity. No account vaults, browser profiles, proxy credentials or private backups are included.

The application identifier and Windows registration namespace are separate from the official application. No data migration is performed. Ignore rules and `scripts/check-source-privacy.py` reject known private file types; new content and artifact contents still need review.

No installer, updater manifest, account export or engine binary is published with this branch. Source checks do not establish real website login, browser exploit resistance or fresh-install acceptance.

## Resume packaging only after

1. Confirm Cromma UI rights, or replace its affected implementation, and retain applicable notices.
2. Select an engine with inspectable patches and current security coverage; verify its archive digest, architecture, source and licenses.
3. Remove the source-only stop conditions in one reviewed change and restore actual engine-preparation tests.
4. Test fingerprint behavior, profile isolation, data recovery, measurements and a fresh install using synthetic accounts.
5. Inspect the source history and new binary artifacts for private data before enabling a release workflow.

Until then, friends can inspect or contribute to this fork; it is not a ready-to-use application.
