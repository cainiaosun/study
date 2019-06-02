rem-调试数据
'	Environment("EmployType")="自雇人士客户"
'	Environment("CustomerName")="TESTA0000931393"
'	Environment("CertID")="440823199102250619"
'	Environment("CellphoneNumber")= "13499880350"
'	Environment("ECIFID")="A0000931393"
'	Environment("BusinessSum")="100000.00"
'	Environment("Term")="36"
'	Environment("RepaymentType")="等额本息"'还款方式
'	Environment("MarketingProgram")="普通方案"'营销方案

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
	Element(First_DetailFrame_0,"关键信息复核","WebElement","html tag","SPAN",,,0).Click
	Call Dialog_Handle(First_Window,"确定",5)
	rem-这里等待校验按钮对象很奇怪，不支持各种方法，弃用
	Wait 3
	First_Page.Sync
	set biaodan=First_myiframe0_1.WebTable("index:=0")
	R=biaodan.RowCount()
	For i = 1 To R Step 1
		C=biaodan.ColumnCount(i)
		For j = 1 To C Step 1
			MV=biaodan.GetCellData(i,j)
			Select Case MV
				Case "客户类型  * "
					'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
					biaodan.ChildItem(i,j+1,"WebList",0).Click
					biaodan.ChildItem(i,j+1,"WebList",0).Select Environment("EmployType")
				Case "客户名称  * "
					'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
					biaodan.ChildItem(i,j+1,"WebEdit",0).Click
					biaodan.ChildItem(i,j+1,"WebEdit",0).Set Environment.Value("CustomerName")
				Case "客户身份证号  * "
					'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
					biaodan.ChildItem(i,j+1,"WebEdit",0).Click
					biaodan.ChildItem(i,j+1,"WebEdit",0).Set Environment.Value("CertID")
				Case "手机  * "
					'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
					biaodan.ChildItem(i,j+1,"WebEdit",0).Click
					biaodan.ChildItem(i,j+1,"WebEdit",0).Set Environment.Value("CellphoneNumber")
				Case "核心客户编号  * "
					'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
					biaodan.ChildItem(i,j+1,"WebEdit",0).Click
					biaodan.ChildItem(i,j+1,"WebEdit",0).Set Environment("ECIFID")
				Case "贷款金额  * "
					'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
					biaodan.ChildItem(i,j+1,"WebEdit",0).Click
					biaodan.ChildItem(i,j+1,"WebEdit",0).Set Environment.Value("BusinessSum")
				Case "贷款期限  * "
					'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
					biaodan.ChildItem(i,j+1,"WebList",0).Click
					biaodan.ChildItem(i,j+1,"WebList",0).Select Environment.Value("Term")
				Case "还款类型  * "
					'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
					biaodan.ChildItem(i,j+1,"WebList",0).Click
					biaodan.ChildItem(i,j+1,"WebList",0).Select Environment.Value("RepaymentType")
				Case "营销方案  * "
					'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
					biaodan.ChildItem(i,j+1,"WebList",0).Click
					biaodan.ChildItem(i,j+1,"WebList",0).Select Environment.Value("MarketingProgram")
			End Select	
		Next
	Next
'''	Element_Relation(First_myiframe0_1,"支付方式","WebList",1,0,0).Select                                               "自主支付" 
'''	Element_Relation(First_myiframe0_1,"还款账户","WebEdit",1,0,0).Set                                                   "123213" 
'''	Element_Relation(First_myiframe0_1,"还款账户","WebEdit",1,0,0).Set                                                   "123213" 
'''	Element_Relation(First_myiframe0_1,"还款账户","WebEdit",1,0,0).Set                                                   "123213" 
'''	Element_Relation(First_myiframe0_1,"还款账户","WebEdit",1,0,0).Set                                                   "123213" 
'''	Element_Relation(First_myiframe0_1,"支付方式","WebList",1,0,0).Select                                               "自主支付" 
'''	Element_Relation(First_myiframe0_1,"支付方式","WebList",1,0,0).Select                                               "自主支付" 
'''	Element_Relation(First_myiframe0_1,"支付方式","WebList",1,0,0).Select                                               "自主支付" 
'''	Element_Relation(First_myiframe0_1,"支付方式","WebList",1,0,0).Select                                               "自主支付" 
	Element(TabContentFrame,"校验","WebElement","html tag","TD",,,3).Click
	Call Dialog_Handle(First_Window,"确定",10)
	First_Window.Close