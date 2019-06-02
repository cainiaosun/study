'Environment.Value("Serialno")="UPL2018042500000014"
t=timer
RunAction "1.3.1、面签任务获取", oneIteration
wait 1
RunAction "1.3.2、面签处理信息填写", oneIteration
wait 1
RunAction "1.3.3、面签资料审查填写", oneIteration
wait 1
RunAction "1.3.4、面签意见处理", oneIteration
wait 1
RunAction "1.3.5、提交申请", oneIteration
Print "申请："&Environment.Value("Serialno")&"面签处理成功"
Print "面签处理用时："&timer-t