'Environment.Value("UserID")="008268"'用户编号，必输，流程中重新赋值
'Environment.Value("Serialno")="UPL2018082100000018"'申请编号，非必输，流程中重新赋值
'Environment.Value("ECIFID")=""'客户核心编号，非必输，流程中重新赋值
'Environment.Value("CustomerName")="陈八二"'客户姓名，必输
'Environment.Value("CertID")="110100199001019822"'证件号码，必输
'Environment.Value("EmployType")="标准受薪客户"'客户类型，必输
'Environment.Value("BusinessSum")="200000.00"'贷款金额，必输
'Environment.Value("Term")="24"'贷款期限，必输
'Environment.Value("BusinessType")="消费类标准工薪贷"'贷款品种，必输
'Environment.Value("MarketingProgram")="随心e贷专案放额度"'营销方案，必输
'Environment.Value("Account")="6235957400000059841"'账号，必输
'Environment.Value("CellphoneNumber")="13600000982 "'手机号码，必输
'Environment.Value("RepaymentType")="个人所得税专案2.0版"'还款方式，必输
'Environment.Value("已评分数据")=""

Print("面签信息，时点："&time)
t=timer
With Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
	.WebList("业务来源类型").Click
	.WebList("业务来源类型").Select "自来客户"
	rem-目前在南粤e贷中是不需要选择面签类型的，是否有其他情况，遇到后修改
	If Left(Environment("BusinessType"),2)<>"南粤" Then
		.WebList("面签类型").Click
		.WebList("面签类型").Select "处理中心面签"
	End If
	.WebButton("初审人员姓名").Click
	Browser("信用速贷申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息").Frame("myiframe0").WebEdit("选择").Click
	Browser("信用速贷申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息").WebButton("确认").Click
	.WebButton("个贷处理中心").Click
	Browser("信用速贷申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息").Frame("myiframe0").WebEdit("选择").Click
	Browser("信用速贷申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息").WebButton("确认").Click
	Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
	If Browser("信用速贷申请").Window("信贷风险管理系统V7").Dialog("来自网页的消息").Static("对话框").exist(3) Then
		text=Browser("信用速贷申请").Window("信贷风险管理系统V7").Dialog("来自网页的消息").Static("对话框").GetROProperty("text")
		Browser("信用速贷申请").Window("信贷风险管理系统V7").Dialog("来自网页的消息").Close
		If instr(text,"存量客户-续贷")<>0 Then
			.WebList("业务来源类型").Select "存量客户-续贷"
		ElseIf instr(text,"存量客户-再贷-结清90天内(含)")<>0 Then
			.WebList("业务来源类型").Select "存量客户-再贷-结清90天内(含)"
		ElseIf instr(text,"存量客户-再贷-结清90天以上")<>0 Then
			.WebList("业务来源类型").Select "存量客户-再贷-结清90天以上"
		ElseIf instr(text,"交叉销售")<>0 Then
			.WebList("业务来源类型").Select "交叉销售"
		End If
	Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
	End If			
End With
Print("面签信息完成，用时："&timer-t&"s；时点："&time&"。")