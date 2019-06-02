i=DataTable.GetCurrentRow
rem*DataTable.GetCurrentRow获取的首次迭代值有时候会是0有时候会是1(出现这种现象的原因不明白)
rem*第一次迭代的时候加载函数库和数据表
If i=0 or i=1 Then
	rem*加载函数库
	LoadFunctionLibrary "../../../函数库/ActionLibrary.qfl"
	LoadFunctionLibrary "../../../函数库/CreditLibrary.qfl"
	LoadFunctionLibrary "../../../函数库/PublicFunction.qfl"
	LoadFunctionLibrary "../../../函数库/UPlLibrary.qfl"
	rem*导入数据表
	DataTable.Import "../../../导入数据/信用速贷标准流程.xlsx"
	rem*设置路径(脚本组装调用脚本的路径)
	Environment.Value("Path")="../../../基础脚本库/信用速贷"
	rem*恢复场景网址参数
	Environment.Value("URL")="http://11.8.121.150:7001/GDNY_CZ/logon.html"
End If
rem*初始化一组数据
Environment.Value("Serialno")=DataTable("申请编号",1)
Environment.Value("UserID")=DataTable("用户ID",globalsheet)
Environment.Value("EmployType")=DataTable("雇佣类型",globalsheet)
Environment.Value("CustomerName")=DataTable("客户姓名",globalsheet)
Environment.Value("CertID")=DataTable("证件号码",globalsheet)
Environment.Value("BusinessType")=DataTable("业务品种",globalsheet)
Environment.Value("BusinessSum")=DataTable("授信总额",globalsheet)
Environment.Value("Term")=DataTable("期限",globalsheet)
Environment.Value("Account")=DataTable("入账账户",1)
Environment.Value("MarketingProgram")=DataTable("专案类型",1)
Environment.Value("CellphoneNumber")=DataTable("手机号码",1)
Environment.Value("RepaymentType")=DataTable("还款方式",1)
rem*根据业务品种加载并执行脚本
Print Environment("BusinessType")
LogNote(">>>执行第"&i&"次迭代："&Environment("BusinessType")&">>>")
LoadAndRunAction "../"&Environment("BusinessType"),Environment("BusinessType")
LogNote(">>>>执行第："&i&"次迭代完成>>>")