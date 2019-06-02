Print("提交操作，时点："&time)
t=timer
Browser("信用速贷申请").Page("信用速贷申请").Frame("myiframe0").WebEdit("value:="&Environment.Value("Serialno")).Click
Browser("信用速贷申请").Page("信用速贷申请").Frame("right").WebElement("提交").Click
Browser("信用速贷申请").Dialog("来自网页的消息").WinButton("确定").Click
Browser("信用速贷申请").Window("提交动作选择列表 -- 网页对话框").Page("提交动作选择列表").WebElement("提交").Click
Browser("信用速贷申请").Window("提交动作选择列表 -- 网页对话框").Dialog("来自网页的消息").WinButton("确定").Click
Browser("信用速贷申请").Window("提交动作选择列表 -- 网页对话框").Dialog("来自网页的消息").WinButton("确定").Click
Print("提交操作完成，用时："&timer-t&"s；时点："&time&"。")