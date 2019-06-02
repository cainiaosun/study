rem-调试数据
'	Environment("CustomerName")="TESTA0000931393"
'	Environment("BusinessType")="经营类标准信用速贷"
'	Environment("评分数据")="13617668691" 
'	Environment("Serialno")=""
	
rem-加载共享对象库
path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)
rem--已评分任务发起面签
Set Browser_0=Browser("主窗口（浏览器）")
Set Home_Page=Browser("主窗口（浏览器）").Page("主窗口Page页")
Set Home_Frame_Left=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("left")
Set Home_Frame_Right=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("right")
Set Home_Frame_myiframe0=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("myiframe0")
	Element(Home_Page,"信用评估查询","WebElement","html tag","SPAN",,,0).Click
	Element(Home_Page,"已评分任务","WebElement","html tag","A",,,0).Click
	Element(Home_Frame_Right,"查询条件","Link","html tag","A",,,1).Click
	Element_Relation_1(Home_Frame_Right,"客户姓名","WebEdit",0,0).Set                           Environment("CustomerName")
	Element(Home_Frame_Right,"查询","WebButton","html tag","INPUT",,,1).Click
	rem'如果Environment("已评分数据")未空，那么按照默认的对象选择第一条评分数据，否则，这里取信用评估用随机数生成的手机号码作为评分唯一性判断，选择到对应的评分记录。当然后面客户信息填写的时候会按照实际的手机号码进行更新
	If Environment("评分数据")="" Then
		Home_Frame_myiframe0.WebEdit("name:=R0F.()*","index:=0").Click
	else
		Element(Home_Frame_myiframe0,Environment("评分数据"),"WebEdit","html tag","INPUT",,,0).Click
	End If	
	Element(Home_Frame_Right,"发起面签","WebElement","html tag","TD",,,1).Click
	If Dialog_Handle(Browser_0,"",3)<>"" Then
		msgbox(Dialog_Handle(Browser_0,"",3)&"，点击“确认”继续！")
	End If	

With Browser("主窗口（浏览器）").Window("一级窗口")
	Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")
	Set First_Page=.Page("一级窗口Page页")
	Set First_myiframe0=.Page("一级窗口Page页").Frame("myiframe0_0")
	Set First_ObjectList=.Page("一级窗口Page页").Frame("ObjectList")
	Set Second_Page=.Window("二级窗口").Page("二级窗口Page页")		
End With	
	If Element_Relation(First_myiframe0,"贷款品种","WebEdit",0,0,0).GetROProperty("value")="" Then
		Print("信用评估结果：“业务品种”为空，请关注！")
		Element_Relation(First_myiframe0,"贷款品种","WebButton",0,0,0).Click
		Call ItemSelection(Second_Page,"0","0",Environment("BusinessType"))		
	End If	
	Element_Relation(First_myiframe0,"客户经理","WebButton",1,0,0).Click
	Call FindSelection(Second_Page,"1","","","0","0","")
	Organ=Element_Relation(First_myiframe0,"机构名称","WebEdit",0,0,0).GetRoproperty("value")
	Element_Relation(First_myiframe0,"城市","WebList",0,0,0).Select    Left(Organ,2)
	
	Element(First_ObjectList,"保存","WebElement","html tag","TD",,,3).Click
	Environment("Serialno")=Element_Relation(First_myiframe0,"申请编号","WebEdit",0,0,0).GetRoproperty("value")
	If Environment("Serialno")="" Then		
		Environment("Serialno")=inputbox("申请编号未获取成功，请手工赋值：")
	End If
	Print(Environment("Serialno"))
	Call Dialog_Handle(First_Window,"确定",10)
	Call Dialog_Handle(First_Window,"确定",10)