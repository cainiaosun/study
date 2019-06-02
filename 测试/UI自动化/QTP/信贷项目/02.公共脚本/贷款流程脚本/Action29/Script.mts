rem-调试参数
'	Environment("Serialno")="cz2019011800000004"
'	Environment("PhaseRole")="客户经理"
	'Environment("PhaseMenu")

rem-申请审批
Call FlowControl(1,Environment("PhaseRole"))rem-函数设置进入的页签和提交意见
With Browser("creationtime:=0").Page("title:=.*")
	If Environment("PhaseRole")="客户经理" Then
		rem*在申请发起时，选择申请的菜单
		.WebElement("innertext:=放贷申请","html tag:=span").Click
	Else
		rem*在进入审批阶段的时候，需要重新登录并进入审核的菜单
		'Login(Environment("UserID"))
		.WebElement("innertext:=放贷复核","html tag:=span").Click
		.Frame("name:=left").Link("text:="&Environment("PhaseMenu")&" .* 件","url:=.*N.\)").Click
	End If
	Call DataSubmit(Environment("Serialno"),Environment("PhaseOpnion"))rem*调用的签署意见并提交的方法
	If Environment("PhaseOpnion")="批准" Then
		rem-如果是批准，那么需要发送记账或发送关联系统，那此处只写了记账
		.Frame("name:=left").link("text:="&Environment("PhaseMenu")&"-未记账 .* 件").Click
		.Frame("name:=myiframe0").WebEdit("value:="&Environment("Serialno")).Click
		.Frame("name:=right").WebElement("text:=记账","index:=1").Click
		Browser("creationtime:=0").dialog("text:=来自网页的消息").WinButton("text:=确定").Click
		Print "放贷成功"
	End If
End With
'Call Quit()