Set WS = CreateObject("WScript.Shell")
WS.Popup "重置试用大约数秒时间，请稍后！",2
Set FSO = CreateObject("Scripting.FilesystemObject")
set SA = CreateObject("Shell.Application")
If FSO.FolderExists("C:\\ProgramData\\SafeNet Sentinel") Then
	WS.Popup """删除目录C:\ProgramData\SafeNet Sentinel,请稍候！""",2
	FSO.DeleteFolder "C:\\ProgramData\\SafeNet Sentinel"
Else
	WS.Popup """目录C:\ProgramData\SafeNet Sentinel不存在,待生成，请稍候！""",2
End If
instdemo="""D:\InstallSoftWare\UFT\bin\instdemo.exe"""rem-UFT安装目录下的文件instdemo.exe，这个要根据自己的电脑修改，想一下怎么自动获取
SA.ShellExecute instdemo,"","","runas",1 rem-以管理员方式运行
WScript.sleep 5000
If FSO.FolderExists("C:\\ProgramData\\SafeNet Sentinel") Then
	WS.Popup "重置试用成功！",8
Else
	WS.Popup "重置试用失败，尝试重新执行！",8
End If
Set SA=Nothing
Set FSO=Nothing
Set WS=Nothing