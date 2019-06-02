'rem-调试数据：
'	rem-申请编号	
'	Environment("Serialno")="sq2019011100000001"

rem-选择需填写审查报告的数据
Browser("授信业务审查审批").Page("授信业务审查审批").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click

rem-审查报告填写
Browser("授信业务审查审批").Page("授信业务审查审批").Frame("right").WebElement("填写审查报告").Click
With Browser("授信业务审查审批").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	If .Frame("myiframe0").WebEdit("选择的报告类型").exist(3) then'rem-判断是否已填写审查报告，判断选择报告类型的弹框是否弹出，弹出报告未填写，不弹出为已填写
		.Frame("myiframe0").WebEdit("选择的报告类型").click
		.Frame("ObjectList").WebElement("确定").Click	
	End If
	.Image("Close 关闭").WaitProperty "visible","ture",5000
	.Image("Close 关闭").click
End With

rem-选择需填写审查报告的数据
Browser("授信业务审查审批").Page("授信业务审查审批").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click

rem-审查报告生成
Browser("授信业务审查审批").Page("授信业务审查审批").Frame("right").WebElement("生成审查报告").Click
Browser("授信业务审查审批").dialog("来自网页的消息").WinButton("确定").Click
With Browser("授信业务审查审批").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("ObjectList")
	.WebList("选择打印报告内容").Select "封面"
	.Image("添加箭头").Click
	.WebElement("确定打印").Click
End With
Browser("报告").Page("报告").WebButton("关闭").WaitProperty "visible","ture",8000
Browser("报告").Page("报告").WebButton("关闭").click