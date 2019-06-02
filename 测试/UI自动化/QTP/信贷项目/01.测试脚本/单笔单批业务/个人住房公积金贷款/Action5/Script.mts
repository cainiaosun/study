'environment.Value("BusinessSum")="10000"
'environment.Value("Limit")="12"
'environment.Value("Orgin")="11600112"
'environment.Value("serialno")=""
'获取申请编号，作为后面识别处理的任务用
With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("申请信息填写")
	environment("serialno")=.WebEdit("申请编号").getroproperty ("value")
	print "获取的申请编号："&environment("serialno")
	.WebEdit("申请金额(元)").Set environment("BusinessSum")
	.WebEdit("敞口金额(元)").Set environment("BusinessSum")
	.WebEdit("用途").Click
	.WebEdit("用途").set "用途"
'	Value1=.WebEdit("贷款投向").GetROProperty("value")
'	If Value1="" Then
'		.WebButton("贷款投向").Click
'		Set Page1=Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
'		rem*贷款投向选择操作
'		Page1.Frame("frameleft").WebElement("行业类型大类").WaitProperty "visible","true",6
'		Page1.Frame("left").Image("gray_arrow").Click
'		Page1.Frame("left").WebElement("农业").Click
'		Page1.Frame("frameright").WebElement("行业类型子类").WaitProperty "visible","true",6
'		Page1.Frame("left_2").Image("gray_arrow").Click
'		Page1.Frame("left_2").WebElement("稻谷种植").Click
'		Page1.Frame("frameright").WebElement("确定").Click
'	End If
	.WebEdit("期限").Click
	.WebEdit("期限").Set environment("Limit")
	.WebList("利率模式").Select "固定"
	.WebEdit("执行年利率").Set "5"
	.WebList("还款方式").Click
	.WebList("还款方式").Select "等额本息"
	.WebList("还款周期").Select "按月"
	.WebEdit("统一还款日").Set "21"
	.WebButton("入账机构").Click
	rem*这里是入账机构选择操作
	With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
		.Frame("ObjectList").WebEdit("机构编号").Set environment("Orgin")
		.Frame("ObjectList").WebButton("查询").Click
		.Frame("myiframe0").WebEdit("value:="&environment("Orgin")).Click
		.WebButton("确认").Click
	End With
	.WebEdit("开发商名称").Click
	.WebEdit("开发商名称").Set "开发商名称"
	.WebEdit("房屋地址").Click
	.WebEdit("房屋地址").Set "房屋地址"
	.WebEdit("房屋总价").Click
	.WebEdit("房屋总价").Set "1000000"
	.WebEdit("首付金额（元）").Click
	.WebEdit("首付金额（元）").Set "500000"
	.WebEdit("首付比例").Click
	.WebEdit("首付比例").Set "50"
	.WebEdit("按揭贷款成熟（%）").Click
	.WebEdit("按揭贷款成熟（%）").Set "50"
'	.WebList("提款方式").Click
'	.WebList("提款方式").Select "分次提款"
	.WebButton("主担保方式").Click
	rem*这里是主担保方式选择操作
	With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
		.Frame("left").WebElement("信用").Click
		.WebButton("确认").Click
	End With
	.WebList("有无其他担保方式").Click
	.WebList("有无其他担保方式").Select "无"
	.WebList("是否开发商担保").Click
	.WebList("是否开发商担保").Select "是"
	.WebList("是否低风险业务").Click
	.WebList("是否低风险业务").Select "是"
	.WebButton("协办客户经理").Click
	With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
		.Frame("myiframe0").WebEdit("用户ID(协办客户经理)").Click
		.WebButton("确认").Click
	End With
End With
Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
With Browser("单笔单批业务申请").Window("信贷风险管理系统V7")
If .Dialog("来自网页的消息").WinButton("确定").exist(2.5) Then
	.Dialog("来自网页的消息").WinButton("确定").Click
End If
wait 1
.Close
.Dialog("Windows Internet Explorer").WinButton("确定").Click
End With