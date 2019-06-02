'Environment.Value("UserID")="008268"'用户编号，必输，流程中重新赋值
'Environment.Value("Serialno")=""'申请编号，非必输，流程中重新赋值
'Environment.Value("ECIFID")=""'客户核心编号，非必输，流程中重新赋值
'Environment.Value("CustomerName")="徐四零"'客户姓名，必输
'Environment.Value("CertID")="110100199101010403"'证件号码，必输
'Environment.Value("EmployType")="标准受薪客户"'客户类型，必输
'Environment.Value("BusinessSum")="200000.00"'贷款金额，必输
'Environment.Value("Term")="24"'贷款期限，必输
'Environment.Value("BusinessType")="消费类标准工薪贷"'贷款品种，必输
'Environment.Value("MarketingProgram")="随心e贷专案放额度"'营销方案，必输
'Environment.Value("Account")="6235957400006260666"'账号，必输
'Environment.Value("CellphoneNumber")="18770000001"'手机号码，必输
'Environment.Value("RepaymentType")="等额本息"'还款方式，必输
'Environment.Value("已评分数据")=""
Print("面签处理信息填写，时点："&time)
t=timer
With Browser("面签处理管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
	.WebList("营销专属方案").Click
	.WebList("营销专属方案").Select Environment.Value("MarketingProgram")
	Select Case Environment.Value("EmployType")
		Case "优良职业客户"
			'优良职业客户的时候输入
			.WebButton("优良单位名称").Click
			With Browser("面签处理管理").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
				.Frame("ObjectList").WebCheckBox("优良单位(查询)").Set "ON"
				.Frame("ObjectList").WebButton("查询").Click
				.Frame("myiframe0").WebEdit("优良单位").Click
				.WebButton("确认").Click
			End With
		Case else
	End Select	
End With
Browser("面签处理管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("TabContentFrameArr0").WebElement("保存").Click:Wait 1
Print("面签处理信息填写完成，用时："&timer-t&"s；时点："&time&"。")