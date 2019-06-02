Print("其他联系人，时点："&time)
t=timer
With Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	.Frame("TabContentFrame").WebElement("其他联系人").Click
	.Frame("myiframe0").WebElement("密切联系人信息").waitproperty "visible","true",5000
	.Frame("myiframe0").WebEdit("密切联系人姓名").click
	.Frame("myiframe0").WebEdit("密切联系人姓名").Set "lihua"
	.Frame("myiframe0").WebList("密切联系人关系").Click
	.Frame("myiframe0").WebList("密切联系人关系").Select "配偶"	
	.Frame("myiframe0").WebEdit("密切联系人手机").Click
	.Frame("myiframe0").WebEdit("密切联系人手机").Set "18776765438"

	.Frame("myiframe0").WebEdit("紧急联系人1姓名").Click
	.Frame("myiframe0").WebEdit("紧急联系人1姓名").Set "zhangsan"
	.Frame("myiframe0").WebList("紧急联系人1关系").Click
	.Frame("myiframe0").WebList("紧急联系人1关系").Select "朋友"
	.Frame("myiframe0").WebEdit("紧急联系人1手机").Click
	.Frame("myiframe0").WebEdit("紧急联系人1手机").Set "18776453762"

	.Frame("myiframe0").WebEdit("紧急联系人2姓名").Click
	.Frame("myiframe0").WebEdit("紧急联系人2姓名").Set "lisi"
	.Frame("myiframe0").WebList("紧急联系人2关系").Click
	.Frame("myiframe0").WebList("紧急联系人2关系").Select "朋友"
	.Frame("myiframe0").WebEdit("紧急联系人2手机").Click
	.Frame("myiframe0").WebEdit("紧急联系人2手机").Set "18776459238"
	
	.Frame("myiframe0").WebEdit("紧急联系人3姓名").Click
	.Frame("myiframe0").WebEdit("紧急联系人3姓名").Set "wangmazi"
	.Frame("myiframe0").WebList("紧急联系人3关系").Click
	.Frame("myiframe0").WebList("紧急联系人3关系").Select "朋友"
	.Frame("myiframe0").WebEdit("紧急联系人3手机").Click
	.Frame("myiframe0").WebEdit("紧急联系人3手机").Set "19876453762"
	
	'''''''''保存
	.Frame("DetailFrame").WebElement("保存").Click		
End With
Print("其他联系人完成，用时："&timer-t&"s；时点："&time&"。")
	