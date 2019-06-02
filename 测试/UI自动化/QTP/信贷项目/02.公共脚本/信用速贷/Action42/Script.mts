'Environment.Value("Serialno")="UPL2018080800000009"

Print("面签任务获取，时点："&time)
t=timer
Browser("面签处理管理").Page("面签处理管理").WebElement("面签处理").Click
Browser("面签处理管理").Page("面签处理管理").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click
Browser("面签处理管理").Page("面签处理管理").Frame("right").WebElement("获取面签").Click:wait 1
Print("面签任务获取完成，用时："&timer-t&"s；时点："&time&"。")