rem-调试数据
	'Environment("BeginNumber")=0'rem--执行开始的步骤位置
	'Environment("EndNumber")=100'rem--结束的步骤位置
'	Environment("UserID")="008268"'
'	Environment("Serialno")=""
'	Environment("ECIFID")=""
'	
'	Environment("CustomerName")="黄三八"
'	Environment("CertID")="110100199101013380"
'	Environment("CellphoneNumber")= "13499880338"
'	Environment("EmployType")="自雇人士客户"
'	Environment("BusinessSum")="100000.00"
'	Environment("Term")="36"
'	Environment("BusinessType")="经营类标准信用速贷"
'	Environment("MarketingProgram")="普通方案"'营销方案
'	Environment("RepaymentType")="等额本息"'还款方式
'	Environment("IsCycle")="是"'额度是否循环
'	Environment("Account")="010001235000282806"'账号
'	Environment("PayType")="自主支付"'支付方式
'	
'	Environment("MaritalStatus")="未婚"rem-婚姻状态
'	Environment("HouseholdRegister")="本地"rem-户口所在地
'	Environment("LocalProperty")="是"rem-是否有本地房产
'	Environment("OccupationalType")="高新技术"rem-职业类型
'	Environment("AccountEntryOrgan")="广州分行速贷业务部（微小）"rem-入账机构
'	Environment("EducationLevel") ="本科"rem-教育程度
'	Environment("Sex")="男性"rem-性别
'	
'	Environment("评分数据")=""

rem--初始数据
Function DataTableOperate(DataSheetNum)
	rem--匹配调整，执行行数据，DataSheetNum匹配数据表的位置值
	'Call DataTableOperate(2)
	Environment("TestCaseNum")=DataTable("案例编号",1)
	Environment("CurrentRow")=DataTable.GetCurrentRow
	RowCount=DataTable.GetRowCount'rem--这样的获取方法要求第一个sheet表必须是Global所需表
	For i = 0 To RowCount Step 1		
		If DataTable("案例编号",DataSheetNum)=Environment("TestCaseNum") Then
			Exit For'rem--先判断当前执行行对应数据是否匹配，匹配退出循环，不匹配遍历数据查询到匹配项为止
		ElseIf i=RowCount  Then
			rem--循环到GetCurrentRow-1次时已将遍历完成所有的数据，没有找到数据则打印日期并恢复当前执行行
			Call LogNote("没有找到对案例"&Environment("TestCaseNum") &"对应的测试数据！")
			DataTable.SetCurrentRow(Environment("CurrentRow"))
		Else
			rem--循环重置执行行数
			DataTable.SetCurrentRow(i+1)
		End If
	Next
End Function
Call DataTableOperate(2)'rem-切换到数据表匹配数据成功的行数
	Environment("BeginNumber")=DataTable("开始步骤",2)'rem--执行开始的步骤位置
	Environment("EndNumber")=DataTable("结束步骤",2)''rem--结束的步骤位置
	Environment("UserID")=DataTable("用户ID",2)
	Environment("Serialno")=DataTable("流水号",2)
	Environment("ECIFID")=DataTable("核心客户号",2)
	
	Environment("CustomerName")=DataTable("客户姓名",2)
	Environment("CertType")=DataTable("证件类型",2)
	Environment("CertID")=DataTable("证件号码",2)
	Environment("CellphoneNumber")=DataTable("手机号码",2)
	Environment("Account")=DataTable("入账账户",2)
	Environment("RepayAccountName1")=DataTable("还款账户名1",2)
	Environment("RepayAccount")=DataTable("还款账户1",2)
	Environment("RepayAccountName1")=DataTable("还款账户名2",2)
	Environment("RepayAccount")=DataTable("还款账户2",2)	
	Environment("TransferAccountName1")=DataTable("转账账户名",2)
	Environment("TransferAccount")=DataTable("转账账户",2)			
	
	Environment("BusinessType")=DataTable("业务品种",2)
	Environment("EmployType")=DataTable("雇佣类型",2)
	Environment("BusinessSum")=DataTable("授信总额",2)
	Environment("Term")=DataTable("期限",2)
	
	Environment("MarketingProgram")=DataTable("专案类型",2)
	Environment("RepaymentType")=DataTable("还款方式",2)
	Environment("IsCycle")=DataTable("是否循环",2)
	
	Environment("PayType")=DataTable("支付方式",2)
	Environment("InnerBank")=DataTable("行内受托",2)
	
	Environment("MaritalStatus")="未婚"rem-婚姻状态
	Environment("HouseholdRegister")="本地"rem-户口所在地
	Environment("LocalProperty")="是"rem-是否有本地房产
	Environment("OccupationalType")="高新技术"rem-职业类型
	Environment("AccountEntryOrgan")="广州分行速贷业务部（微小）"rem-入账机构
	Environment("EducationLevel") ="本科"rem-教育程度
	Environment("Sex")="男性"rem-性别
	Environment("评分数据")=""
DataTable.SetCurrentRow(Environment("CurrentRow"))rem--赋值完毕后恢复执行行行数