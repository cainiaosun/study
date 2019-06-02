'Environment.Value("Account")="6231288300000331878"
'Environment.Value("CustomerName")="钱一百"
'Environment.Value("EmployType")="自雇人士客户"
Print("贷款信息，时点："&time)
t=timer
With Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	.Frame("DetailFrame").WebElement("贷款信息").Click
	''''''''''贷款基本信息
	.Frame("myiframe0").WebButton("贷款用途").waitproperty "visible","true",5000
	.Frame("myiframe0").WebButton("贷款用途").Click
	Browser("信用速贷申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息").Frame("left").WebElement("html id:=text1","html tag:=A").Click
	Browser("信用速贷申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息").WebButton("确认").Click
	.Frame("myiframe0").WebList("支付方式").Click
	.Frame("myiframe0").WebList("支付方式").Select "自主支付"
	.Frame("myiframe0").WebList("是否签约信用速贷存抵贷").Click
	.Frame("myiframe0").WebList("是否签约信用速贷存抵贷").Select "否"
	If Environment.Value("EmployType")="自雇人士客户" Then
		.Frame("myiframe0").WebButton("行业投向").Click
		Set Object=Browser("信用速贷申请").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
		Call IndustrySelection(Object)
	End If	
	.Frame("myiframe0").WebEdit("备注摘要").Click
	.Frame("myiframe0").WebEdit("备注摘要").Set "备注摘要"
	''''''核算信息
	.Frame("myiframe0").WebList("还款方式").Click
	.Frame("myiframe0").WebList("还款方式").Select "等额本息"
	.Frame("myiframe0").WebList("还款周期").Click
	.Frame("myiframe0").WebList("还款周期").Select "按月"
	.Frame("myiframe0").WebEdit("还款账户名").Click
	.Frame("myiframe0").WebEdit("还款账户名").Set Environment.Value("CustomerName")
	.Frame("myiframe0").WebEdit("还款账户").Click
	.Frame("myiframe0").WebEdit("还款账户").Set Environment.Value("Account")
	.Frame("myiframe0").WebEdit("入账账户").Click
	.Frame("myiframe0").WebEdit("入账账户").Set Environment.Value("Account")
	'''''保存
	.Frame("TabContentFrame").WebElement("保存").Click
	Wait 3
End With
Print("贷款信息完成，用时："&timer-t&"s；时点："&time&"。")