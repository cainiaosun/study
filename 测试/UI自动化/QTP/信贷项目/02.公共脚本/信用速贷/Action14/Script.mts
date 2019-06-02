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

Print("基本信息，时点："&time)
t=timer
Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("DetailFrame").WebElement("更新核心客户编号").Click
Browser("信用速贷申请").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").WaitProperty "visible","true",5000
wait 0.3
Browser("信用速贷申请").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").Click
Browser("信用速贷申请").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").Click
wait 1
With Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
	Environment.Value("ECIFID")=.WebEdit("核心客户号").getroproperty("value")
	'print environment("ECIFID")
	.WebList("性别").waitproperty "visible","true",5000
	.WebList("性别").Click
	.WebList("性别").Select "男性"
	.WebList("婚姻状况").Click
	.WebList("婚姻状况").Select "未婚"
	.WebEdit("身份证发证机关所在地").Click
	.WebEdit("身份证发证机关所在地").Set "发证机关地址"
	.WebList("教育程度").Click
	.WebList("教育程度").Select "硕士"
	.WebEdit("手机").Click
	.WebEdit("手机").Set Environment.Value("CellphoneNumber")
	 Environment.Value("CellphoneNumber")=.WebEdit("手机").GetRoproperty("value")
	.WebList("个人类型").Click
	Select Case Environment.Value("EmployType")
		Case "自雇人士客户"
		.WebList("个人类型").Select "小微企业法人代表"
		Case else
		.WebList("个人类型").Select "其它"
	End Select
	'这一部分是"省份、直辖市、自治区"的录入
	With Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
		If .WebEdit("省份、直辖市、自治区").GetROProperty("value")="" Then
			.WebButton("省份、直辖市、自治区").Click
			Set Object=Browser("信用速贷申请").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
			Call AddressSelection(Object)
		End If
	End with
	rem
	.WebEdit("居住地址").Click
	.WebEdit("居住地址").Set "居住地址"
	.WebEdit("住宅邮编").Click
	.WebEdit("住宅邮编").Set "123456"
	.WebList("工作关系是否我行经办分部所在地").Click
	.WebList("工作关系是否我行经办分部所在地").Select "是"
	.WebList("是否农户").Click
	.WebList("是否农户").Select "否"	
End With
Print("基本信息完成，用时："&timer-t&"s；时点："&time&"。")