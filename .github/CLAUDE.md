# .github/
> L2 | 父级: ../CLAUDE.md

workflows/checks.yml: 只读源码、来源和隐私文件检查。
workflows/windows-installer.yml: 手动构建 Windows 安装包，在可丢弃 runner 试装、启动、升级和卸载后，仅上传三个明确产物供人工复核；contents:read，无自动 Releases 发布。
dependabot.yml: 依赖更新建议。

已知问题见 docs/release-readiness.md。未恢复上游自动发布工作流。
