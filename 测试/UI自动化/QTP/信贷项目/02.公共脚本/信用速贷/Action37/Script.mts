Print("选择处理任务，时点："&time)
t=timer
'''进入菜单选择处理任务
Browser("任务提示").Page("任务提示").WebElement("信用速贷征信调查").Click
rem'这里可以考虑加一个页面加载的判断
Browser("任务提示").Page("任务提示").Frame("myiframe0").WebEdit("value:="&Environment.Value("Serialno")).Click
Browser("任务提示").Page("任务提示").Frame("right").WebElement("处理").Click
Set Object=Browser("任务提示").Window("信贷风险管理系统V7")
rem'Call DialogHandle(Object)
If Object.Dialog("micclass:=Dialog").WinButton("text:=是\(&Y\)").Exist(5) Then
	Object.Dialog("micclass:=Dialog").WinButton("text:=是\(&Y\)").Highlight
	Object.Dialog("micclass:=Dialog").WinButton("text:=是\(&Y\)").Click
End If
Print("选择处理任务完成，用时："&timer-t&"s；时点："&time&"。")