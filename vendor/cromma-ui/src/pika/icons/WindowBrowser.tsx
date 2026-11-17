/**
 * [INPUT]: @pikaicons/core-free 0.1.0 的 SidebarMenuIcon 与 PikaIconProps。
 * [OUTPUT]: 沿用 WindowBrowser 接口，以免费窗口/侧栏图形表达浏览器入口。
 * [POS]: 官方免费包 SidebarMenuIcon 的原始路径；来源和摘要见 ../../../PIKA-UPSTREAM.json。
 * [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
 */
// 官方免费包来源和核验方法见 ../../../PIKA-UPSTREAM.json。
import type { PikaIconProps } from '../types';
export default function WindowBrowser({
  size = 24,
  color,
  className,
  ariaLabel,
  ...props
}: PikaIconProps) {
  const iconStyle = {
    color: color || 'currentColor'
  };
  return <svg width={size} height={size} viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className={className} role="img" aria-label={ariaLabel ?? 'window-browser icon'} style={iconStyle} {...props}><path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 8h.01M6 12h.01M6 16h.01M9 3.011C9.577 3 10.236 3 11 3h2c2.8 0 4.2 0 5.27.545a5 5 0 0 1 2.185 2.185C21 6.8 21 8.2 21 11v2c0 2.8 0 4.2-.545 5.27a5 5 0 0 1-2.185 2.185C17.2 21 15.8 21 13 21h-2c-.764 0-1.423 0-2-.011M9 3.011c-1.54.03-2.492.138-3.27.534A5 5 0 0 0 3.545 5.73C3 6.8 3 8.2 3 11v2c0 2.8 0 4.2.545 5.27a5 5 0 0 0 2.185 2.185c.778.396 1.73.505 3.27.534M9 3.011V20.99" fill="none" /></svg>;
}
