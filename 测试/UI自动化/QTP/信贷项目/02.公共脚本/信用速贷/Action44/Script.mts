Print("提交申请，时点："&time)
t=timer
Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("提交").Click
Browser("任务提示").Window("信贷风险管理系统V7").Window("提交动作选择列表 -- 网页对话框").Page("提交动作选择列表").WebElement("提交").Click
wait 1
Browser("任务提示").Window("信贷风险管理系统V7").Window("提交动作选择列表 -- 网页对话框").Dialog("来自网页的消息").WinButton("确定").Click
If Browser("任务提示").Window("信贷风险管理系统V7").Window("提交动作选择列表 -- 网页对话框").Dialog("来自网页的消息").WinButton("确定").Exist(10) Then
	Browser("任务提示").Window("信贷风险管理系统V7").Window("提交动作选择列表 -- 网页对话框").Dialog("来自网页的消息").WinButton("确定").Click
End If
Set Object=Browser("任务提示").Window("信贷风险管理系统V7")
rem'Call DialogHandle(Object)''如果审批通过出账的话，这里会有一个出账成功的弹框
For i = 1 To 5 Step 1
	If Object.Dialog("micclass:=Dialog").Exist(3)Then
		If Object.Dialog("micclass:=Dialog").WinButton("text:=确定").Exist(2) Then
			Object.Dialog("micclass:=Dialog").WinButton("text:=确定").Click
		ElseIf Object.Dialog("micclass:=Dialog").WinButton("text:=确认").Exist(2) Then
			Object.Dialog("micclass:=Dialog").WinButton("text:=确认").Click
		ElseIf Object.Dialog("micclass:=Dialog").WinButton("text:=是\(&Y\)").Exist(2) Then
			Object.Dialog("micclass:=Dialog").WinButton("text:=是\(&Y\)").Click
		End If
	Else
		Exit for'如果没有发现Dialog弹框，那么退出循环
	End If
Next	
wait 3
Print("提交申请完成，用时："&timer-t&"s；时点："&time&"。")