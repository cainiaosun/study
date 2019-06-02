'rem-调试数据	
'	Environment("PhaseRole")="公司分部审查岗"rem-当前处理人角色
'	Environment("PhaseMenu")="\[一般业务\]分部风险总监终审"rem-进入的菜单页签	
'	Environment("Serialno")="sq2019011100000001"rem-申请流水号
'	Environment("UserID")="000451"rem-用户编号
'	Environment("PhaseOpnion")="提交批文生成岗"rem-上一级选择的批文

PhaseOpnion_L=Environment("PhaseOpnion")rem-批文生成阶段和审查都用的是审查岗，通过这个变量判断是否点击“批文整理”按钮，是否填写审查报告，初值默认为空，后续取每一步的上一级意见
Call FlowControl(Environment("BusinessType"),Environment("PhaseRole"))rem-函数设置进入的页签和提交意见
Print "需要选择的菜单："&Environment("PhaseMenu")
Print("当前处理人角色："&Environment("PhaseRole"))
rem-进入菜单
Browser("信贷风险管理系统V7").Page("授信业务审查审批").WebElement("授信业务审查审批").Click
rem-选中处理任务的菜单和数据
With Browser("信贷风险管理系统V7").Page("授信业务审查审批")
	.Frame("left").Link("text:="&Environment("PhaseMenu")&" \d+ 件","url:=.*N.{2}").Click
	.Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click
	rem-签署意见
	Print("当前提交意见："&Environment("PhaseOpnion"))
	If PhaseOpnion_L="提交批文生成岗" Then
		.Frame("right").WebElement("批文整理").Click
	Else
		.Frame("right").WebElement("签署意见").Click
	End If	
End With
With Browser("信贷风险管理系统V7").Window("信贷风险管理系统V7")	
	If PhaseOpnion_L="提交批文生成岗" Then
		.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("批文").Set "批文信息"
		.Page("信贷风险管理系统V7").Frame("ObjectList").WebElement("保存").Click
	Else
		.Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("意见输入栏").Set "同意申请"
		.Page("信贷风险管理系统V7").Frame("TabContentFrame").WebElement("保存").Click
	End If	
	.Close
	If .Dialog("Windows Internet Explorer").WinButton("确定").Exist(2) Then
		.Dialog("Windows Internet Explorer").WinButton("确定").Click
	End If
End With
If Environment("PhaseRole")="公司分部审查岗" and PhaseOpnion_L<>"提交批文生成岗"Then
	RunAction "1.1.6.3、审查报告填写和生成", oneIteration
End If