# WoPilot source maintenance

This source fork is based on CCBaga `v0.2.50` (`568fed199dcdf22468186449116c9ab4cfa6de62`). It preserves the WoPilot name and artwork and does not use upstream's binary updater.

For manual Windows builds and future updates:

1. Read and disclose the current engine-security and component-license limitations in `docs/release-readiness.md`; do not claim them resolved without first-party evidence.
2. Review the next official stable source, preserve attribution and the fork's separate application identity, and verify actual browser patches and engine checksums.
3. Run source, native, profile-isolation and clean-install tests with synthetic data. Keep real application data outside the checkout and build resources.
4. Review the complete tracked tree, new commit metadata, archive members and artifact contents for personal data before publishing.
5. Use the manual Windows workflow on a public commit, then review the actual artifact and successful clean-install results before publishing a Release. Frontend compilation alone does not approve an installer.

No installed application or personal data is migrated by this repository. Backups belong outside the checkout. There is no unattended installation or update service.
