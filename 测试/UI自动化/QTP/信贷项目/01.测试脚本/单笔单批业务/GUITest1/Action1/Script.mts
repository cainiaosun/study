Set WS=CreateObject("WScript.Shell")
WS.Popup "重置试用大约用时15s，请耐心等候！",3
WScript.Sleep 2000
Set FSO=CreateObject("Scripting.FilesystemObject")
If FSO.FolderExists("C:\\ProgramData\\SafeNet Sentinel") Then
	'WS.Popup """删除目录C:\ProgramData\SafeNet Sentinel,请稍候！""",3
	WScript.Sleep 2000
	FSO.DeleteFolder "C:\\ProgramData\\SafeNet Sentinel"
Else
	'WS.Popup """目录C:\ProgramData\SafeNet Sentinel不存在,待生成，请稍候！""",3
End If
'WS.Popup """执行文件C:\Program Files\HP\Unified Functional Testing\bin\instdemo.exe,请稍候！""",2
WScript.Sleep 2000
WS.Run """C:\Program Files\HP\Unified Functional Testing\bin\instdemo.exe"""
'WS.Popup """检查目录C:\ProgramData\SafeNet Sentinel是否生成,请稍候！""",3
WScript.Sleep 3000
If FSO.FolderExists("C:\\ProgramData\\SafeNet Sentinel") Then
	WS.Popup "重置试用成功！",3
Else
	WS.Popup "重置试用失败！",3
End If
Set FSO=Nothing
Set WS=Nothing