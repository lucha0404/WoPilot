# workflows/
> L2 | 父级: ../CLAUDE.md

checks.yml: Windows 源码单元测试、前端构建、旧内核下载和打包阻断、Pika 来源和私人文件检查。仅 contents:read，不保留 Git 凭据，不访问 Secrets，不制作或发布安装包。

没有 release 工作流；源码通过不代表浏览器安全或实机安装验收。

Ubuntu 隔离任务仅测试底层文件事务；不使用真实内核，不制作发行物。
