'Environment.Value("Serialno")="UPL2018042500000014"
t=timer
RunAction "3.1、任务获取", oneIteration
wait 1
RunAction "3.2、面签信息", oneIteration
wait 1
RunAction "3.3、客户详情", oneIteration
wait 1
RunAction "3.4、贷款信息", oneIteration
wait 1
RunAction "3.5、关键信息复核", oneIteration
'提交操作
wait 0.5
RunAction "3.6、提交操作", oneIteration
wait 0.5
Print "申请："&Environment.Value("Serialno")&"信用速贷录入成功"
Print "信用速贷录入用时："&timer-t