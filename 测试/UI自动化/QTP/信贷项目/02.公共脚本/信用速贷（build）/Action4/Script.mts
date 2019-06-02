rem--调试参数
'	Environment("Serialno")="UPL2019022100000001"

rem-加载共享对象库
path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)
rem--影像扫描
Set Home_Page=Browser("主窗口（浏览器）").Page("主窗口Page页")
	Element(Home_Page,"影像扫描","WebElement","html tag","SPAN",,,0).Click

Set Browser_0=Browser("主窗口（浏览器）")
Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")
Set Home_Frame_TabContentFrame=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("TabContentFrame")
Set Home_Frame_myiframe0=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("myiframe0")
Set First_Page=Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")
	Element(Home_Frame_TabContentFrame,"获取","WebElement","html tag","TD",,,1).Click
	Call FindSelection(First_Page,Environment("Serialno"),"1","0","0","0",Environment("Serialno"))
	Call BrowserClose()
	Element(Home_Frame_myiframe0,Environment("Serialno"),"WebEdit","html tag","INPUT",,,0).Click
	Element(Home_Frame_TabContentFrame,"完成","WebElement","html tag","TD",,,1).Click
	Call Dialog_Handle(Browser_0,"确定",10)
	Call Dialog_Handle(Browser_0,"确定",10)	