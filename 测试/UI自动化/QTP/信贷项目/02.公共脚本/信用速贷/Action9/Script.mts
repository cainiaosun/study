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
Print("面签意见处理，时点："&time)
t=timer
Browser("面签处理管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("ObjectList").WebElement("面签意见处理").Click
Browser("面签处理管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebList("面签意见").Select "面签同意"
Browser("面签处理管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("意见详情").Set "同意申请"
Browser("面签处理管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("TabContentFrameArr2").WebElement("保存").Click:wait 1
Print("面签意见处理完成，用时："&timer-t&"s；时点："&time&"。")