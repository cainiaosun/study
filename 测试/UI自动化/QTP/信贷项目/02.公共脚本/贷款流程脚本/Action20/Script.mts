rem-调试数据
	Environment("CustomerType")="公司客户"
	Environment("CustomerName")="TESTB0000531530"
	Environment("CertID")="45624541-X"
	Environment("BusinessType")="综合授信额度"
	Environment("BusinessSum")="10000"
	Environment("Limit")="12"
	Environment.Value("Orgin")="11600113"rem*入账机构
	Environment("Serialno")=""
	Environment("PhaseMenu")=""
	Environment("PhaseOpnion")=""
	Environment("PhaseRole")=""
	
	


Dim t
t=timer
Environment.Value("t")=timer
rem*登录
t1=timer
Environment("UserID")="000678"
Login(Environment("UserID"))
rem*调用操作
RunAction "1.1.1、新增申请", oneIteration
LoadAndRunAction "C:/Users/922004/Desktop/孙洪斌/学习文档集/信贷脚本/测试脚本/单笔单批业务全流程/综合授信额度","授信额度基本信息"
'RunAction "1.1.2、申请信息填写", oneIteration
RunAction "1.1.3、填写审查报告", oneIteration
RunAction "1.1.4、生成审查报告", oneIteration
RunAction "1.1.5、签署意见并提交", oneIteration
Quit()
time1=timer-t1
t2=timer
RunAction "1.1.6、审查审批", oneIteration
print "申请信息填写用时："&time1&"s"
print "审批用时："&timer-t2&"s"
print "申请总用时："&timer-t&"s"