'Environment.Value("Serialno")=""
'Environment.Value("Grained")="三级审批师岗"
Print("调整处理人，时点："&time)
t=timer
'''1、使用总行用户登录
'Call Login("008025")
'''2、查询对应产品的岗位处理人
Browser("审批流程监控").Page("审批授权模型维度管理").WebElement("审批授权模型维度管理").Click
Browser("审批流程监控").Page("审批授权模型维度管理").Frame("left").WebElement("审批授权模型维度管理").Click
Browser("审批流程监控").Page("审批授权模型维度管理_2").Frame("right").Link("查询条件").Click
Browser("审批流程监控").Page("审批授权模型维度管理").Frame("right").WebList("业务品种").Select Environment.Value("BusinessType")
Browser("审批流程监控").Page("审批授权模型维度管理").Frame("right").WebButton("查询").Click
set biaodan=Browser("审批流程监控").Page("审批授权模型维度管理").Frame("myiframe0").WebTable("表单")
'environment.Value("grained")="征信调查岗"
Row=biaodan.RowCount()
Column=biaodan.ColumnCount(3)
For i = 3 To row Step 1
	For j = 2 To Column Step 1
		If biaodan.ChildItem(i,j,"webedit",0).getroproperty("value")= Environment.Value("Grained")Then
			tuichu="tuichu"
			exit for
		End If
	Next
	If tuichu="tuichu" Then
		Exit for
	End If
Next
'print i&j
str=biaodan.ChildItem(i,j+1,"webedit",0).getroproperty("value")
'print str
arr=split (str," ")
Environment.Value("UserID")=arr(1)
'print environment("userid")
'''3、调整处理人查询的有权处理人
Browser("审批流程监控").Page("审批流程监控").WebElement("信用速贷业务进度查询").Click
Browser("审批流程监控").Page("审批流程监控_2").Frame("left").WebElement("在办申请业务").Click
Browser("审批流程监控").Page("审批流程监控_2").Frame("right").Link("查询条件").Click
Browser("审批流程监控").Page("审批流程监控_2").Frame("right").WebEdit("申请编号").Set Environment.Value("Serialno")
Browser("审批流程监控").Page("审批流程监控_2").Frame("right").WebButton("查询").Click
Browser("审批流程监控").Page("审批流程监控_2").Frame("myiframe0").WebEdit("申请编号").Click ''因为通过申请编号查询的是唯一结果故而可以直接选择该条数据
Browser("审批流程监控").Page("审批流程监控_2").Frame("right_2").WebElement("任务调整").Click
Browser("审批流程监控").Window("请选择所需信息").Page("请选择所需信息").Frame("ObjectList").Link("查询条件").Click
Browser("审批流程监控").Window("请选择所需信息").Page("请选择所需信息").Frame("ObjectList").WebEdit("用户ID").Set Environment.Value("UserID")
Browser("审批流程监控").Window("请选择所需信息").Page("请选择所需信息").Frame("ObjectList").WebButton("查询").Click
wait 2
Browser("审批流程监控").Window("请选择所需信息").Page("请选择所需信息").Frame("myiframe0").WebEdit("用户ID").Click   ''查询结果是唯一的，所以直接选择
Browser("审批流程监控").Window("请选择所需信息").Page("请选择所需信息").WebButton("确认").Click
Browser("审批流程监控").Dialog("来自网页的消息").WinButton("确定").Click
Print("调整处理人完成，用时："&timer-t&"s；时点："&time&"。")