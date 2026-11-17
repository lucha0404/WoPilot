#!/usr/bin/env python3
# [INPUT]: 仅交付源码的 WoPilot 分支，尚无通过安全验收的指纹内核。
# [OUTPUT]: 下载或运行外部工具前明确失败，并指向重新开放发布的条件。
# [POS]: 保留旧命令入口的失败提示；不下载、不准备或覆盖浏览器资源。
# [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md


def main():
    raise SystemExit(
        'Browser engine preparation is disabled for this source-only fork. '
        'See docs/release-readiness.md.'
    )


if __name__ == '__main__':
    main()
