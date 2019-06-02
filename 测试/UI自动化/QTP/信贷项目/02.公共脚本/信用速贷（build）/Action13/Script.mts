'Environment("EmployType")="自雇人士客户" 

rem-加载共享对象库
path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)
With Browser("主窗口（浏览器）").Window("一级窗口")
	Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")
	Set First_Page=.Page("一级窗口Page页")
	Set First_myiframe0_0=.Page("一级窗口Page页").Frame("myiframe0_0")
	Set First_myiframe0_1=.Page("一级窗口Page页").Frame("myiframe0_1")
	Set First_ObjectList=.Page("一级窗口Page页").Frame("ObjectList")
	Set First_TabContentFrameArr_0=.Page("一级窗口Page页").Frame("TabContentFrameArr_0")
	Set First_TabContentFrameArr_1=.Page("一级窗口Page页").Frame("TabContentFrameArr_1")
	Set First_TabContentFrameArr_2=.Page("一级窗口Page页").Frame("TabContentFrameArr_2")
	Set Second_Window=.Window("二级窗口")
	Set Second_Page=.Window("二级窗口").Page("二级窗口Page页")
End With
	If  Environment("EmployType")="优良职业客户" Then
		Element_Relation(First_myiframe0_1,"优良单位名称","WebEdit",1,0,0).Set                           "优良单位"
	End If
	Element(First_TabContentFrameArr_0,"保存","WebElement","html tag","TD",,,3).Click
	Call IsFinish(First_myiframe0_1)
	Element(First_ObjectList,"面签资料审查","WebElement","html tag","SPAN",,,0).Click
	Element(First_TabContentFrameArr_1,"保存","WebElement","html tag","TD",,,1).Click
	Call Dialog_Handle(First_Window,"确定",10)
	Element(First_ObjectList,"面签意见处理","WebElement","html tag","SPAN",,,0).Click
	Call Dialog_Handle(First_Window,"确定",5)
	Element_Relation(First_myiframe0_0,"面签意见","WebList",1,0,0).Select                                      "面签同意"
	Element_Relation(First_myiframe0_0,"意见详情(限2000个汉字)","WebEdit",1,0,0).Set               "同意"
	Element(First_TabContentFrameArr_2,"保存","WebElement","html tag","TD",,,3).Click
	Call IsFinish(First_myiframe0_0)
	Element(First_ObjectList,"提交","WebElement","html tag","TD",,,1).Click
	Element(Second_Page,"提 交","WebElement","html tag","TD",,,1).Click
	Call Dialog_Handle(Second_Window,"确定",10)
	Call Dialog_Handle(Second_Window,"确定",10)
	Call Dialog_Handle(First_Window,"确定",10)