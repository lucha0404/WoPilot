# WoPilot

[English](README.md)

WoPilot 是基于 [CCBaga v0.2.50](https://github.com/liseami/CCBaga/releases/tag/v0.2.50) 的非官方 Windows 定制版，使用自己的名称、图标和应用资料标识。保留本地账号资料管理、失败恢复、独立浏览器资料、指纹及环境检查，不承诺账号不会被封。

## 下载和安装

打开 [Releases 下载页](https://github.com/lucha0404/WoPilot/releases/latest)，下载 **WoPilot-0.2.50-windows-x86_64-setup.exe**，在 Windows 10 或 11 的 64 位电脑上运行即可。安装包已包含配套浏览器；缺少 Microsoft WebView2 时，会下载微软官方运行环境。

安装包没有 Windows 发布者数字签名，系统可能提示发布者未知。请核对 GitHub 下载来源和随包提供的 SHA-256 文件摘要。安装后使用自己的账号和网络设置，安装包不提供维护者的登录或代理资料。

## 已知问题

- 内置指纹浏览器仍是 **148.0.7778.215**，近期 Chromium 安全补丁的回补覆盖尚未核实，本次没有修复这个上游问题。
- Cromma UI 界面组件的独立再分发条款仍未确认。保留了原作者及第三方声明，项目顶层 MIT 不代表所有第三方组件都已获同样授权。
- 已核对并修复免费 Pika 图标的来源和许可，这不等于解决了 Cromma UI 组件代码自身的授权问题。
- 后续从本 fork 的 Releases 手动下载安装更新；官方整包更新入口已停用，以保留 WoPilot 定制。

各次构建的检查结果和边界见发布说明及[发布状态](docs/release-readiness.md)。此前的只交源码安排已被本次明确授权的手动 Windows 发布替代，上述已知问题继续如实披露；没有自动发布流程。

## 检查源码

```sh
bun install --frozen-lockfile
bun test
bun run build
python scripts/test-fetch-browser.py
python vendor/cromma-ui/verify-pika-source.py
python scripts/check-source-privacy.py
```

安装包由手动触发的 `Build Windows installer` 工作流在可丢弃的 GitHub Windows 环境构建、试装。工作流仅有仓库读取权限，只上传待复核的安装包、摘要和公开构建信息；发布到 Releases 仍是独立的手动步骤。

## 资料与授权

应用标识和 Windows 浏览器注册名称独立于官方版，不自动迁移官方程序的资料。账号、身份导出、登录资料和网络凭据只能由使用者在自己的电脑上配置，不应放进共享仓库或安装包。未导入本机定制的私有提交，新提交使用 GitHub 隐私邮箱。

保留原作者的 [MIT 许可证](LICENSE)和[第三方归属说明](NOTICE.md)，未把未知第三方条款重新标成 MIT。[使用说明](docs/usage.md)介绍功能，[维护说明](UPDATE-WOPILOT.md)说明后续更新方式。
