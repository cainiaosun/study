Print("选择处理任务，时点："&time)
t=timer
Browser("任务提示").Page("任务提示").WebElement("信用速贷贷款审批").Click
Browser("任务提示").Page("任务提示").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click
Browser("任务提示").Page("任务提示").Frame("right").WebElement("处理").Click
Wait 2
Set Object=Browser("任务提示").Window("信贷风险管理系统V7")
rem'Call DialogHandle(Object)
If Object.Dialog("micclass:=Dialog").WinButton("text:=是\(&Y\)").Exist(5) Then
	Object.Dialog("micclass:=Dialog").WinButton("text:=是\(&Y\)").Highlight
	Object.Dialog("micclass:=Dialog").WinButton("text:=是\(&Y\)").Click
End If
Print("选择处理任务完成，用时："&timer-t&"s；时点："&time&"。")