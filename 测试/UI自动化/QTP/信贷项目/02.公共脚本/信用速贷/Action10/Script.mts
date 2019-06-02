Print("提交申请，时点："&time)
t=timer
Browser("面签处理管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("ObjectList").WebElement("提交").Click
Browser("面签处理管理").Window("信贷风险管理系统V7").Window("提交动作选择列表 -- 网页对话框").Page("提交动作选择列表").WebElement("提交").Click
Browser("面签处理管理").Window("信贷风险管理系统V7").Window("提交动作选择列表 -- 网页对话框").Dialog("来自网页的消息").WinButton("确定").Click
Browser("面签处理管理").Window("信贷风险管理系统V7").Window("提交动作选择列表 -- 网页对话框").Dialog("来自网页的消息").WinButton("确定").Click
If Browser("面签处理管理").Window("信贷风险管理系统V7").Dialog("Windows Internet Explorer").WinButton("确定").Exist(1) Then
	Browser("面签处理管理").Window("信贷风险管理系统V7").Dialog("Windows Internet Explorer").WinButton("确定").Click:Wait 1
End If
Print("提交申请完成，用时："&timer-t&"s；时点："&time&"。")