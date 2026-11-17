# workflows/
> L2 | 父级: ../CLAUDE.md

checks.yml: Windows 源码/固定来源/隐私文件检查，Ubuntu 底层文件事务回归，不制作发行物。
windows-installer.yml: 仅 workflow_dispatch，Windows x64 固定引擎准备、无私人数据构建及空白 CI 安装/启动/升级/卸载验证；仅上传安装包、校验摘要和公开构建信息。没有写仓库或自动发布权限。

源码检查与安装验收不代表浏览器安全补丁覆盖或第三方授权已完全核清。
