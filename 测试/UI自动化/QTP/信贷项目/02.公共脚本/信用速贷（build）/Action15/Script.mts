rem-调试数据
'	Environment("BusinessType")="经营类标准信用速贷"
'	Environment("AccountEntryOrgan")="广州分行速贷业务部（微小）"rem-入账机构

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
End With
	First_Window.Maximize
	rem--录入，面签信息填写保存
	Element_Relation(First_myiframe0_0,"业务来源类型","WebList",1,0,0).Select                                          "自来客户"
	rem-目前在南粤e贷中是不需要选择面签类型的，是否有其他情况，遇到后修改
	If Left(Environment("BusinessType"),2)<>"南粤" Then
		Element_Relation(First_myiframe0_0,"面签类型","WebList",1,0,0).Select                                          "处理中心面签"
	End If
	Element_Relation(First_myiframe0_0,"初审人姓名","WebButton",1,0,0).Click
	Call FindSelection(Second_Page,"1","0","0","0","0",Environment("AccountEntryOrgan"))
	Element_Relation(First_myiframe0_0,"个贷处理中心","WebButton",1,0,1).Click
	Call FindSelection(Second_Page,"1","0","0","0","0",Environment("AccountEntryOrgan"))
	Element(First_right,"保存","WebElement","html tag","TD",,,3).Click
	If Dialog_Handle(First_Window,"",10)<>"" Then
		text=Dialog_Handle(First_Window,"关闭",10)
		If instr(text,"存量客户-续贷")<>0 Then
			Element_Relation(First_myiframe0_0,"业务来源类型","WebList",1,0,0).Select                         "存量客户-续贷"
		ElseIf instr(text,"存量客户-再贷-结清90天内(含)")<>0 Then
			Element_Relation(First_myiframe0_0,"业务来源类型","WebList",1,0,0).Select                         "存量客户-再贷-结清90天内(含)"	
		ElseIf instr(text,"存量客户-再贷-结清90天以上")<>0 Then
			Element_Relation(First_myiframe0_0,"业务来源类型","WebList",1,0,0).Select                         "存量客户-再贷-结清90天以上"
		ElseIf instr(text,"交叉销售")<>0 Then
			Element_Relation(First_myiframe0_0,"业务来源类型","WebList",1,0,0).Select                         "交叉销售"
			Element_Relation(First_myiframe0_0,"推荐机构/推荐人名称","WebEdit",1,0,0).Set                 "推荐人"
			Element_Relation(First_myiframe0_0,"推荐人电话","WebEdit",1,0,0).Set                                    "17566776765"
		End If
		Element(First_right,"保存","WebElement","html tag","TD",,,3).Click
	End If
	Call IsFinish(First_myiframe0_0)