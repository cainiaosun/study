With Browser("客户管理").Window("信贷风险管理系统V7")
.Page("信贷风险管理系统V7").Frame("left").WebElement("客户高管信息").Click
.Page("信贷风险管理系统V7").Frame("right").WebElement("新增").WaitProperty "visible","true",5
.Page("信贷风险管理系统V7").Frame("right").WebElement("新增").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebButton("高管姓名").Click
.Window("请选择所需信息").Page("请选择所需信息").Frame("myiframe0").WebEdit("客户编号").Click
.Window("请选择所需信息").Page("请选择所需信息").WebButton("确认").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebList("担任职务").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebList("担任职务").Select "法人代表（高管）"
.Page("信贷风险管理系统V7").Frame("myiframe0").WebList("性别").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebList("性别").Select "男性"
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("出生日期").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("出生日期").Object.value="1950/01/01"
.Page("信贷风险管理系统V7").Frame("myiframe0").WebList("学历").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebList("学历").Select "研究生"
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("工作经历").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("工作经历").Set "工作简历"
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("联系电话").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("联系电话").Set "18778764537"
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("担任该职务时间").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("担任该职务时间").Set "1995/01/01"
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("相关从业年限").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("相关从业年限").Set "10"
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("持股情况").Click
.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("持股情况").Set "100%持股"
.Page("信贷风险管理系统V7").Frame("right_2").WebElement("1x1").Click
End With