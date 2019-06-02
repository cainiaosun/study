'Environment.Value("Serialno")="UPL2018042500000014"
t=timer
With Browser("面签排班管理").Page("面签排班管理")
	.WebElement("面签排班").Click
	.Frame("myiframe0").WebEdit("value:="&Environment.Value("Serialno")).Click
	.Frame("right").WebElement("任务详情").Click
	Browser("面签排班管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("ObjectList").WebElement("保存").Click
	Browser("面签排班管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Image("Close 关闭").Click
	'''UPL用户发起的这一步没有'''Browser("面签排班管理").Window("信贷风险管理系统V7").Dialog("Windows Internet Explorer").WinButton("确定").Click
	Wait 2
	Browser("面签排班管理").Refresh
	.Frame("myiframe0").WebEdit("value:="&Environment.Value("Serialno")).Click
	.Frame("right").WebElement("更新台账").Click
	Browser("面签排班管理").Dialog("来自网页的消息").WinButton("确定").Click
	Browser("面签排班管理").Dialog("来自网页的消息").WinButton("确定").Click
End With
wait 2.5
Print "申请："&Environment.Value("Serialno")&",面签排班成功"
Print "面签排班用时："&timer-t