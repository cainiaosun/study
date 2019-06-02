i=DataTable.GetCurrentRow
rem*DataTable.GetCurrentRow获取的首次迭代值有时候会是0有时候会是1(出现这种现象的原因不明白)
rem*第一次迭代的时候加载函数库和数据表
If i=0 or i=1 Then
	rem*加载函数库
	Environment.Value("Time")=0
	LoadFunctionLibrary "../../../函数库/ActionLibrary.qfl"
	LoadFunctionLibrary "../../../函数库/CreditLibrary.qfl"
	LoadFunctionLibrary "../../../函数库/PublicFunction.qfl"
	LoadFunctionLibrary "../../../函数库/UPlLibrary.qfl"
	rem*导入数据表
	DataTable.Import "../../../导入数据/信用速贷标准流程2.xlsx"
	rem*设置路径(脚本组装调用脚本的路径)
	Environment.Value("Path")="../../../基础脚本库/信用速贷"
	rem*恢复场景网址参数
	Environment.Value("URL")="http://11.8.121.150:7001/GDNY_CZ/logon.html"
End If

Print("开始信用评估...")
t=timer
With Browser("信贷风险管理系统V7")
	.Page("信贷风险管理系统V7").WebElement("信用评估查询").Click
	.Page("信用评估查询").Frame("right").WebElement("新增").Click
	With .Window("信用评分详情 -- 网页对话框").Page("信用评分详情")
		With .Frame("myiframe0")
			.WebEdit("客户名称").Click
			.WebEdit("客户名称").Set Datatable("客户姓名",globalsheet)
			.WebEdit("身份证号码").Click
			.WebEdit("身份证号码").Set DataTable("证件号码",globalsheet)
			.WebList("客户性质").Click
			.WebList("客户性质").Select DataTable("雇佣类型",globalsheet)
			.WebEdit("手机号码").Click
			.WebEdit("手机号码").Set DataTable("手机号码",globalsheet)
			.WebList("婚姻状态").Click
			.WebList("婚姻状态").Select DataTable("婚姻",globalsheet)
			.WebEdit("贷款金额").Click
			.WebEdit("贷款金额").Set DataTable("贷款金额",globalsheet)
			.WebList("期限").Click
			.WebList("期限").Select DataTable("期限",globalsheet)
			.WebList("户口所在地").Click
			.WebList("户口所在地").Select DataTable("户口所在地",globalsheet)
			If DataTable("家庭有本地房产",globalsheet)="" Then
				DataTable("家庭有本地房产",globalsheet)="否"
				DataTable("备注房产",globalsheet)="否"
			End If
			.WebList("家庭是否有本地房产").Click
			.WebList("家庭是否有本地房产").Select DataTable("家庭有本地房产",globalsheet)
			.WebList("职业类型").Click
			.WebList("职业类型").Select DataTable("职业类型",globalsheet)
			.WebEdit("所得税缴费基数").Click
			.WebEdit("所得税缴费基数").Set DataTable("所得税缴费基数",globalsheet)
			.WebEdit("月均银行流水/利润经营").Click
			.WebEdit("月均银行流水/利润经营").Set DataTable("月均银行流水",globalsheet)
			.WebEdit("住房公积金缴费基数").Click
			.WebEdit("住房公积金缴费基数").Set DataTable("住房公积金缴费基数",globalsheet)
			.WebEdit("社保缴费基数").Click
			.WebEdit("社保缴费基数").Set DataTable("社保缴费基数",globalsheet)
			.WebEdit("寿险缴费年限").Click
			.WebEdit("寿险缴费年限").Set DataTable("寿险年缴金额",globalsheet)
			If .WebList("职称级别").GetROProperty("disabled")=0 Then
				.WebList("职称级别").Click
				.WebList("职称级别").Select DataTable("职称级别",globalsheet)
			End If
			If .WebList("公务员级别").GetROProperty("disabled")=0 Then
				.WebList("公务员级别").Click
				.WebList("公务员级别").Select DataTable("公务员级别",globalsheet)
			End If	
			.WebList("自然村人口数量").Click
			.WebList("自然村人口数量").Select ""
			If DataTable("入账机构",globalsheet)="" Then
				DataTable("入账机构",globalsheet)="UPL深圳分部"
				DataTable("备注入账机构",globalsheet)="UPL深圳分部"
				DataTable("城市",globalsheet)="深圳"
			End If
			.WebList("入账机构").Click 
			.WebList("入账机构").Select DataTable("入账机构",globalsheet)
			.WebList("城市").Click
			.WebList("城市").Select DataTable("城市",globalsheet)
			.WebList("业务品种").Click
			.WebList("业务品种").Select DataTable("业务品种",globalsheet)
			If DataTable("营销专案",globalsheet)="高新技术企业华为专案"  Then
				DataTable("营销专案",globalsheet)="高新技术企业华为专案1.0"
				DataTable("备注专案",globalsheet)="高新技术企业华为专案1.0"
			ElseIf DataTable("营销专案",globalsheet)="高新技术优质企业专案"  Then
				DataTable("营销专案",globalsheet)="高新技术优质企业专案1.0"
				DataTable("备注专案",globalsheet)="高新技术优质企业专案1.0"
'			ElseIf DataTable("营销专案",globalsheet)="代发户随借随还" Then
'				DataTable("营销专案",globalsheet)="代发工资专案随借随还"
'				DataTable("备注专案",globalsheet)="代发工资专案随借随还"
'			
'			ElseIf DataTable("营销专案",globalsheet)="随心e贷"  Then
'				DataTable("营销专案",globalsheet)="随心e贷专案"
'				DataTable("备注专案",globalsheet)="随心e贷专案"
			End If
			.WebList("营销专属方案").Click
			.WebList("营销专属方案").Select DataTable("营销专案",globalsheet)
			.WebList("还款方式").Click
			.WebList("还款方式").Select DataTable("还款方式",globalsheet)
		End With
		.WebElement("保存").Click
		.WebElement("信用评估").Click
	End With
End With
With Browser("信贷风险管理系统V7").Window("信用评分详情 -- 网页对话框")
	If .Dialog("来自网页的消息").Exist(3) Then
		text=.Dialog("来自网页的消息").Static("提示").GetROProperty("text")
		If left(text,5)="没有该客户" Then
		.Dialog("来自网页的消息").Close:wait 1
		End If
	End If
	If .Dialog("来自网页的消息").Exist(5)  Then
		text=.Dialog("来自网页的消息").Static("提示").GetROProperty("text")
		If text="信用评估成功！并行处理结果:成功" Then
			print("信用评估成功！")
			DataTable("结果",1)="成功"
			.Dialog("来自网页的消息").Close:wait 2
		Else
			print("信用评估失败，请检查！")
			DataTable("结果",1)=text
		End If
	End If
End With:wait 3
ttime=timer-t
Environment.Value("Time")=Environment.Value("Time")+ttime
print("信用评估用时："&ttime)
print("截止目前总用时："&Environment.Value("Time"))