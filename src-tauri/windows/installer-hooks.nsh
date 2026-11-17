; [INPUT]: Tauri NSIS 的当前用户安装目录和固定 WoPilot-B 名称空间。
; [OUTPUT]: B 独立启动项及卸载时的本应用注册项清理。
; [POS]: 安装器窄钩子；不执行 SSH，不删除资料，不改其他浏览器关联。
; [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
!macro NSIS_HOOK_POSTINSTALL
  CreateShortCut "$SMPROGRAMS\WoPilot Browser.lnk" "$INSTDIR\requirement-french.exe" "--browser" "$INSTDIR\browser-runtime\icons\browser.ico" 0
!macroend
!macro NSIS_HOOK_POSTUNINSTALL
  Delete "$SMPROGRAMS\WoPilot Browser.lnk"
  DeleteRegKey HKCU "Software\Clients\StartMenuInternet\WoPilot-B"
  DeleteRegKey HKCU "Software\Classes\WoPilot-B.URL"
  DeleteRegKey HKCU "Software\Classes\WoPilot-B.HTML"
  DeleteRegValue HKCU "Software\RegisteredApplications" "WoPilot-B"
!macroend
