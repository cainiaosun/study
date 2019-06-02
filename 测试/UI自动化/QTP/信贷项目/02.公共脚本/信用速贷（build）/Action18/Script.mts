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
	rem-其他联系人
	Element(TabContentFrame,"其他联系人","WebElement","html tag","SPAN",,,0).Click
	Element_Relation(First_myiframe0_1,"密切联系人姓名","WebEdit",1,0,0).Set                                        "密切联系人" 
	Element_Relation(First_myiframe0_1,"密切联系人关系","WebList",1,0,0).Select                                  "配偶"
	Element_Relation(First_myiframe0_1,"密切联系人手机","WebEdit",1,0,0).Set                                        "18779999001" 
	Element_Relation(First_myiframe0_1,"紧急联系人姓名","WebEdit",1,0,0).Set                                        "紧急联系人1" 
	Element_Relation(First_myiframe0_1,"紧急联系人关系","WebList",1,0,0).Select                                  "朋友"
	Element_Relation(First_myiframe0_1,"紧急联系人手机","WebEdit",1,0,0).Set                                        "18779999002" 
	Element_Relation(First_myiframe0_1,"紧急联系人姓名","WebEdit",1,1,0).Set                                        "紧急联系人2" 
	Element_Relation(First_myiframe0_1,"紧急联系人关系","WebList",1,1,0).Select                                  "朋友"
	Element_Relation(First_myiframe0_1,"紧急联系人手机","WebEdit",1,1,0).Set                                        "18779999003" 
	Element_Relation(First_myiframe0_1,"紧急联系人姓名","WebEdit",1,2,0).Set                                        "紧急联系人3" 
	Element_Relation(First_myiframe0_1,"紧急联系人关系","WebList",1,2,0).Select                                  "朋友"
	Element_Relation(First_myiframe0_1,"紧急联系人手机","WebEdit",1,2,0).Set                                        "18779999004" 
	Element(First_DetailFrame_1,"保存","WebElement","html tag","TD",,,1).Click
	Call IsFinish(First_myiframe0_1)