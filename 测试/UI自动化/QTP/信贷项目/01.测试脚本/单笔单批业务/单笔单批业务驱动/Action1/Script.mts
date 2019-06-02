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
	DataTable.Import "../../../导入数据/单笔单批业务全流程.xlsx"
	rem*设置路径(脚本组装调用脚本的路径)
	Environment.Value("Path")="../../../基础脚本库/贷款流程脚本"
	rem*恢复场景网址参数
	Environment.Value("URL")="http://11.8.121.150:7001/GDNY_CZ/logon.html"
End If
rem*初始化一组数据
Environment.Value("UserID")=DataTable("用户ID",globalsheet)
Environment.Value("CustomerType")=DataTable("客户类型",globalsheet)
Environment.Value("CustomerName")=DataTable("客户姓名",globalsheet)
Environment.Value("CertID")=DataTable("证件号码",globalsheet)
Environment.Value("BusinessType")=DataTable("业务品种",globalsheet)
Environment.Value("BusinessSum")=DataTable("授信总额",globalsheet)
Environment.Value("Limit")=DataTable("期限",globalsheet)
Environment.Value("AccountNo")=DataTable("入账账户",1)
Environment.Value("ReAccountNo")=DataTable("还款账户",1)
Environment.Value("ReAccountNoName")=DataTable("还款账户账户名",1)
Environment.Value("Payment")=DataTable("发放金额",1)
rem*根据业务品种加载并执行脚本
print Environment("BusinessType")
If i=0 or i=1 Then
	Environment.Value("ExamineNumber")=""
End If
If i<>0 and i<>1 and Environment("ExamineNumber")=i Then
	LogNote(">>>>执行第："&i-1&"次迭代完成>>>")
End If
LogNote(">>>执行第"&i&"次迭代："&Environment("BusinessType")&">>>")
LoadAndRunAction "../"&Environment("BusinessType"),Environment("BusinessType")
If i=DataTable.GetRowCount Then
	LogNote(">>>>执行第："&i&"次迭代完成>>>")
End If
Environment("ExamineNumber")=DataTable.GetCurrentRow+1'rem用于校验迭代是否完成