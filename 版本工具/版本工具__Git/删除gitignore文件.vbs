path=inputbox("Ŀ��Ŀ¼��","ɾ��gitignore�ļ�","��������ȷ��Ŀ��Ŀ¼·�����������ɾ���ļ���")

Function FolderTree(path)
	set Fso=CreateObject("Scripting.FileSystemObject")	
	If Fso.folderExists((path))=False Then
		msgbox("Ŀ��Ŀ¼�����ڣ����������Ƿ���ȷ��")
		Exit Function
	End If
	set Folder=fso.GetFolder(Path)
	set SubFolders=Folder.SubFolders
	For Each SubFolder in SubFolders
		ignorefile=SubFolder.path&"/.gitignore"
		If Fso.fileExists(ignorefile) Then
			Fso.deleteFile(ignorefile)
		End If
		FolderTree(SubFolder.path)rem-�������ݹ�
	Next
	FolderTree=True
End Function

If path<>"" Then
	If msgbox(path,1,"�ٴ�ȷ��Ŀ��Ŀ¼�Ƿ���ȷ!")=1 Then
		If FolderTree(path)=True Then
			msgbox(path&"����Ŀ��ɾ��.gitignore�ļ��ɹ�!")
		End If	
	End If
End If