t=timer:RunAction "0、初始数据", oneIteration'rem--调试时请修改初始数据
Call Login(Environment("UserID"))
t1=timer:RunAction "1、面签流程", oneIteration:t2=timer:ms1="面签流程："&t2-t1:Print(ms1)&"；"
t1=timer:RunAction "2、影像扫描", oneIteration:t2=timer:ms2="影像扫描："&t2-t1:Print(ms2)&"；"
RunAction "3、信用速贷录入", oneIteration:t2=timer:ms3="信用速贷录入："&t2-t1:Print(ms3)&"；"
Call Quit()
Call Login("008250")
Environment("Grained")="征信调查岗"
t1=timer:RunAction "4、调整处理人", oneIteration:t2=timer:ms4="调整处理人："&t2-t1:Print(ms4)&"；"
Call Quit()
Call Login(Environment("UserID"))
t1=timer:RunAction "5、信用速贷征信调查", oneIteration:t2=timer:ms5="信用速贷征信调查："&t2-t1:Print(ms5)&"；"
Call Quit()
Call Login("008250")
Environment("Grained")="三级审批师岗"
t1=timer:RunAction "4、调整处理人", oneIteration:t2=timer:ms6="调整处理人："&t2-t1:Print(ms6)&"；"
Call Quit()
Call Login(Environment("UserID"))
t1=timer:RunAction "6、信用速贷贷款审批", oneIteration:t2=timer:ms7="信用速贷贷款审批："&t2-t1:Print(ms7)&"；"
Call Quit()
Print("各阶段运行时长"&ms1&ms2&ms3&ms4&ms5&ms6&ms7)
Print("流程总用时："&timer-t)
Call LogNote("各阶段运行时长"&ms1&ms2&ms3&ms4&ms5&ms6&ms7)
Call LogNote("流程总用时："&timer-t)