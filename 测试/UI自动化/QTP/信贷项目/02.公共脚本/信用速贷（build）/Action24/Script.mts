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
	Element(First_DetailFrame_0,"贷款信息","WebElement","html tag","SPAN",,,0).Click
	First_Page.Sync
	Element_Relation(First_myiframe0_1,"详细用途","WebButton",1,0,0).Click
	If Environment("EmployType")<>"自雇人士客户" and left(Environment("BusinessType"),2)<>"经营" Then
		Purpose="购车-一手车"
	Else:Purpose="经营"
	End If
	Call ItemSelection(Second_Page,"0","0",Purpose)
	Call ItemSelection(Second_Page,"0","0","经营")
	Element_Relation(First_myiframe0_1,"贷款用途交易金额","WebEdit",1,0,0).Set            10000000
	Element(TabContentFrame,"保存","WebElement","html tag","TD",,,3).Click
	Call IsFinish(First_myiframe0_1)