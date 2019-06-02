'需要录制的操作：
'1、登录；
'2、面签预约；
'3、面签排班；
'4、面签处理；
'5、影像扫描；
'6、资料录入；
'7、提交审批；
t=timer
Call Login(Environment.Value("UserID"))
RunAction "1、面签流程", oneIteration
RunAction "2、影像扫描", oneIteration
RunAction "3、信用速贷录入", oneIteration
Call quit()
Call Login("008250")
Environment.Value("Grained")="征信调查岗"
RunAction "4、调整处理人", oneIteration
Call quit()
Call Login(Environment.Value("UserID"))
RunAction "5、信用速贷征信调查", oneIteration
Call quit()
Call Login("008250")
Environment.Value("Grained")="三级审批师岗"
RunAction "4、调整处理人", oneIteration
Call quit()
Call Login(Environment.Value("UserID"))
RunAction "6、信用速贷贷款审批", oneIteration
Call quit()
print "总耗时"&timer-t