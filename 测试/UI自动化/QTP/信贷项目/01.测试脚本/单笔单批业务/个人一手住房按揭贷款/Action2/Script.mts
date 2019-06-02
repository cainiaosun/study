'environment("businesssum")="10000"
'environment("limit")="12"
'使用的变量environment("serialno")
'获取申请编号，作为后面识别处理的任务用
With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("申请信息填写")
	environment("serialno")=.WebEdit("申请编号").getroproperty ("value")
	print "获取的申请编号："&environment("serialno")
	.WebEdit("申请金额(元)").Set environment("BusinessSum")
	.WebEdit("敞口金额(元)").Set environment("BusinessSum")
	.WebList("用途").Click
	.WebList("用途").Select "购买住房-一手房"
	.WebList("本笔贷款是否为员工贷").Click
	.WebList("本笔贷款是否为员工贷").Select "否"
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
		.Frame("myiframe0").WebEdit("机构名称（入账机构）").Click
		.WebButton("确认").Click
	End With
	.WebButton("开发商名称").Click
	With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
		.Frame("myiframe0").WebEdit("客户名称（开发商）").Click
		.WebButton("确认").Click
	End With
	.WebEdit("购房合同号").Click
	.WebEdit("购房合同号").Set "购房合同1232131242231"
	.WebEdit("房屋地址").Click
	.WebEdit("房屋地址").Set "房屋地址"
	.WebEdit("单价（元/平米）").Click
	.WebEdit("单价（元/平米）").Set "1000000"
	.WebEdit("建筑面积（平米）").Click
	.WebEdit("建筑面积（平米）").Set "100"
	.WebEdit("首付金额（元）").Click
	.WebEdit("首付金额（元）").Set "10000000"
	.WebList("购房形式").Click
	.WebList("购房形式").Select "现房"
	.WebList("房屋类别").Click
	.WebList("房屋类别").Select "住宅"
	.WebEdit("购房套数").Click
	.WebEdit("购房套数").Set "1"
	.WebButton("主担保方式").Click
	rem*这里是主担保方式选择操作
	With Browser("单笔单批业务申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
		.Frame("left").WebElement("信用").Click
		.WebButton("确认").Click
	End With
	.WebList("是否开发商担保").Click
	.WebList("是否开发商担保").Select "是"
	.WebList("是否低风险业务").Click
	.WebList("是否低风险业务").Select "是"
	.WebList("是否员工标识").Click
	.WebList("是否员工标识").Select "否"
	.WebList("一般关联交易标识").Click
	.WebList("一般关联交易标识").Select "否"
	.WebList("重大关联交易标识").Click
	.WebList("重大关联交易标识").Select "否"
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
.Close
.Dialog("Windows Internet Explorer").WinButton("确定").Click
End With