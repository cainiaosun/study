'rem-调试数据：
'	rem-申请编号	
'	Environment("Serialno")="sq2019011100000001"

rem-选择需填写审查报告的数据
Browser("授信额度申请").Page("授信额度申请").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click

rem-审查报告生成
Browser("授信额度申请").Page("授信额度申请").Frame("right").WebElement("生成审查报告").Click
Browser("授信额度申请").dialog("来自网页的消息").WinButton("确定").Click
With Browser("授信额度申请").Window("调查报告定制打印设置 -- 网页对话框").Page("调查报告定制打印设置")
	.WebList("可选打印").Select "封面"
	.Image("向右添加").Click
	.WebElement("确定").Click
End With
Browser("报告").Page("报告").WebButton("关闭").WaitProperty "visible","ture",8000
Browser("报告").Page("报告").WebButton("关闭").click




