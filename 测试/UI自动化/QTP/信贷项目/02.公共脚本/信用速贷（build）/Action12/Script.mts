rem-调试数据
'	Environment("Serialno")="UPL2019022100000001"

rem-加载共享对象库
path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)
rem--面签任务获取和处理
Set Home_Page=Browser("主窗口（浏览器）").Page("主窗口Page页")
	Element(Home_Page,"面签处理","WebElement","html tag","SPAN",,,0).Click

Set Home_Frame_Left=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("left")
	Element(Home_Page,"待获取面签","WebElement","html tag","A",,,0).Click
	
Set Home_Frame_Right=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("right")
Set Home_Frame_myiframe0=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("myiframe0")
	Element(Home_Frame_Right,"查询条件","Link","html tag","A",,,1).Click
	Element_Relation_1(Home_Frame_Right,"申请编号","WebEdit",0,0).Set                              Environment("Serialno")
	Element(Home_Frame_Right,"查询","WebButton","html tag","INPUT",,,1).Click
	Element(Home_Frame_myiframe0,Environment("Serialno"),"WebEdit","html tag","INPUT",,,0).Click
	Element(Home_Frame_Right,"获取面签","WebElement","html tag","TD",,,3).Click