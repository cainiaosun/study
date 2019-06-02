Environment.Value("Term")="24"
Print("风险参数，时点："&time)
t=timer
if Browser("任务提示").Window("信贷风险管理系统V7").Dialog("来自网页的消息").Exist(3) then
	Browser("任务提示").Window("信贷风险管理系统V7").Dialog("来自网页的消息").Close
End if
Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("DetailFrame").WebElement("风险参数").Click
Set Object=Browser("任务提示").Window("信贷风险管理系统V7")
rem‘Call DialogHandle(Object)
If Object.Dialog("micclass:=Dialog").WinButton("text:=确定").Exist(4) Then
	Object.Dialog("micclass:=Dialog").WinButton("text:=确定").Click
End If
'''基本信息
'R=0
'Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").RefreshObject
print ("获取tableRows："&Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebTable("贷款方案编码").RowCount)
set biaodan=Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebTable("贷款方案编码")
print ("表单对象是否存在："&biaodan.Exist)
print biaodan.RowCount
print ("table数值："&biaodan.GetROProperty("rows"))
print ("表单行列数值：")&biaodan.RowCount()
R=biaodan.RowCount()
print ("R值:"&R)
print ("RowCount信息:"&biaodan.RowCount())
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
				biaodan.ChildItem(i,j+1,"WebEdit",0).Set "1.00"
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
rem’风险参数
set biaodan=Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebTable("贷款期限  *")
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
'''风险计算
Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("TabContentFrame").WebElement("传统风险计算").Click:Wait 1
'value=Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("核定贷款金额").GetROProperty("value")
'If value="" or value="0.00"  Then
'		msgbox("核定金额评定不通过，请手工修改测算后，点击确定继续执行！")
'End If
set biaodan=Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebTable("贷款期限  *")
R=biaodan.RowCount()
For i = 1 To R Step 1
	If Examine=1 Then
		Exit For 
	End If
	C=biaodan.ColumnCount(i)
	For j = 1 To C Step 1
		MV=biaodan.GetCellData(i,j)
		Select Case MV
			rem'这个Case是在评分通过后出现的
			Case "核定贷款金额"
				biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
				value=biaodan.ChildItem(i,j+1,"WebEdit",0).GetRoproperty("value")
				Print("核定金额是："&Cstr(value))
				If value="" or value="0.00"  Then
					msgbox("核定金额评定不通过，请手工修改测算后，点击确定继续执行！")
				End If
				Examine=1
				Exit For
		End Select	
	Next
Next
Print("风险参数完成，用时："&timer-t&"s；时点："&time&"。")