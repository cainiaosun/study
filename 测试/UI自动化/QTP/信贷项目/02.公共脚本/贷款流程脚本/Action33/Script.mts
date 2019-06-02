rem-调试参数
	Environment("Serialno")="cz2019011800000004"
	Environment("PhaseRole")="客户经理"
	Environment("PhaseOpnion")=""
rem*参数定义并赋值
Environment.Value("UserID")=DataTable("用户ID",1)
Environment.Value("CustomerName")=DataTable("客户姓名",1)
'Environment.Value("serialno")=DataTable("合同编号",1)'rem*通过参数传递就行了
Environment.Value("Payment")=DataTable("发放金额",1)
rem*登录
Login(Environment("UserID"))
rem*调用操作
RunAction "3.1、新增放贷", oneIteration
RunAction "3.2、出账详情", oneIteration
For Iterator = 1 To 10 Step 1
	If Environment("PhaseOpnion")="批准" Then
		Exit For
	End If
	RunAction "3.3、提交及审批", oneIteration
Next