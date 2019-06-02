Path=Environment.Value("Path")
Path="../../../基础脚本库/信用速贷"

t0=timer
rem-------------------------------------------------------------------------------------------
rem-------------------------------------------------------------------------------------------
t=timer
Call Login(Environment.Value("UserID"))
rem'面签阶段
rem-LoadAndRunAction Path,"1.0、新增面签",oneIteration
LoadAndRunAction Path,"1.1、信用评估",oneIteration
LoadAndRunAction Path,"1.2、发起面签",oneIteration
LoadAndRunAction Path,"1.3.1、面签任务获取", oneIteration
LoadAndRunAction Path,"1.3.2、面签处理信息填写", oneIteration
LoadAndRunAction Path,"1.3.3、面签资料审查填写", oneIteration
LoadAndRunAction Path,"1.3.4、面签意见处理", oneIteration
LoadAndRunAction Path,"1.3.5、提交申请", oneIteration
Print("面签阶段用时："&timer-t&"s")
rem-------------------------------------------------------------------------------------------
rem-------------------------------------------------------------------------------------------
rem-影像扫描阶段
t=timer
LoadAndRunAction Path,"2、影像扫描", oneIteration
Print("影像扫描阶段用时："&timer-t&"s")
rem-------------------------------------------------------------------------------------------
rem-------------------------------------------------------------------------------------------
rem-录入阶段
t=timer
LoadAndRunAction Path,"3.1、任务获取", oneIteration
LoadAndRunAction Path,"3.2、面签信息", oneIteration
rem-LoadAndRunAction Path,"3.3、客户详情", oneIteration
LoadAndRunAction Path,"3.3.1、基本信息", oneIteration
LoadAndRunAction Path,"3.3.2、工作信息", oneIteration
LoadAndRunAction Path,"3.3.3、财务综合信息", oneIteration
LoadAndRunAction Path,"3.3.4、其他联系人", oneIteration
LoadAndRunAction Path,"3.4、贷款信息", oneIteratio
LoadAndRunAction Path,"3.5、关键信息复核", oneIteration
LoadAndRunAction Path,"3.6、提交操作", oneIteration
Call quit()
Print("录入阶段用时："&timer-t&"s")
rem-------------------------------------------------------------------------------------------
rem-------------------------------------------------------------------------------------------
rem-征信调查阶段
t=timer
Call Login("008250")
Environment.Value("Grained")="征信调查岗"
LoadAndRunAction Path,"4、调整处理人", oneIteration
Call quit()
Call Login(Environment.Value("UserID"))
LoadAndRunAction Path,"5.1、选择处理任务", oneIteration
LoadAndRunAction Path,"3.3.5、综合征信信息", oneIteration
LoadAndRunAction Path,"5.2、风险参数", oneIteration
LoadAndRunAction Path,"5.3、面签意见处理", oneIteration
LoadAndRunAction Path,"5.4、提交申请", oneIteration
Call quit()
Print("征信调查阶段用时："&timer-t&"s")
rem-------------------------------------------------------------------------------------------
rem-------------------------------------------------------------------------------------------
rem-审批阶段阶段
t=timer
Call Login("008250")
Environment.Value("Grained")="三级审批师岗"
LoadAndRunAction Path,"4、调整处理人", oneIteration
Call quit()
Call Login(Environment.Value("UserID"))
LoadAndRunAction Path,"6.1、选择处理任务", oneIteration
LoadAndRunAction Path,"6.2、面签意见处理", oneIteration
LoadAndRunAction Path,"6.3、提交申请", oneIteration
Call quit()
Print("审批阶段用时："&timer-t&"s")
rem-------------------------------------------------------------------------------------------
rem-------------------------------------------------------------------------------------------
Print("申请  "&Environment("Serialno")&"  总耗时" &timer-t0&"s")