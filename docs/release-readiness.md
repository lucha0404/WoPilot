# WoPilot release status and known issues

Reviewed 2026-11-16. The owner has explicitly authorized a manual Windows installer release from the cleaned public source, with known issues disclosed. This supersedes the earlier source-only pause. The installer retains fingerprint functionality and the pinned 148 engine; no browser-security repair is claimed.

## Browser security: unresolved and disclosed

The upstream application pins Fingerprint Chromium 148.0.7778.215. The engine project's current latest official binary is 150.0.7871.186. Its source tag contains documentation rather than browser patches; the project says patches are published with a subsequent binary release.

Chrome's official CVE-2026-125350 record describes an XML use-after-free fixed in 157.0.8103.50, with active exploitation recorded by CISA. Both engine baselines predate that fix. No verifiable backport mapping was found. This is not a claim that an exploit has been reproduced against every fork binary, and neither browser is presented as patched.

Sources:

- [Official fingerprint engine release](https://github.com/adryfish/fingerprint-chromium/releases/latest)
- [150 source-tag tree](https://api.github.com/repos/adryfish/fingerprint-chromium/git/trees/150.0.7871.186?recursive=1)
- [Delayed patch-source policy](https://github.com/adryfish/fingerprint-chromium#build-from-source)
- [Chrome CNA record and CISA evidence](https://www.cve.org/CVERecord?id=CVE-2026-125350)
- [Google security release](https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html)

Checking a 150 binary's publisher hash would establish file provenance, not close this gap. BotBrowser and CloakBrowser were screened; their licensing and launch interfaces do not provide a simple, free, auditable drop-in replacement.

The pinned preparation and packaging scripts have been restored for the authorized manual build, together with their offline regression tests. The inherited automatic release workflow and Arch recipe remain removed. A dedicated Windows workflow builds in a disposable runner and must pass installation/startup/upgrade/uninstall checks before its artifact can be reviewed for manual publication. These checks do not establish current browser exploit resistance.

## Third-party terms: partly repaired

- Original CCBaga project work retains its MIT notice.
- Fingerprint Chromium retains BSD-3-Clause attribution. The existing Chromium resources contain an embedded credits page; absence of a separate LICENSE file does not establish missing attribution. A future engine's actual credits must be preserved and checked again.
- Pika free-icon license, fixed provenance and drawing replacements are recorded under `vendor/cromma-ui`. This repair does not license the surrounding component library.
- Cromma UI is a copied local library with references to other interface projects. No independent first-party redistribution terms were found. That gap is disclosed in this release and is not cured by the top-level MIT notice. A rights-holder statement or replacement of the affected implementation is still needed to settle the component terms; no permission notice is invented.
- LobeHub, GLib and Unicode notices remain present. Other dependencies keep their respective terms; no complete binary-notice audit is claimed for an installer that has not been built.

This is a source fork on GitHub. The platform's public-fork permission is distinct from permission to distribute every component in an installer; it cannot confer rights a contributor does not own.

Sources: [upstream third-party notice](https://github.com/liseami/CCBaga/blob/v0.2.50/NOTICE.md), [GitHub public-fork terms](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#5-license-grant-to-other-users).

## Personal data

The friend branch was reconstructed from the official tag and a reviewed final customization diff. Private local commits, personal author metadata and local update paths are not imported. New commits use a GitHub no-reply identity. No account vaults, browser profiles, proxy credentials or private backups are included.

The application identifier and Windows registration namespace are separate from the official application. No data migration is performed. Ignore rules and `scripts/check-source-privacy.py` reject known private file types; new content and artifact contents still need review.

Only an installer built from a public commit in a disposable runner, its checksum and public build information may be published after review. No account export or maintainer profile is included. Actual completed checks belong in the matching Release; source checks alone do not establish website login or browser exploit resistance.

## Future maintenance

1. Confirm Cromma UI rights, or replace its affected implementation, and retain applicable notices.
2. Select an engine with inspectable patches and current security coverage; verify its archive digest, architecture, source and licenses.
3. Preserve strict source/asset checksums and the engine-preparation tests; do not turn a newer version number into an unsupported security claim.
4. Test fingerprint behavior, profile isolation, data recovery, measurements and a fresh install using synthetic accounts.
5. Inspect the source history and new binary artifacts for private data before enabling a release workflow.

The current Windows installer is shared with these limitations disclosed. It must not be described as a browser-security-audited or fully third-party-license-cleared release. No macOS or Linux installer is offered by this fork.
