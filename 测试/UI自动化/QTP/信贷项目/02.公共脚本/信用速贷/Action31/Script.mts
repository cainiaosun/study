t=timer
RunAction "1.1、信用评估", oneIteration
RunAction "1.2、发起面签", oneIteration
RunAction "1.3、面签处理", oneIteration
Print "面签总用时："&timer-t