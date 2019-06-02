rem-调试数据
	'Environment("PhaseOpnion")="批准"
	'Environment("UserID")="000678"

For iLoop = 1 To 15 Step 1
	If iLoop>14 or environment("PhaseOpnion")="批准" Then
		Exit for
	End If
	Login(Environment("UserID"))
	RunAction "1.1.6.1、进入菜单、选中数据、签署意见", oneIteration
	RunAction "1.1.6.2、提交审批", oneIteration
	Quit()
Next