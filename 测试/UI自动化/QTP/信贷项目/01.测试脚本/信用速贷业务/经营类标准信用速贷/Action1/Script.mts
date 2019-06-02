
t0=timer
Path=Environment("Path")
rem----------------------------------------------------------------------------------------------------------------------
rem----------------------------------------------------------------------------------------------------------------------
t=timer
rem--初始数据
'RunAction "0、初始数据", oneIteration'rem--调试可以使用这句初始数据
LoadAndRunAction Path,"0、初始数据",oneIteration
Call LogNote("数据初始完成!")
rem'面签阶段
'LoadAndRunAction Path,"1.0、新增面签）",oneIteration'rem--南粤e贷不评分需新增面签
If  Environment("BeginNumber")<=1 and 1<=Environment("EndNumber") Then
	Call LogNote("开始运行：面签阶段")
	Call Login(Environment.Value("UserID"))
	Call LogNote("开始运行：信用评估")
	LoadAndRunAction Path,"1.1、信用评估",oneIteration
	Call LogNote("运行完成：信用评估")
End If
If  Environment("BeginNumber")<=2 and 2<=Environment("EndNumber") Then
	Call LogNote("开始运行：面签流程")
	LoadAndRunAction Path,"1.2、发起面签",oneIteration
End If
If  Environment("BeginNumber")<=3 and 3<=Environment("EndNumber") Then
	LoadAndRunAction Path,"1.3.1、面签任务获取", oneIteration
	LoadAndRunAction Path,"1.3.2、面签任务处理", oneIteration
	Call LogNote("运行完成：面签流程")
	Call LogNote("运行完成：面签阶段")
End If
Print("面签阶段用时："&timer-t&"s")
rem----------------------------------------------------------------------------------------------------------------------
rem----------------------------------------------------------------------------------------------------------------------
rem-影像扫描阶段
If  Environment("BeginNumber")<=4 and 4<=Environment("EndNumber") Then
	t=timer
	Call LogNote("开始运行：影像扫描")
	LoadAndRunAction Path,"2、影像扫描", oneIteration
	Call LogNote("运行完成：影像扫描")
	Print("影像扫描阶段用时："&timer-t&"s")
End If
rem----------------------------------------------------------------------------------------------------------------------
rem----------------------------------------------------------------------------------------------------------------------
rem-录入阶段
t=timer
If  Environment("BeginNumber")<=5 and 5<=Environment("EndNumber") Then
	Call LogNote("开始运行：录入阶段")
	LoadAndRunAction Path,"3.1、任务获取", oneIteration
End If
If  Environment("BeginNumber")<=6 and 6<=Environment("EndNumber") Then
	LoadAndRunAction Path,"3.2、面签信息", oneIteration
End If
If  Environment("BeginNumber")<=7 and 7<=Environment("EndNumber") Then
	rem-LoadAndRunAction Path,"3.3、客户详情", oneIteration
	LoadAndRunAction Path,"3.3.1、客户详情", oneIteration
	LoadAndRunAction Path,"3.3.3、其他联系人", oneIteration
End If
If  Environment("BeginNumber")<=8 and 8<=Environment("EndNumber") Then
	LoadAndRunAction Path,"3.4、贷款信息", oneIteratio
End If
If  Environment("BeginNumber")<=9 and 9<=Environment("EndNumber") Then
	LoadAndRunAction Path,"3.5、关键信息复核", oneIteration
	LoadAndRunAction Path,"3.6、提交操作", oneIteration
	Call quit()
	Call LogNote("运行完成：录入阶段")
End If
Print("录入阶段用时："&timer-t&"s")
rem----------------------------------------------------------------------------------------------------------------------
rem----------------------------------------------------------------------------------------------------------------------
rem-征信调查阶段
t=timer
If  Environment("BeginNumber")<=10 and 10<=Environment("EndNumber") Then
	Call LogNote("开始运行：征信调查阶段")
	Call Login("008250")
	Environment.Value("Grained")="征信调查岗"
	LoadAndRunAction Path,"4、调整处理人", oneIteration
	Call quit()
End If
If  Environment("BeginNumber")<=11 and 11<=Environment("EndNumber") Then
	Call Login(Environment.Value("UserID"))
	LoadAndRunAction Path,"5.1、选择处理任务", oneIteration
End If
If  Environment("BeginNumber")<=12 and 12<=Environment("EndNumber") Then
	LoadAndRunAction Path,"3.3.2、综合征信信息", oneIteration
End If
If  Environment("BeginNumber")<=13 and 13<=Environment("EndNumber") Then
	LoadAndRunAction Path,"5.2、贷款参数", oneIteration
	LoadAndRunAction Path,"5.3、风险参数", oneIteration
End If
If  Environment("BeginNumber")<=14 and 14<=Environment("EndNumber") Then
	LoadAndRunAction Path,"5.4、意见处理和提交", oneIteration
	Call quit()
	Call LogNote("运行结束：征信调查阶段")
End If
Print("征信调查阶段用时："&timer-t&"s")
rem----------------------------------------------------------------------------------------------------------------------
rem----------------------------------------------------------------------------------------------------------------------
rem-审批阶段阶段
t=timer
If  Environment("BeginNumber")<=15 and 15<=Environment("EndNumber") Then
	Call LogNote("开始运行：审批阶段")
	Call Login("008250")
	Environment.Value("Grained")="三级审批师岗"
	LoadAndRunAction Path,"4、调整处理人", oneIteration
	Call quit()
	Call Login(Environment.Value("UserID"))
	LoadAndRunAction Path,"6.1、选择处理任务", oneIteration
	LoadAndRunAction Path,"6.2、意见处理和提交", oneIteration
	Call quit()
	Call LogNote("运行结束：审批阶段")
End If
Print("审批阶段用时："&timer-t&"s")
rem----------------------------------------------------------------------------------------------------------------------
rem----------------------------------------------------------------------------------------------------------------------
Print("申请  "&Environment("Serialno")&" 流程总用时" &timer-t0&"s")
Call LogNote("申请  "&Environment("Serialno")&" 流程总用时" &timer-t0&"s")