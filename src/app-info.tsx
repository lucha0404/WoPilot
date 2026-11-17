/**
 * [INPUT]: 本机应用版本、共享 YAML 与 Cromma UI。
 * [OUTPUT]: WoPilot 本机定制版的只读版本信息；读取失败明确显示。
 * [POS]: 侧栏版本说明，不联网检查、下载安装或重启。
 * [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
 */
import {useEffect,useState} from 'react';
import {getVersion} from '@tauri-apps/api/app';
import {Button,NavButton} from 'cromma-ui';
import {FolderDefault} from 'cromma-ui/pika';
import {AppDialog} from './dialog';
import {useI18n} from './i18n';
export function AppInfo(){
  const {t}=useI18n();
  const [open,setOpen]=useState(false),[version,setVersion]=useState(''),[error,setError]=useState('');
  useEffect(()=>{
    let live=true;
    void getVersion().then(value=>{if(live)setVersion(value);}).catch(error=>{if(live)setError(String(error));});
    return()=>{live=false;};
  },[]);
  return <>
    <NavButton className="workspace-nav app-info-nav" icon={<FolderDefault size={17} aria-hidden="true"/>} onClick={()=>setOpen(true)}>{t('版本信息')}</NavButton>
    {version&&<small className="app-version">v{version}</small>}
    <AppDialog open={open} onOpenChange={setOpen} title={t('WoPilot 本机定制版')} width={460} footer={<Button variant="ghost" onClick={()=>setOpen(false)}>{t('关闭弹窗')}</Button>}>
      <dl className="app-info-version"><div><dt>{t('当前版本')}</dt><dd>{version||'—'}</dd></div></dl>
      <p className="system-feedback">{t('此版本由本机定制构建，不检查或安装官方更新。更新需手动安装新的定制版本。')}</p>
      {error&&<p role="alert" className="system-feedback error">{t('无法读取版本：{error}',{error})}</p>}
    </AppDialog>
  </>;
}
