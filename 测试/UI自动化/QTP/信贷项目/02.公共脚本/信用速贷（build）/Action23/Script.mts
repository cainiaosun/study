rem-加载共享对象库
path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)

With Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")
	Set Browser_0=Browser("主窗口（浏览器）")
	Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")rem-录入弹窗
	Set First_Page=Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")rem-录入Page页面
	Set Second_Page=Browser("主窗口（浏览器）").Window("一级窗口").Window("二级窗口").Page("二级窗口Page页")rem-弹出窗口Page页面
	'Set Second_myiframe0=.Window("二级窗口").Page("二级窗口Page页").Frame("myiframe0")
	Set First_myiframe0_0=.Frame("myiframe0_0")rem-面签信息填写Frame页面
	Set First_right=.Frame("right_0")rem-面签信息保存按钮所在Frame页面
	Set First_myiframe0_1=.Frame("myiframe0_1")rem-贷款相关信息填写Frame页面
	Set First_DetailFrame_0=.Frame("DetailFrame_0")rem-各个页面切换标签所在页面，如：客户详情、贷款信息
	Set TabContentFrame=.Frame("TabContentFrame")rem-各个页面切换标签所在页面，如：主借款人、其他联系人
	Set First_DetailFrame_1=.Frame("DetailFrame_1")rem-贷款相关信息保存、更新核心客户编号按钮所在Frame页面
End With
Set biaodan=First_myiframe0_1.WebTable("index:=4")
R=biaodan.RowCount()
For i = 1 To R Step 1
	C=biaodan.ColumnCount(i)
	For j = 1 To C Step 1
		MV=biaodan.GetCellData(i,j)
		'print i&","&j&":"&MV
		Select Case MV
			Case "单位工商查询结果  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select "正常"
			Case "年龄  * "
				'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
				biaodan.ChildItem(i,j+1,"WebEdit",0).Click
				biaodan.ChildItem(i,j+1,"WebEdit",0).Set "28"
			Case "当地社保  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select "有"
			Case "社保记录状态  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select "当前有"
			Case "公积金记录状态  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select "当前有"
			rem-自雇人士客户字段
			rem--------------------------------------------------------------------------
			Case "工作性质  * "
				'biaodan.ChildItem(i,j+1,"WebButton",0).HighLight
				biaodan.ChildItem(i,j+1,"WebButton",0).Click
				Call FindSelection(Second_Page,"1","0","1","0","0","0")
			rem--------------------------------------------------------------------------
			Case "企业是否有注册  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select "否"
			Case "客户在他行有无未结清的信用/保证贷款  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select "无"
			Case "自雇人士身份  * "
				'biaodan.ChildItem(i,j+1,"WebCheckBox,0).HighLight
				biaodan.ChildItem(i,j+1,"WebCheckBox",0).Click
				biaodan.ChildItem(i,j+1,"WebCheckBox",0).Set "on"	
			rem-寿险等产品字段	
			rem-------------------------------------------------------------------------
			Case "保险公司名称1  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select "中国人寿"
			Case "保单名称1  * "
				'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
				biaodan.ChildItem(i,j+1,"WebEdit",0).Click
				biaodan.ChildItem(i,j+1,"WebEdit",0).Set "我的保单"	
			rem-------------------------------------------------------------------------
		End Select	
	Next
Next
Element(First_DetailFrame_1,"保存","WebElement","html tag","TD",,,1).Click
Call IsFinish(First_myiframe0_1)