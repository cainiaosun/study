Set WS = CreateObject("WScript.Shell")
WS.Popup "�������ô�Լ����ʱ�䣬���Ժ�",2
Set FSO = CreateObject("Scripting.FilesystemObject")
set SA = CreateObject("Shell.Application")
If FSO.FolderExists("C:\\ProgramData\\SafeNet Sentinel") Then
	WS.Popup """ɾ��Ŀ¼C:\ProgramData\SafeNet Sentinel,���Ժ�""",2
	FSO.DeleteFolder "C:\\ProgramData\\SafeNet Sentinel"
Else
	WS.Popup """Ŀ¼C:\ProgramData\SafeNet Sentinel������,�����ɣ����Ժ�""",2
End If
instdemo="""D:\InstallSoftWare\UFT\bin\instdemo.exe"""rem-UFT��װĿ¼�µ��ļ�instdemo.exe�����Ҫ�����Լ��ĵ����޸ģ���һ����ô�Զ���ȡ
SA.ShellExecute instdemo,"","","runas",1 rem-�Թ���Ա��ʽ����
WScript.sleep 5000
If FSO.FolderExists("C:\\ProgramData\\SafeNet Sentinel") Then
	WS.Popup "�������óɹ���",8
Else
	WS.Popup "��������ʧ�ܣ���������ִ�У�",8
End If
Set SA=Nothing
Set FSO=Nothing
Set WS=Nothing