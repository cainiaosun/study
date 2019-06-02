'Environment.Value("Serialno")="UPL2018082100000018"

Print("获取任务，时点："&time)
t=timer
Browser("信用速贷申请").Page("信用速贷申请").WebElement("信用速贷录入").Click
Browser("信用速贷申请").Page("信用速贷申请").Frame("right").WebElement("获取申请").Click:Wait 1
Browser("信用速贷申请").Window("请选择所需信息").Page("请选择所需信息").Frame("myiframe0").WebEdit("value:="&Environment.Value("Serialno")).Click
Browser("信用速贷申请").Window("请选择所需信息").Page("请选择所需信息").WebButton("确认").Click:Wait 0.5
'Call BrowserClose()
Print("获取任务完成，用时："&timer-t&"s；时点："&time&"。")