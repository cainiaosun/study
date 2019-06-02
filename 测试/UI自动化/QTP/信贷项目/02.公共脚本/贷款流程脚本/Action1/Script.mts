'rem-调试数据
'	Environment("Type")="授信业务"
'	Environment("CustomerType")="公司客户"
'	Environment("CustomerName")="TESTB0000531530"
'	Environment("CertID")="45624541-X"
'	Environment("BusinessType_0")="0"rem-定级业务品种大类，如不存在填0
'	Environment("BusinessType_1")="授信额度"rem-次级业务品种大类，如不存在填0
'	Environment("BusinessType")="综合授信额度"rem-业务品种
'	Environment("IsSmall")="否"rem-是否小微
	
rem-进入菜单
With Browser("浏览器").Page("业务申请")
	If Environment("Type")="单笔业务"Then
		.Webelement("单笔单批业务申请").Click
	Else	
		.WebElement("授信额度申请").Click	
	End If
	.Frame("right").WebElement("新增申请").Click'点击新增申请按钮
End With
rem-弹出界面录入
With Browser("浏览器").window("新增窗口").Page("信贷风险管理系统V7")
	.Frame("选择").WebList("客户类型").Select Environment("CustomerType")'rem选择客户类型
	print(.Frame("选择").WebList("是否小微业务").GetRoProperty("disabled"))
	.Frame("按钮").WebElement("下一步").Click'选择客户类型后点击“下一步”
	If .Frame("选择").WebList("是否小微业务").Exist(15)  And .Frame("选择").WebList("是否小微业务").GetRoProperty("disabled")=0 Then
		.Frame("选择").WebList("是否小微业务").Select Environment("IsSmall")
	End If 
	.Frame("选择").WebButton("客户编号").WaitProperty "visible","ture",3000'rem*等待下一页面的“客户编号字段出现“
	.Frame("选择").WebButton("客户编号").Click'rem*点击客户编号进入选择客户
End With
rem-查询选择客户
Set Mypage=Browser("浏览器").window("新增窗口").Window("请选择所需信息").Page("请选择所需信息")
Call FindSelection(Mypage,Environment("CustomerName"),Environment("CertID"),"1","0","0","0")
rem-列表选择业务品种
Browser("浏览器").window("新增窗口").Page("信贷风险管理系统V7").Frame("选择").WebButton("业务品种").Click
Set Mypage=Browser("浏览器").window("新增窗口").Window("请选择所需信息").Page("请选择所需信息")
Call ItemSelection(Mypage,Environment("BusinessType_0"),Environment("BusinessType_1"),Environment("BusinessType"))
Browser("浏览器").window("新增窗口").Page("信贷风险管理系统V7").Frame("ObjectList").WebElement("确认").Click