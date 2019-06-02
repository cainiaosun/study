environment("BusinessSum")="10000"
environment("Limit")="24"
With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
	'获取申请编号，作为后面识别处理的任务用
	Environment("SerialNo")=.WebEdit("申请编号").GetRoProperty ("value")
	Print "获取的申请编号："&Environment("SerialNo")
	'填写页面信息
	.WebList("业务子品种").Click
	.WebList("业务子品种"). Select "诚信通"
	.WebEdit("金额(元)").Set environment("BusinessSum")
	.WebEdit("敞口金额(元)").Set environment("BusinessSum")
	.WebEdit("用途").Click
	.WebEdit("用途").Set "用途"
	Value1=.WebEdit("贷款投向").GetROProperty("value")
	If Value1="" Then
		.WebButton("贷款投向").Click
		Set Object=Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
		rem*贷款投向选择操作
		Call IndustrySelection(Object)
	End If
	.WebEdit("期限").Click
	.WebEdit("期限").Set environment("Limit")
	.WebList("利率模式").Select "固定"
	.WebEdit("执行年利率").Set "5"
	.WebList("还款方式").Click
	.WebList("还款方式").Select "分期付息到期还本（当月需还款）"
	.WebList("还款周期").Select "按月"
	.WebEdit("统一还款日").Set "21"
	.WebButton("入账机构").Click
	rem*入账机构选择操作
	With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
		.Frame("myiframe0").WebEdit("机构名称（入账机构）").Click
		.WebButton("确认").Click
	End With
	.WebList("提款方式").Click
	.WebList("提款方式").Select "分次提款"
	.WebButton("主担保方式").Click
	rem*主担保方式选择操作
	With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
		.Frame("left").WebElement("信用").Click
		.WebButton("确认").Click
	End With
	.WebList("有无其它担保方式").Click
	.WebList("有无其它担保方式").Select "无"
	.WebList("是否低风险业务").Click
	.WebList("是否低风险业务").Select "是"
	.WebButton("协办客户经理").Click
	With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
		.Frame("myiframe0").WebEdit("协办客户经理").Set
		.WebButton("确认").Click
	End With
	Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
	Wait 30
	With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Dialog("来自网页的消息")
		If .WinButton("确定").exist(2.5) Then
			.WinButton("确定").Click
		End If
	End With
End With
Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Close
Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Dialog("Windows Internet Explorer").WinButton("确定").Click