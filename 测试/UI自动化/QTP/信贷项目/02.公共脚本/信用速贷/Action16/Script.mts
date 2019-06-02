Print("综合财务信息，时点："&time)
t=timer
With Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	.Frame("myiframe0").WebEdit("月收入").Click
	.Frame("myiframe0").WebEdit("月收入").Set "10000.00"
	.Frame("myiframe0").WebList("家庭本地房产").Click
	.Frame("myiframe0").WebList("家庭本地房产").Select "有"
	.Frame("myiframe0").WebList("居住状况").Click
	.Frame("myiframe0").WebList("居住状况").Select "自置"
	.Frame("myiframe0").WebList("户口所在地").Click
	.Frame("myiframe0").WebList("户口所在地").Select "本地"
	'''下面是保存
	.Frame("DetailFrame").WebElement("保存").Click
End With
Print("综合财务信息完成，用时："&timer-t&"s；时点："&time&"。")