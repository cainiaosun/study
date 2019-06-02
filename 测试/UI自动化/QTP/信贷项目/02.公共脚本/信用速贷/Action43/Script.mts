Print("面签意见处理，时点："&time)
t=timer
With Browser("任务提示").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	.Frame("right").WebElement("审批意见处理").Click
	Wait 1.5
	.Frame("myiframe0").WebList("审批结果").Click
	.Frame("myiframe0").WebList("审批结果").Select "同意"
	.Frame("myiframe0").WebEdit("审批意见").Click
	.Frame("myiframe0").WebEdit("审批意见").Set "同意申请"
	.Frame("TabContentFrameArr2").WebElement("保存").Click	
	Wait 1
End With
Print("面签意见处理完成，用时："&timer-t&"s；时点："&time&"。")