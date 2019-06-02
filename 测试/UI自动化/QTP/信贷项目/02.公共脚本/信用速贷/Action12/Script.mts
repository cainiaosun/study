'Environment.Value("Serialno")="UPL2018082100000018"

Print("影像扫描，时点："&time)
t=timer
Browser("影像扫描").Page("影像扫描").WebElement("影像扫描").Click
Browser("影像扫描").Page("影像扫描").Frame("TabContentFrame").WebElement("获取").Click
Browser("影像扫描").Window("请选择所需信息").Page("请选择所需信息").Frame("ObjectList").Link("查询条件").Click
Browser("影像扫描").Window("请选择所需信息").Page("请选择所需信息").Frame("ObjectList").WebEdit("申请编号").Set Environment("Serialno")
Browser("影像扫描").Window("请选择所需信息").Page("请选择所需信息").Frame("ObjectList").WebButton("查询").Click:Wait 2
Browser("影像扫描").Window("请选择所需信息").Page("请选择所需信息").Frame("myiframe0").WebEdit("value:="&Environment.Value("Serialno")).Click
Browser("影像扫描").Window("请选择所需信息").Page("请选择所需信息").WebButton("确认").Click
wait 2
Browser("影像扫描").Page("影像扫描").Frame("myiframe0").WebEdit("value:="&Environment.Value("Serialno")).Click
Browser("影像扫描").Page("影像扫描").Frame("TabContentFrame").WebElement("完成").Click
Browser("影像扫描").Dialog("来自网页的消息").WinButton("确定").Click
wait 0.5
Browser("影像扫描").Dialog("来自网页的消息").WinButton("确定").Click
wait 2
Call BrowserClose()    '关掉除第一个页面的其他网页页面
wait 3
Print("影像扫描完成，用时："&timer-t&"s；时点："&time&"。")