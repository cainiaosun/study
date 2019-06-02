rem-调试数据
	Environment("Type")="单笔业务"rem-业务类型：额度业务、单笔业务
	Environment("BusinessType_0")="0"rem-顶级业务品种大类，如不存在填0
	Environment("BusinessType_1")="流动资金贷款"rem-次级业务品种大类，如不存在填0
	Environment("BusinessType")="短期流动资金贷款"rem-业务品种
	
	Environment("CustomerType")="公司客户"rem-客户类型：个人客户、公司客户
	Environment("IsSmall")="否"rem-是否小微
	Environment("CustomerName")="小茗同学"rem-客户名称
	Environment("CertID")="06455631-5"rem-证件号码

	Environment("Serialno")=""rem-流水号
	Environment("PhaseRole")="客户经理"rem-审批阶段每一阶段的用户角色名
	Environment("UserID")="000678"rem-各个阶段的用户ID
	Environment("PhaseMenu")=""rem-审批阶段需要选择的菜单页签
	Environment("PhaseOpnion")=""rem-审批的时候提交意见选择
	
	Environment("BusinessSum")="100000"rem-授信金额（协议金额也取这个值）
	Environment("ContractSum")="10000"rem-合同金额
	Environment("LoanSum")="10000"rem-放款/借据金额
	Environment("Limit")="12"rem-授信期限
	Environment("AmortiseLimit")="12"rem-摊还期限（气球贷专用）
	Environment("ContractLimit")="12"rem-合同期限
	Environment("Orgin")="11600113"rem*入账机构
	Environment("IsCycle")="是"rem-是否循环
	Environment("LowRisk" )="是"rem-是否低风险
	Environment("RateType")="固定"rem-利率模式：浮动、固定
	Environment("FloatType")=""rem-浮动方式：浮动比率、浮动点
	Environment("FloatPoint")=""rem-浮动值
	Environment("FloatRatio")=""rem-浮动比
	Environment("Rate")="12"rem-利率
	Environment("RepayType")="利随本清"rem-还款方式：等额本息、利随本清等
	Environment("RepayCycle")="一次"rem-还款周期：一次、按月等
	Environment("DrawingType")="分次提款"rem-提款方式：分次提款、一次提款
	Environment("PayType" )="自主支付"rem-支付方式
	Environment("AccountNo")="010001230900006108"'rem*入账账户
	Environment("ReAccountNoName")="小茗同学"'rem*还款账户账户名
	Environment("ReAccountNo")="010001230900006108"rem*还款账户
	Environment("GuaranteeType_0" )="0"rem-顶级担保方式大类，无时填0
	Environment("GuaranteeType_1" )="0"rem-次级担保方式大类，无时填0
	Environment("GuaranteeType" )="信用"rem-担保方式
	
	
	

	

Call LogNote("新任务！！！！！！")
rem-调用公共脚本的路径
Path="../../../02.公共脚本/贷款流程脚本"

t0=timer
UserID_Origin=Environment("UserID")
Call Login(Environment("UserID"))
LoadAndRunAction Path,"1.1.1、新增申请"
RunAction "申请信息", oneIteration

rem-签署意见提交
LoadAndRunAction Path,"1.1.3、填写审查报告"
LoadAndRunAction Path,"1.1.4、生成审查报告"
LoadAndRunAction Path,"1.1.5、签署意见并提交"
Call Quit()
t1=timer
Print("新增申请及提交用时："&t1-t0)
rem-授信循环审批
'Environment("PhaseRole")
For iLoop = 1 To 15 Step 1
	If iLoop>14 or environment("PhaseOpnion")="批准" Then
		Exit for
	End If
	Call Login(Environment("UserID"))
	LoadAndRunAction Path,"1.1.6.1、进入菜单、选中数据、签署意见"
	LoadAndRunAction Path,"1.1.6.2、提交审批"
	Call Quit()
Next
t2=timer
Print("授信循环审批用时："&t2-t1)
Print("申请审批总用时："&t2-t0)


Call Login("008250")
LoadAndRunAction Path,"2.1、查询批复流水号"
Call Quit()
t3=timer
Print("查询批复号用时："&t3-t2)

rem-协议合同
Call Login(UserID_Origin)
If Environment("Type")="单笔业务" Then
	LoadAndRunAction Path,"2.4、单笔合同登记"
	RunAction "合同信息", oneIteration
Else
	LoadAndRunAction Path,"2.2、登记协议"
	LoadAndRunAction Path,"2.2.1、协议信息"
	LoadAndRunAction Path,"2.3、项下合同登记"
	LoadAndRunAction Path,"2.3.1、项下合同信息"
End If
t4=timer
Print("登记协议及合同用时："&t4-t3)


rem-新增放贷
'Call Login(Environment("UserID"))
LoadAndRunAction Path,"3.1、新增放贷"
LoadAndRunAction Path,"3.2、出账详情"

rem-重置用户角色和提交意见（不重置的话前面审批阶段给他们赋值了影响判断）
Environment("PhaseRole")="客户经理"
Environment("PhaseOpnion")=""
rem-放贷循环审批
For i = 1 To 15 Step 1
	If Environment("PhaseOpnion")="批准" Then
		Exit For
	End If
	If Environment("PhaseRole")<>"客户经理" Then
		Call Login(Environment("UserID"))
	End If
	LoadAndRunAction Path,"3.3、提交及审批"
	Call Quit()
Next
t5=timer
Print("放款流程用时："&t5-t4)
Print("总时间："&t5-t0)