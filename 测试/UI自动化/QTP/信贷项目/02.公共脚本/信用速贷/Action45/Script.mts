'Environment.Value("UserID")="008268"'用户编号，必输，流程中重新赋值
'Environment.Value("Serialno")=""'申请编号，非必输，流程中重新赋值
'Environment.Value("ECIFID")=""'客户核心编号，非必输，流程中重新赋值
'Environment.Value("CustomerName")="熊灿辉"'客户姓名，必输
'Environment.Value("CertID")="430181199005073722"'证件号码，必输
'Environment.Value("EmployType")="自雇人士客户"'客户类型，必输
'Environment.Value("BusinessSum")="200000.00"'贷款金额，必输
'Environment.Value("Term")="24"'贷款期限，必输
'Environment.Value("BusinessType")="南粤e贷1号（经营）"'贷款品种，必输
'Environment.Value("MarketingProgram")="普通方案"'营销方案，必输
'Environment.Value("Account")="6235955040000001112"'账号，必输
'Environment.Value("CellphoneNumber")="13636363636"'手机号码，必输
'Environment.Value("RepaymentType")="等额本息"'还款方式，必输
t=timer
Print("新增面签，开始时点："&time)
With Browser("面签处理管理").Page("面签处理管理")
	.WebElement("面签处理").Click
	.Frame("left").WebElement("新增面签").Click
	.Frame("right").WebElement("新增预约").Click
End With
With Browser("面签处理管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	With .Frame("myiframe0")
		.WebEdit("客户姓名").Click
		.WebEdit("客户姓名").Set Environment("CustomerName")
		.WebEdit("身份证号码").Click
		.WebEdit("身份证号码").Set Environment("CertID")
		.WebList("雇佣类型").Click
		.WebList("雇佣类型").Select Environment("EmployType")
		.WebButton("贷款品种").Click
		With Browser("面签处理管理").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
			.Frame("left").WebElement("innertext:="&Environment("BusinessType"),"html tag:=A").Click
			.WebButton("确认").Click
		End With
		.WebList("营销专案").Click
		.WebList("营销专案").Select Environment("MarketingProgram")
		.WebEdit("申请金额").Click
		.WebEdit("申请金额").Set Environment.Value("BusinessSum")
		.WebEdit("贷款期限").Click
		.WebEdit("贷款期限").Set Environment.Value("Term")
		.WebButton("客户经理").Click
		With Browser("面签处理管理").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
			.Frame("myiframe0").WebEdit("客户经理").Click
			.WebButton("确认").Click
		End With			
'		.WebList("城市").Click
'		.WebList("城市").Select
	End With
	.Frame("ObjectList").WebElement("保存").Click
	Environment("Serialno")=.Frame("myiframe0").WebEdit("申请编号").GetROProperty("value")
	Print("获取申请编号："&Environment("Serialno"))
	Browser("面签处理管理").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").Click
	Browser("面签处理管理").Window("信贷风险管理系统V7").Dialog("Windows Internet Explorer").WinButton("确定").Click
End With
Print("新增面签完成，用时："&timer-t&"s；结束时点："&time&"。")