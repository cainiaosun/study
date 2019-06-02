rem--调试参数
	Environment.Value("Term")="36"
	Environment("BusinessSum")="200000"

t=timer	
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
	Element(First_DetailFrame_0,"风险参数","WebElement","html tag","SPAN",,,0).Click:Wait(1)
	Call Dialog_Handle(First_Window,"确定",3)
	First_Page.Sync:Wait(1)
	First_DetailFrame_1.RefreshObject
	Element(First_myiframe0_1,"贷款方案编码","WebElement","html tag","TD",,,0).WaitProperty "innertext","贷款方案编码",20
	Set biaodan=First_myiframe0_1.WebTable("index:=1")
		biaodan.highlight
		R=biaodan.RowCount()
		For i = 1 To R Step 1
			C=biaodan.ColumnCount(i)
			For j = 1 To C Step 1
				MV=biaodan.GetCellData(i,j)
				Select Case MV
					Case "户籍、工作关系、房产在我行经办行所在地  * "
						'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
						biaodan.ChildItem(i,j+1,"WebList",0).Click
						biaodan.ChildItem(i,j+1,"WebList",0).Select "是"
					rem-房贷还款额和房贷已还款月份均为房贷信用速贷填写
					rem---------------------------------------------------------------------------
					Case "原房贷月还款额  * "
						'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
						biaodan.ChildItem(i,j+1,"WebEdit",0).Click
						biaodan.ChildItem(i,j+1,"WebEdit",0).Set "20000.00"
					Case "房贷已还款月份  * "
						'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
						biaodan.ChildItem(i,j+1,"WebEdit",0).Click
						biaodan.ChildItem(i,j+1,"WebEdit",0).Set "10"
					rem---------------------------------------------------------------------------
					rem-房贷还款额和房贷已还款月份均为房贷信用速贷填写
					rem---------------------------------------------------------------------------
					Case "原房贷月还款额  * "
						'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
						biaodan.ChildItem(i,j+1,"WebEdit",0).Click
						biaodan.ChildItem(i,j+1,"WebEdit",0).Set "20000.00"
					Case "房贷已还款月份  * "
						'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
						biaodan.ChildItem(i,j+1,"WebEdit",0).Click
						biaodan.ChildItem(i,j+1,"WebEdit",0).Set "10"
					rem--------------------------------------------------------------------------	
					rem-寿险相关字段为寿险产品所需
					rem---------------------------------------------------------------------------
					Case "寿险年缴金额  * "
						'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
						biaodan.ChildItem(i,j+1,"WebEdit",0).Click
						biaodan.ChildItem(i,j+1,"WebEdit",0).Set "50000.00"
					Case "应缴年限  * "
						'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
						biaodan.ChildItem(i,j+1,"WebEdit",0).Click
						biaodan.ChildItem(i,j+1,"WebEdit",0).Set "15"
					Case "实缴年限  * "
						'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
						biaodan.ChildItem(i,j+1,"WebEdit",0).Click
						biaodan.ChildItem(i,j+1,"WebEdit",0).Set "10"
					Case "保单个数  * "
						'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
						biaodan.ChildItem(i,j+1,"WebEdit",0).Click
						biaodan.ChildItem(i,j+1,"WebEdit",0).Set "1"
					Case "保单是否已缴清超过12个月  * "
						'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
						biaodan.ChildItem(i,j+1,"WebList",0).Click
						biaodan.ChildItem(i,j+1,"WebList",0).Select "否"
					rem--------------------------------------------------------------------------	
					Case "我行认定城市级别  * "
						'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
						biaodan.ChildItem(i,j+1,"WebList",0).Click
						biaodan.ChildItem(i,j+1,"WebList",0).Select "一线城市"
					Case "月均银行流水/利润经营"
						'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
						biaodan.ChildItem(i,j+1,"WebEdit",0).Click
						biaodan.ChildItem(i,j+1,"WebEdit",0).Set "1000000.00"
					Case "家庭有本地房产  * "
						'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
						biaodan.ChildItem(i,j+1,"WebList",0).Click
						biaodan.ChildItem(i,j+1,"WebList",0).Select "否"
					Case "信用报告查询次数  * "
						'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
						biaodan.ChildItem(i,j+1,"WebEdit",0).Click
						biaodan.ChildItem(i,j+1,"WebEdit",0).Set "1"
					Case "本人当前是否有未结清房产抵押类贷款  * "
						'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
						biaodan.ChildItem(i,j+1,"WebList",0).Click
						biaodan.ChildItem(i,j+1,"WebList",0).Select "是"
					Case "公积金/社保缴费记录是否需要减额  * "
						'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
						biaodan.ChildItem(i,j+1,"WebList",0).Click
						biaodan.ChildItem(i,j+1,"WebList",0).Select "是"
				End Select	
			Next
		Next
	
	First_Page.Sync
	Set biaodan=First_myiframe0_1.WebTable("index:=2")
		biaodan.highlight
		R=biaodan.RowCount()
			For i = 1 To R Step 1
				C=biaodan.ColumnCount(i)
				For j = 1 To C Step 1
					MV=biaodan.GetCellData(i,j)
					Select Case MV
						Case "贷款期限  * "		
			'				biaodan.ChildItem(i,j+1,"WebList",0).HighLight
							biaodan.ChildItem(i,j+1,"WebList",0).Click
							biaodan.ChildItem(i,j+1,"WebList",0).Select Environment.Value("Term")
						Case "所有信用卡额度  * "
			'				biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
							biaodan.ChildItem(i,j+1,"WebEdit",0).Click
							biaodan.ChildItem(i,j+1,"WebEdit",0).Set "200000"
						Case "所有信用卡已使用额度  * "
							'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
							biaodan.ChildItem(i,j+1,"WebEdit",0).Click
							biaodan.ChildItem(i,j+1,"WebEdit",0).Set "1000.00"
						Case "其他金融机构无抵/质押贷款余额  * "
							'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
							biaodan.ChildItem(i,j+1,"WebEdit",0).Click
							biaodan.ChildItem(i,j+1,"WebEdit",0).Set "10000.00"
						Case "其他金融机构无抵/质押贷款月还款额  * "
							'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
							biaodan.ChildItem(i,j+1,"WebEdit",0).Click
							biaodan.ChildItem(i,j+1,"WebEdit",0).Set "1000.00"
						Case "其他贷款月还款额(含抵/质押贷款)  * "			
							'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
							biaodan.ChildItem(i,j+1,"WebEdit",0).Click
							biaodan.ChildItem(i,j+1,"WebEdit",0).Set "1000.00"
						rem‘非标准工薪贷的部分
						
					End Select	
				Next
			Next
		Element(TabContentFrame,"评分模型计算","WebElement","html tag","TD",,,1).Click
		Call Dialog_Handle(First_Window,"确定",60)
		Call IsFinish(First_myiframe0_1)
		Element_Relation(First_myiframe0_1,"核定贷款金额","WebEdit",0,0,0).Highlight
		ConfirmSum=Element_Relation(First_myiframe0_1,"核定贷款金额","WebEdit",0,0,0).GetRoproperty("value")
		Print("核定贷款金额："&ConfirmSum)
		If Clng(ConfirmSum)<Clng(Environment("BusinessSum")) Then
			LogNote("核定贷款金额"&ConfirmSum&"小于申请金额"&Environment("BusinessSum")&"，需要手工评定才能通过！")
			Call PopBox("核定贷款金额低于申请金额，请暂停执行，手工评定通过后点击确定继续执行！",360)
		End If	
print("风险参数评分用时："&timer-t)		