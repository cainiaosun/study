Environment.Value("UserID")="008268"'用户编号，必输，流程中重新赋值
Environment.Value("Serialno")=""'申请编号，非必输，流程中重新赋值
Environment.Value("ECIFID")=""'客户核心编号，非必输，流程中重新赋值
Environment.Value("CustomerName")="李五"'客户姓名，必输
Environment.Value("CertID")="11010019900101305X"'证件号码，必输
Environment.Value("EmployType")="标准受薪客户"'客户类型，必输
Environment.Value("BusinessSum")="200000.00"'贷款金额，必输
Environment.Value("Term")="36"'贷款期限，必输
Environment.Value("BusinessType")="消费类标准工薪贷"'贷款品种，必输
Environment.Value("MarketingProgram")="随心e贷"'营销方案，必输
Environment.Value("Account")="6235957400000053075"'账号，必输
Environment.Value("CellphoneNumber")="17688300305"'手机号码，必输
Environment.Value("RepaymentType")="不规则还款"'还款方式，必输
Environment.Value("已评分数据")=""

Print("开始信用评估，评估时点："&time)
t=timer
With Browser("信贷风险管理系统V7")
	.Page("信贷风险管理系统V7").WebElement("信用评估查询").Click
	.Page("信用评估查询").Frame("right").WebElement("新增").Click
	With .Window("信用评分详情 -- 网页对话框").Page("信用评分详情")
		With .Frame("myiframe0")
			.WebEdit("客户名称").Click
			.WebEdit("客户名称").Set Environment("CustomerName")
			.WebEdit("身份证号码").Click
			.WebEdit("身份证号码").Set Environment("CertID")
			.WebList("客户性质").Click
			.WebList("客户性质").Select Environment("EmployType")
			rem'使用一个随机数产生的手机号码，作为下一步已评分任务的唯一性判断
			Environment.Value("已评分数据")="136"&Cstr(RandomNumber(10000000,99999999))
			.WebEdit("手机号码").Click
			.WebEdit("手机号码").Set Environment("已评分数据")
			.WebList("婚姻状态").Click
			.WebList("婚姻状态").Select "未婚"
			.WebEdit("贷款金额").Click
			.WebEdit("贷款金额").Set Environment("BusinessSum")
			.WebList("期限").Click
			.WebList("期限").Select Environment("Term")
			.WebList("户口所在地").Click
			.WebList("户口所在地").Select "本地"
			.WebList("家庭是否有本地房产").Click
			.WebList("家庭是否有本地房产").Select "是"
			If Environment("EmployType")<>"自雇人士客户" Then
				.WebList("职业类型").Click
				.WebList("职业类型").Select "高新技术"	
			End If
			.WebEdit("所得税缴费基数").Click
			.WebEdit("所得税缴费基数").Set ""
			.WebEdit("月均银行流水/利润经营").Click
			.WebEdit("月均银行流水/利润经营").Set ""
			.WebEdit("住房公积金缴费基数").Click
			.WebEdit("住房公积金缴费基数").Set ""
			.WebEdit("社保缴费基数").Click
			.WebEdit("社保缴费基数").Set ""
			.WebEdit("寿险年缴金额").Click
			.WebEdit("寿险年缴金额").Set ""
			If .WebList("职称级别").GetROProperty("disabled")=0 Then
				.WebList("职称级别").Click
				.WebList("职称级别").Select ""
			End If
			If .WebList("公务员级别").GetROProperty("disabled")=0 Then
				.WebList("公务员级别").Click
				.WebList("公务员级别").Select ""
			End If	
			.WebList("自然村人口数量").Click
			.WebList("自然村人口数量").Select ""
			.WebList("入账机构").Click 
			.WebList("入账机构").Select "广州分行速贷业务部（微小）"
			.WebList("城市").Click
			.WebList("城市").Select "广州"
			.WebList("业务品种").Click
			.WebList("业务品种").Select Environment("BusinessType")
			.WebList("营销专属方案").Click
			.WebList("营销专属方案").Select Environment("MarketingProgram")
			.WebList("还款方式").Click
			.WebList("还款方式").Select Environment("RepaymentType")
			.WebList("教育程度").Click
			.WebList("教育程度").Select "硕士"
		End With
		.WebElement("保存").Click
		.WebElement("信用评估").Click
	End With
End With
With Browser("信贷风险管理系统V7").Window("信用评分详情 -- 网页对话框")
	If .Dialog("来自网页的消息").Exist(3) Then
		text=.Dialog("来自网页的消息").Static("提示").GetROProperty("text")
		If left(text,5)="没有该客户" Then
		.Dialog("来自网页的消息").Close:wait 1
		End If
	End If
	If .Dialog("来自网页的消息").Exist(5)  Then
		text=.Dialog("来自网页的消息").Static("提示").GetROProperty("text")
		If text="信用评估成功！并行处理结果:成功" Then
			print("信用评估成功！")
			.Dialog("来自网页的消息").Close:wait 2
		Else
			print("信用评估失败，请检查！")
			.Dialog("来自网页的消息").Close:wait 2
		End If
	End If
End With
print("信用评估完成，用时："&timer-t&"s；完成时点："&time&"。")