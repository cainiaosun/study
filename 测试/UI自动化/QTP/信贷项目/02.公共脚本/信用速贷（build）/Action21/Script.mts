rem--调试数据
'	Environment("Serialno")="UPL2019022600000002"

rem-加载共享对象库
path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)

Set Home_Page=Browser("主窗口（浏览器）").Page("主窗口Page页")
	Element(Home_Page,"信用速贷录入","WebElement","html tag","SPAN",,,0).Click

Set Browser_0=Browser("主窗口（浏览器）")
Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")
Set Home_Frame_right=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("right")
Set Home_Frame_myiframe0=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("myiframe0")
Set First_Page=Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")
	Element(Home_Frame_myiframe0,Environment("Serialno"),"WebEdit","html tag","INPUT",,,0).Click
	Element(Home_Frame_right,"提交","WebElement","html tag","TD",,,1).Click
	rem-解决风险预警/探测弹框问题
	For i = 1 To 2 Step 1
		EaxmSinal=First_Window.Exist(5)
		EaxmTitle=left(First_Window.GetROProperty("regexpwndtitle"),4)		
		If EaxmTitle="自动风险" Then			
			text=First_Page.WebTable("index:=1").GetROProperty("text")	
			title=left(First_Window.GetROProperty("regexpwndtitle"),6)			
			Call LogNote(title&"信息："&text)
			Print(title&"信息："&text)			
			If title="自动风险预警" Then
				action="确   定"
			ElseIf title="自动风险探测"Then
				action="关  闭"
				Err.Raise 002,"自定义错误","风险探测不通过！探测信息："&text
			End If
			First_Page.WebButton("name:="&action,"html taag:=INPUT").Click
			Wait(1)
			If action="关  闭" Then:Exit For:End If
		Else:Exit For
		End If
	Next
	Call Dialog_Handle(Browser_0,"确定",10)
	Element(First_Page,"提 交","WebElement","html tag","TD",,,1).Click
	Call Dialog_Handle(First_Window,"确定",10)
	Call Dialog_Handle(First_Window,"确定",10)	