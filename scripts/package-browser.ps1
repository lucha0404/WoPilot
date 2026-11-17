# [INPUT]: 仅交付源码的分支，尚无通过安全验收的 Windows 指纹内核。
# [OUTPUT]: 即使存在手工放入的引擎，也明确拒绝打包。
# [POS]: Windows 构建阻断入口，不读取或修改引擎、用户资料及系统设置。
# [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
throw 'Browser engine packaging is disabled for this source-only fork. See docs/release-readiness.md.'
