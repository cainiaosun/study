rem-调试参数
'	Environment.Value("Serialno")="sq20061117000021"
rem*查询并获取批复流水号
With Browser("快速查询主界面").Page("快速查询主界面")
	.WebElement("快速统计查询").Click
	.Frame("left").Image("gray_arrow").Click
	.Frame("left").WebElement("最终审批意见快速查询").Click
	.Frame("right").WebEdit("申请流水号").Set Environment("Serialno")
	.Frame("right").WebButton("查询").Click
	Environment.Value("Serialno")=.Frame("myiframe0").WebEdit("批复流水号").GetRoproperty("value") 
End With
print "获取的批复流水号："&Environment("Serialno")