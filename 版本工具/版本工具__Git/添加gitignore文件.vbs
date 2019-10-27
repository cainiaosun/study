rem-遍历文件夹：
rem-判断文件夹下是否存在文件：如果不存在就常见一个.ignore

path=inputbox("目标目录：","添加gitignore文件","请输入正确的目标目录路径，以免错误添加文件！")

Function FolderTree(path)
	set Fso=CreateObject("Scripting.FileSystemObject")	
	If Fso.folderExists((path))=False Then
		msgbox("提示：目标目录不存在，请检查输入是否正确！")
		Exit Function
	End If
	set Folder=fso.GetFolder(Path)
	set SubFolders=Folder.SubFolders
	For Each SubFolder in SubFolders
		ignorefile=SubFolder.path&"/.gitignore"
		If Fso.fileExists(ignorefile)=False Then
			Fso.CreateTextFile(ignorefile)
		End If
		FolderTree(SubFolder.path)rem-自身函数递归
	Next
	FolderTree=True
End Function

If path<>"" Then
	If msgbox(path,1,"确认目标目录是否正确")=1 Then
		If FolderTree(path)=True Then
			msgbox(path&"：子目下添加.gitignore文件成功!")
		End If	
	End If
End If
