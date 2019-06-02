rem-调试数据
'	Environment("Serialno")="UPL2018122800000002"

rem-加载共享对象库
path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)

Set Home_Page=Browser("主窗口（浏览器）").Page("主窗口Page页")
Set Browser_0=Browser("主窗口（浏览器）")
Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")
Set Home_Frame_Left=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("left")
Set Home_Frame_Right=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("right")
Set Home_Frame_myiframe0=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("myiframe0")
Set First_Page=Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")
Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")rem-录入弹窗
	Element(Home_Page,"信用速贷征信调查","WebElement","html tag","SPAN",,,0).Click
	Element(Home_Frame_Right,"查询条件","Link","html tag","A",,,1).Click
	Element_Relation_1(Home_Frame_Right,"申请编号","WebEdit",0,0).Set                           Environment("Serialno")
	Element(Home_Frame_Right,"查询","WebButton","html tag","INPUT",,,1).Click	
	Element(Home_Frame_myiframe0,Environment("Serialno"),"WebEdit","html tag","INPUT",,,0).Click
	Element(Home_Frame_right,"处理","WebElement","html tag","TD",,,1).Click
	Call Dialog_Handle(First_Window,"是\(&Y\)",20)