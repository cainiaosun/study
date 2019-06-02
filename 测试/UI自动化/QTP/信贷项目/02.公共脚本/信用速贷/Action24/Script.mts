'Environment.Value("Serialno")="UPL2018042500000014"
'Environment.Value("Grained")="征信调查岗"
t=timer
RunAction "5.1、选择处理任务", oneIteration
''填写信息并提交
wait 3
RunAction "3.3.5、综合征信信息", oneIteration
RunAction "5.2、风险参数", oneIteration
RunAction "5.3、面签意见处理", oneIteration
RunAction "5.4、提交申请", oneIteration
print "申请："&Environment("Serialno")&",信用速贷征信调查处理成功"
print "信用速贷征信调查处理用时："&timer-t