#!/bin/sh
# [INPUT]: 仅交付源码的分支，尚无通过安全验收的 macOS/Linux 指纹内核。
# [OUTPUT]: 即使存在手工放入的引擎，也明确拒绝打包。
# [POS]: 跨平台构建阻断入口，不品牌化、签名、复制或覆盖任何引擎资源。
# [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
printf '%s\n' 'Browser engine packaging is disabled for this source-only fork. See docs/release-readiness.md.' >&2
exit 1
