'rem-调试数据：
'	rem-申请编号	
'	Environment("Serialno")="sq2019011100000001"

rem-选择需填写审查报告的数据
Browser("授信额度申请").Page("授信额度申请").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click

rem-审查报告填写
Browser("授信额度申请").Page("授信额度申请").Frame("right").WebElement("填写审查报告").Click
With Browser("授信额度申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	If .Frame("myiframe0").WebEdit("选择的报告类型").exist(10) then'rem-判断是否已填写审查报告，判断选择报告类型的弹框是否弹出，弹出报告未填写，不弹出为已填写
		.Frame("myiframe0").WebEdit("选择的报告类型").click
		.Frame("ObjectList").WebElement("确定").Click
	Else:Print("已填写审查报告或审查报告填写页面打开失败！！！")	
	End If
	.Image("Close 关闭").WaitProperty "visible","ture",5000
	.Image("Close 关闭").click
End With