'rem-调试数据	
'	Environment("PhaseRole")="公司分部审查岗"rem-当前处理人角色
'	Environment("PhaseMenu")="\[一般业务\]分部风险总监终审"rem-进入的菜单页签	
'	Environment("Serialno")="sq2019011100000001"rem-申请流水号
'	Environment("UserID")="000451"rem-用户编号
'	Environment("PhaseOpnion")="批准"rem-提交意见，调试的时候填写当前阶段的提交意见

	
rem-选中数据，并提交
Browser("授信业务审查审批").Page("授信业务审查审批").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click
Browser("授信业务审查审批").Page("授信业务审查审批").Frame("right").WebElement("提交").Click

rem-选择处理
With Browser("授信业务审查审批").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	.Frame("ObjectList").WebList("操作选择").Select environment("PhaseOpnion")rem-选择处理意见
	If Environment("PhaseOpnion")<>"批准" Then
		'获取下一岗位的：UserID，PhaseRole（下一处理阶段处理人角色）
		Dim value,arr
		value =.Frame("ObjectList").WebList("选择处理人").GetROProperty("all items")
		If value="" Then
			msgbox "没有可选处理人",,"提示框"
		End If
		value=split(value,";")(0)rem-拆分出第一个处理人字符串如:000265 罗智伟 410 支行行长/团队长
		Print "当前阶段的用户ID："&environment("UserID")
		Print "提交至："&value
		arr=split(value," ")rem-按空格拆分处理人字符串以获得UserID，角色等等
		Environment("UserID")=arr(0)rem-获取下一处理人的UserID
		Environment.Value("PhaseRole")=arr(3)rem-获取下一处理人角色名称（如：支行行长/团队长）
		Print("下一阶段处理人角色："&Environment("PhaseRole"))
		Print "下一阶段的用户ID："&environment("UserID")
		.Frame("ObjectList").WebList("选择处理人").Select value
	End If		
	.Frame("ObjectList").WebElement("提交").Click
End With
Browser("授信业务审查审批").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").Click
Browser("授信业务审查审批").Dialog("来自网页的消息").WinButton("确定").Click

If Environment("PhaseOpnion")="批准" Then
	'msgbox "审批通过",,"提示框"
	Print "审批通过"
End If