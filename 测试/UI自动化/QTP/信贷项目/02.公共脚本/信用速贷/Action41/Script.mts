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
Print("发起面签，时点："&time)
t=timer
With Browser("信用评估查询").Page("信用评估查询")
	.WebElement("信用评估查询").Click
	.Frame("left").WebElement("已评分任务").Click
	With .Frame("right")
		.Link("查询条件").Click
		.WebEdit("客户姓名").Set Environment("CustomerName")
		.WebButton("查询").Click
	End With
	rem'如果Environment("已评分数据")未空，那么按照默认的对象选择第一条评分数据，否则，这里取信用评估用随机数生成的手机号码作为评分唯一性判断，选择到对应的评分记录。当然后面客户信息填写的时候会按照实际的手机号码进行更新
	If Environment("已评分数据")="" Then
		.Frame("myiframe0").WebEdit("已评分数据").Click
	else
		.Frame("myiframe0").WebEdit("value:="&Environment("已评分数据"),"html tag:=INPUT").Click
	End If	
	.Frame("right").WebElement("发起面签").Click
	If Browser("信用评估查询").Dialog("来自网页的消息").Exist(2) Then
		msgbox("请检查是否存在在途申请或其他！点击“确认”继续！")
	End If	
End With
'面签基本信息填写及保存
With Browser("信用评估查询").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	With .Frame("myiframe0")
		If .WebEdit("贷款品种").GetROProperty("value")="" Then'rem在信用评估，评估结果业务品种还未给出前，为空时填写业务品种
			Print("信用评估结果：“业务品种”为空，请关注！")
			.WebButton("贷款品种").Click
			With Browser("信用评估查询").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
				.Frame("left").WebElement("innertext:="&Environment("BusinessType"),"html tag:=A").Click
				.WebButton("确认").Click
			End With
		End If
		.WebButton("客户经理").Click	
			With Browser("信用评估查询").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
				With .Frame("myiframe0")
					.WebEdit("用户ID").Click
					Organ=.WebEdit("用户所属机构").GetROProperty("value")
				End With
				.WebButton("确认").Click
			End With
		If Browser("信用评估查询").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").Exist(1) Then'rem在城市不匹配时会有弹框，关闭弹框，重新填写城市
			Browser("信用评估查询").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").Click
		End If
		.WebList("城市").Click
		.WebList("城市").Select "广州"'Right(Left(Organ,5),2)
	End With
	.Frame("ObjectList").WebElement("保存").Click:wait 2
	Serialno=.Frame("myiframe0").WebEdit("申请编号").GetROProperty("value")
	If Serialno="" Then'rem如果获取到的申请编号是空的，可能是未生成成功，可以手工操作流程，填写赋值申请编号
		Serialno=inputbox("申请编号未获取成功，请手工赋值：")
	End If
	Print("获取申请编号："&Serialno)
	Environment.Value("Serialno")=Serialno
	Browser("信用评估查询").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").Click:wait 0.5
	Browser("信用评估查询").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").Click:wait 0.5
	Print("发起面签成功！")
End With
Print("发起面签完成，用时："&timer-t&"s；完成时点："&time&"。")