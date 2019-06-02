Print("综合征信信息，时点："&time)
t=timer
Set biaodan=Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebTable("综合征信信息")
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
				Browser("任务提示").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息").Frame("myiframe0").WebEdit("选择的工作性质").Click
				Browser("任务提示").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息").WebButton("确认").Click:Wait 1
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
Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("DetailFrame").WebElement("保存").Click:Wait 3 
Print("综合征信信息完成，用时："&timer-t&"s；时点："&time&"。")