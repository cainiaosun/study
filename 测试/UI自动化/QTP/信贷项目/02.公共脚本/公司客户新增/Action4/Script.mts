print "迭代"&datatable.GetCurrentRow
rem*之所在前面加一个m变量的赋值操作是因为DataTable.GetCurrentRow获取的首次迭代值有时候会是0有时候会是1(为什么不明白)
Dim i,m
i=DataTable.GetCurrentRow
If i=0 Then
	Environment.Value("i")=1
	m=Environment("i")
End If
rem*第一次迭代的时候加载函数库和数据表
If i=0 Then
	rem*加载函数库
	LoadFunctionLibrary "C:\Users\922004\Desktop\孙洪斌\学习文档集\QTP脚本集\函数库\ActionLibrary.qfl"
	LoadFunctionLibrary "C:\Users\922004\Desktop\孙洪斌\学习文档集\QTP脚本集\函数库\CreditLibrary.qfl"
	rem*导入数据表
	DataTable.Import "C:\\Users\\922004\\Desktop\\孙洪斌\\学习文档集\\信贷脚本\\导入数据\\公司客户.xlsx"
End If
rem*初始化一组数据
rem-environment.Value("userid")=DataTable("用户ID",1)
environment.Value("CustomerType")=DataTable("客户类型",1)
environment.Value("CustomerName")=DataTable("客户名称",1)
environment.Value("CertID")=DataTable("组织机构号码",1)
environment.Value("SocialCreditID")=DataTable("社会统一信用代码",1)
rem-Login(environment("userid"))
RunAction "1、新增客户", oneIteration
RunAction "2、客户概况信息", oneIteration
wait 3 ''''等待保存成功
RunAction "3、客户高管信息", oneIteration
wait 1
Browser("客户管理").Window("信贷风险管理系统V7").Close
rem-Quit()