'rem-调试数据
'	rem-流水号
'	Environment.Value("Serialno")="sq2019011100000001" 
'	Environment("UserID")="000678"
'	Environment("BusinessType")="综合授信额度"
	
rem-预置数据
Environment.Value("PhaseRole")="客户经理"rem-初始值为"客户经理"
Call FlowControl(Environment("BusinessType"),Environment("PhaseRole"))rem-函数设置进入的页签和提交意见


rem-选择数据
Browser("授信额度申请").Page("授信额度申请").Frame("myiframe0").WebEdit("value:="&environment("Serialno")).Click
rem-签署意见
Browser("授信额度申请").Page("授信额度申请").Frame("right").WebElement("签署意见").Click
With Browser("授信额度申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	.Frame("myiframe0").WebEdit("意见输入框").Set "同意申请"
	.Frame("ObjectList").WebElement("保存").Click
	.Image("Close 关闭").Click
End With


rem-选择数据
Browser("授信额度申请").Page("授信额度申请").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click
rem-提交申请
Browser("授信额度申请").Page("授信额度申请").Frame("right").WebElement("提交").Click
rem-风险探测
With Browser("授信额度申请").Window("-- 网页对话框").Page("Page")
	.WebElement("最终检测结果").waitproperty "visible","true",8000
	.WebElement("确定").Click
End With
rem-选择处理
With Browser("授信额度申请").Window("提交动作选择列表 -- 网页对话框").Page("提交动作选择列表")
	.WebList("选择操作").Select Environment.Value("PhaseOpnion")rem-选择处理意见
	'获取下一岗位的：UserID，PhaseRole（下一处理阶段处理人角色）
	Dim value,arr,arr1
	value =.WebList("选择处理人").GetROProperty("all items")
	If value="" Then
		msgbox "没有可选处理人",,"提示框"
	End If
	value=split(value,";")(0)rem-拆分出第一个处理人字符串如:000265 罗智伟 410 支行行长/团队长
	Print "当前阶段的用户ID："&environment("UserID")
	Print "提交至："&value
	arr=split(value," ")rem-按空格拆分处理人字符串以获得UserID，角色等等
	Environment("UserID")=arr(0)rem-获取下一处理人的UserID
	Environment.Value("PhaseRole")=arr(3)rem-获取下一处理人角色名称（如：支行行长/团队长）
	.WebList("选择处理人").Select value
	.WebElement("提交").Click
End With
Browser("授信额度申请").Window("提交动作选择列表 -- 网页对话框").Dialog("来自网页的消息").WinButton("确定").Click
Browser("授信额度申请").Dialog("来自网页的消息").WinButton("确定").Click