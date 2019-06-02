'rem调试参数
'Environment.Value("Serialno")=""
'Environment.Value("CustomerName")="44010019800101023X-白金客户 "
'Environment.Value("CertID")="44010019800101023X"
'Environment.Value("EmployType")="自雇人士客户"
'Environment.Value("BusinessSum")="100000"
'Environment.Value("Term")="12"
'Environment.Value("BusinessType")="经营类房贷信用速贷"
t=timer
Browser("信贷风险管理系统V7").Page("信贷风险管理系统V7").WebElement("面签预约").Click
With Browser("信贷风险管理系统V7").Page("面签预约管理")
	.Frame("right").WebElement("新增预约").Click
	With Browser("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
		.WebEdit("客户姓名").Click 
		.WebEdit("客户姓名").Set Environment.Value("CustomerName")
		.WebEdit("身份证号码").Click
		.WebEdit("身份证号码").Set Environment.Value("CertID")
		.WebList("雇佣类型").Click
		.WebList("雇佣类型").Select Environment.Value("EmployType")
		.WebButton("贷款品种").Click
		With Browser("信贷风险管理系统V7").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
			.Frame("left").WebElement("innertext:="&Environment.Value("BusinessType"),"html tag:=A").Click
			.WebButton("确认").Click
		End With
		.WebEdit("申请金额").Click
		.WebEdit("申请金额").Set Environment.Value("BusinessSum")
		.WebEdit("贷款申请期限").Click
		.WebEdit("贷款申请期限").Set Environment.Value("Term")
		.WebButton("客户经理").Click
		With Browser("信贷风险管理系统V7").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
			.Frame("myiframe0").WebEdit("R0F0").Click
			.WebButton("确认").Click
		End With
		wait 2
		OrginName=.WebEdit("机构名称").GetRoProperty("value")
		.WebList("城市").Click
		.WebList("城市").Select Mid(OrginName,4,2)
		.WebButton("初始预约时间").Click
		With Browser("信贷风险管理系统V7").Window("信贷风险管理系统V7").Window("-- 网页对话框").Page("Page")
			.Frame("myiframe0").WebEdit("日期").Click
			.Frame("myiframe0").WebEdit("日期").Set "2099/01/01"
			.Frame("myiframe0").WebList("时间").Click
			.Frame("myiframe0").WebList("时间").Select "16:00"
			.WebElement("确认").Click
		End With
		Browser("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("ObjectList").WebElement("保存").Click
		'.WebEdit("申请编号").Highlight
		Serialno=""
		For i = 1 To 10 Step 1
			Serialno=.WebEdit("申请编号").GetRoProperty("value")
			If Serialno="" Then
				wait 1
			Else
				Exit for
			End If
		Next
		Environment.Value("Serialno")=Serialno
		Browser("信贷风险管理系统V7").Window("信贷风险管理系统V7").Close
	End With
	.Frame("myiframe0").WebEdit("value:="&Serialno,"type:=text").Click
	.Frame("right").WebElement("提交").Click
	With Browser("信贷风险管理系统V7").Window("提交动作选择列表 -- 网页对话框")
		.Page("提交动作选择列表").WebElement("提交").Click
		.Dialog("来自网页的消息").WinButton("确定").Click
		.Dialog("来自网页的消息").WinButton("确定").Click
	End With
End With
Print "申请："&Environment.Value("Serialno")&"，面签预约成功！"
Print "面签预约用时："&timer-t