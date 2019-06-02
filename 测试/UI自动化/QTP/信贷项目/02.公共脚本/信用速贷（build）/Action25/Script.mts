rem-加载共享对象库
path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)

With Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")
	Set Browser_0=Browser("主窗口（浏览器）")
	Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")rem-录入弹窗
	Set First_Page=Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")rem-录入Page页面
	Set Second_Page=Browser("主窗口（浏览器）").Window("一级窗口").Window("二级窗口").Page("二级窗口Page页")rem-弹出窗口Page页面
	Set First_myiframe0_0=.Frame("myiframe0_0")rem-面签信息填写Frame页面
	Set First_right=.Frame("right_0")rem-面签信息保存按钮所在Frame页面
	Set First_myiframe0_1=.Frame("myiframe0_1")rem-贷款相关信息填写Frame页面
	Set First_DetailFrame_0=.Frame("DetailFrame_0")rem-各个页面切换标签所在页面，如：客户详情、贷款信息
	Set TabContentFrame=.Frame("TabContentFrame")rem-各个页面切换标签所在页面，如：主借款人、其他联系人
	Set First_DetailFrame_1=.Frame("DetailFrame_1")rem-贷款相关信息保存、更新核心客户编号按钮所在Frame页面
	Set First_TabContentFrameArr_2=.Frame("TabContentFrameArr_2")
	Set Second_Window=Browser("主窗口（浏览器）").Window("一级窗口").Window("二级窗口")
End With
	Element(First_right,"审批意见处理","WebElement","html tag","SPAN",,,0).Click
	Call Dialog_Handle(First_Window,"确定",5)
	Element_Relation(First_myiframe0_0,"审批结果","WebList",1,0,0).Select                                      "同意"
	Element_Relation(First_myiframe0_0,"审批意见(限2000个汉字)","WebEdit",1,0,0).Set               "同意"
	Element(First_TabContentFrameArr_2,"保存","WebElement","html tag","TD",,,3).Click	
	Element(First_right,"提交","WebElement","html tag","TD",,,1).Click
	rem-解决风险预警/探测弹框问题
	For i = 1 To 2 Step 1
		EaxmSinal=Second_Window.Exist(5)
		EaxmTitle=left(Second_Window.GetROProperty("regexpwndtitle"),4)		
		If EaxmTitle="自动风险" Then			
			text=Second_Page.WebTable("index:=1").GetROProperty("text")	
			title=left(Second_Window.GetROProperty("regexpwndtitle"),6)			
			Call LogNote(title&"信息："&text)
			Print(title&"信息："&text)			
			If title="自动风险预警" Then
				action="确   定"
			ElseIf title="自动风险探测"Then
				action="关  闭"
				Err.Raise 002,"自定义错误","风险探测不通过！探测信息："&text
			End If
			Second_Page.WebButton("name:="&action,"html taag:=INPUT").Click
			Wait(1)
			If action="关  闭" Then:Exit For:End If
		Else:Exit For
		End If
	Next
	Element(Second_Page,"提 交","WebElement","html tag","TD",,,1).Click
	Call Dialog_Handle(Second_Window,"确定",10)
	Call Dialog_Handle(Second_Window,"确定",10)