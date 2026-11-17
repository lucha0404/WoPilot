# .github/
> L2 | 父级: ../CLAUDE.md

workflows/checks.yml: 朋友版只读源码检查，不下载或运行指纹内核，不安装应用，不签名或上传发行物。
dependabot.yml: 继承的依赖更新建议，不授予发布权限。

原上游 release 工作流已移除；恢复打包条件见 docs/release-readiness.md。

Ubuntu 隔离任务仅测试底层文件事务；不使用真实内核，不制作发行物。
