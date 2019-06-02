'rem-调试参数
'	Environment("CustomerName")="TESTB0000183337"
'	Environment("Serialno")="ht2019011800000010"
rem*进入菜单
Browser("放贷申请").Page("放贷申请").WebElement("放贷申请").Click
rem*新增并按合同选择放贷的数据
Browser("放贷申请").Page("放贷申请").Frame("right").WebElement("新增放贷申请").Click
With Browser("放贷申请").Window("请选择所需信息").Page("请选择所需信息")
	.Frame("ObjectList").Link("查询条件").Click
	.Frame("ObjectList").WebEdit("客户名称").Set Environment("CustomerName")
	.Frame("ObjectList").WebButton("查询").Click
	.Sync
	.Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click
	.WebButton("确认").Click
End With