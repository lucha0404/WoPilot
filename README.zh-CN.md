# WoPilot

[English](README.md)

WoPilot 基于 [CCBaga 官方 v0.2.50](https://github.com/liseami/CCBaga/releases/tag/v0.2.50)，保留本地账号资料管理、失败恢复、独立浏览器资料、指纹及环境检查源码，并使用 WoPilot 名称和图标。它不是 CCBaga 官方发行版，也不承诺账号不会被封。

## 当前只交付源码

**目前没有通过安全和授权核验的 WoPilot 安装包，请勿把此分支当作开箱即用的浏览器发行版。**

- 指纹功能源码保留。旧浏览器内核不进入仓库，自动下载和正常打包入口已停止。
- 原先使用的 148 内核，以及指纹项目目前最新的 150 内核，都没有取得覆盖当前 Chromium 安全修复的充分证据。更换版本号或校验摘要不等于漏洞已经修复。
- 已补免费 Pika 图标授权，删除或替换来源未核实的图形。Cromma UI 组件自身的再分发条款仍需原作者确认，不能用顶层 MIT 声明代替。
- 不包含维护者的账号保险库、浏览器资料、代理凭据和私人备份。未导入本机定制的私有提交历史，新提交使用 GitHub 隐私邮箱。

证据和恢复发布条件见[发布准备情况](docs/release-readiness.md)。当前交付的是源码分享准备，不是可安装产品。此 fork 使用独立应用标识和 Windows 浏览器注册名称，不自动迁移官方程序的资料。

## 检查源码

安装 Bun、Node.js 和 Python 后运行：

```sh
bun install --frozen-lockfile
bun test
bun run build
python scripts/test-fetch-browser.py
python vendor/cromma-ui/verify-pika-source.py
python scripts/check-source-privacy.py
```

浏览器下载和打包命令会明确停止。以上检查不启动 Claude、不读取真实账号、不安装应用，也不运行旧浏览器。原生平台检查需要相应编译工具，不能由上述源码检查代替。

## 更新与授权

此 fork 不使用官方整包自动更新。以后需核对新版、保留定制并重新测试，详见[维护说明](UPDATE-WOPILOT.md)。账号、身份导出、登录资料和网络凭据只能由使用者在自己的电脑上配置，不应放进共享仓库或安装包。

保留原作者的 [MIT 许可证](LICENSE)和[第三方归属说明](NOTICE.md)。MIT 仅覆盖有权按此条款授权的原创内容，未知第三方条款未被重新标成 MIT。[上游使用说明](docs/usage.md)用于理解功能，不代表当前分支已具备安装条件。
