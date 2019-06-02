t=timer
RunAction "6.1、选择处理任务", oneIteration
Wait 3
RunAction "6.2、面签意见处理", oneIteration
wait 1
RunAction "6.3、提交申请", oneIteration
wait 2
print "申请："&Environment("Serialno")&"，信用速贷贷款审批成功"
print "信用速贷贷款审批用时："&timer-t