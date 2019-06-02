rem-调试数据
'	Environment("Serialno")="UPL2018122800000002"
'	Environment("Grained")="征信调查岗"
'	Environment("BusinessType")="经营类标准信用速贷"
'	Environment("UserID")=""


rem-加载共享对象库
path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)

 rem-1、使用总行用户登录
'Call Login("008025")
rem-2、查询对应产品的岗位处理人
Set Home_Page=Browser("主窗口（浏览器）").Page("主窗口Page页")
Set Browser_0=Browser("主窗口（浏览器）")
Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")
Set Home_Frame_Left=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("left")
Set Home_Frame_Right=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("right")
Set Home_Frame_myiframe0=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("myiframe0")
Set First_Page=Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")
	Element(Home_Page,"审批授权模型维度管理","WebElement","html tag","SPAN",,,0).Click
	Element(Home_Frame_Left,"审批授权模型维度管理","WebElement","html tag","A",,,1).Click
	Element(Home_Frame_Right,"查询条件","Link","html tag","A",,,1).Click
	Element_Relation_1(Home_Frame_Right,"业务品种","WebList",0,1).Select                      Environment("BusinessType")
	Element(Home_Frame_Right,"查询","WebButton","html tag","INPUT",,,1).Click	
	Set biaodan=Home_Frame_myiframe0.WebTable("index:=0")
		'Environment("grained")="征信调查岗"
		Row=biaodan.RowCount()
		Column=biaodan.ColumnCount(3)
		For i = 3 To row Step 1
			For j = 2 To Column Step 1
				If biaodan.ChildItem(i,j,"webedit",0).getroproperty("value")= Environment.Value("Grained")Then
					tuichu="tuichu"
					exit for
				End If
			Next
			If tuichu="tuichu" Then
				Exit for
			End If
		Next
		'print i&j
		str=biaodan.ChildItem(i,j+1,"webedit",0).getroproperty("value")
		'print str
		arr=split (str," ")
		Environment("UserID")=arr(1)
		'print environment("userid")
	rem-3、调整处理人查询的有权处理人
	Element(Home_Page,"信用速贷业务进度查询","WebElement","html tag","SPAN",,,0).Click
	Element(Home_Frame_left,"在办申请业务","WebElement","html tag","A",,,0).Click
	Element(Home_Frame_Right,"查询条件","Link","html tag","A",,,1).Click
	Element_Relation_1(Home_Frame_Right,"申请编号","WebEdit",0,0).Set                           Environment("Serialno")
	Element(Home_Frame_Right,"查询","WebButton","html tag","INPUT",,,1).Click	
	Element(Home_Frame_myiframe0,Environment("Serialno"),"WebEdit","html tag","INPUT",,,0).Click
	Element(Home_Frame_right,"任务调整","WebElement","html tag","TD",,,1).Click
	Call FindSelection(First_Page,Environment("UserID"),"1","0","0","0",Environment("UserID"))
	Print(Dialog_Handle(Browser_0,"确定",20))