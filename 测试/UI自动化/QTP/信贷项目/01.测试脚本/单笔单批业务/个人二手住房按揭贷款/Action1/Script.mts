Login(Environment("UserID"))
Path=Environment("Path")
LoadAndRunAction Path,"1.1.1、新增申请"
LoadAndRunAction Path,"1.1.2、申请信息填写"
LoadAndRunAction Path,"1.1.3、填写审查报告"
LoadAndRunAction Path,"1.1.4、生成审查报告"
LoadAndRunAction Path,"1.1.5、签署意见并提交"
Quit()
rem*循环审批
Dim iLoop,t
t=timer
For iLoop = 1 To 15 Step 1
	Call FlowControl(4,Environment("PhaseRole"))
	print "需要选择的菜单："&environment("PhaseMenu")
	Login(Environment("UserID"))
	LoadAndRunAction Path,"1.1.6.1、进入菜单、选中数据、签署意见"
	LoadAndRunAction Path,"1.1.6.2、提交审批"
	Quit()
	If iLoop>14 or environment("PhaseOpnion")="批准" Then
		Exit for
	End If
Next
LoadAndRunAction Path,"2.1、查询批复流水号"
LoadAndRunAction Path,"2、合同登记"'rem合同登记内部存在登录和退出了
rem*登录
Login(Environment("UserID"))
rem*调用操作
LoadAndRunAction Path,"3.1、新增放贷"
LoadAndRunAction Path,"3.2、出账详情"
For iRow = 1 To 30 Step 1
	If iRow=1 Then
		environment.Value("PhaseRole")="0"rem*赋予一个初始值
	End If
	Call FlowControl(5,Environment("PhaseRole"))
	print Environment("PhaseOpnion")
	LoadAndRunAction Path,"3.3、提交及审批"
	If Environment("PhaseOpnion")="批准" Then
		Exit For
	End If
Next
print timer-t