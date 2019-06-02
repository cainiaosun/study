Environment.Value("UserID")=DataTable("用户ID",1)
Login(Environment("UserID"))
rem*本脚本不涉及目录及其它关联性的问题,可以放心调用,做好参数传递就可以了
'rem*调试用预置数据,调试可以复制到填写部分前面
'environment.Value("serialno")="pf2017122200000001"
'BusinessSum="10000"'rem*合同金额
'Term="12"'rem*合同期限
'RateType="浮动"'rem*利率浮动方式
'Rate="10"'rem*执行年利率（利率模式为固定需要有值）
'AccountNo="110001201900000761"'rem*入账账户
'ReAccountNo="110001201900000761"rem*还款账户
'ReAccountNoName="TESTB0000731816"'rem*还款账户账户名
'SystemTime="2032/12/16"
rem*预置数据
BusinessSum=Environment("BusinessSum" ) 'rem*合同金额
Term=Environment("Limit")'rem*合同期限
RateType="浮动"'rem*利率浮动方式
Rate="10"'rem*执行年利率（利率模式为固定需要有值）
AccountNo=Environment("AccountNo")'rem*入账账户
ReAccountNo=Environment("ReAccountNo")rem*还款账户
ReAccountNoName=Environment("ReAccountNoName")'rem*还款账户账户名
rem*进入登记合同菜单
Browser("合同管理").Page("合同管理").WebElement("登记合同").Click
Browser("合同管理").Page("合同管理").Frame("left").WebElement("未登记完成的合同").Click
Browser("合同管理").Page("合同管理_2").Frame("right").WebElement("登记合同").WaitProperty "visible","true",5000
rem*获取页面展示的系统时间，这一步可以放在其他地方
str=Browser("合同管理").WinStatusBar("msctls_statusbar32").GetROProperty("text")
arr=split(str,"：")
SystemTime=arr(Ubound(arr))
rem*如果列表已存在批复那么直接进入详情,如果没有则登记合同
Select Case Browser("合同管理").Page("合同管理_3").Frame("myiframe0").WebEdit("value:="&environment.Value("serialno")).Exist(2)
	Case true
	Browser("合同管理").Page("合同管理_3").Frame("myiframe0").WebEdit("value:="&environment.Value("serialno")).Click
	Browser("合同管理").Page("合同管理_3").Frame("right").WebElement("合同详情").Click
	Case false
	Browser("合同管理").Page("合同管理_2").Frame("right").WebElement("登记合同").Click
	Browser("合同管理").Window("请选择所需信息").Page("请选择所需信息").Frame("myiframe0").WebEdit("value:="&environment.Value("serialno")).Click
	Browser("合同管理").Window("请选择所需信息").Page("请选择所需信息").WebButton("确认").Click
End Select
rem*合同信息的填写
With Browser("合同管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
	environment.Value("serialno")=.WebEdit("合同流水号").GetROProperty("value")'rem*获取一下合同流水号
	.WebEdit("合同编号").Click
	.WebEdit("合同编号").Set "合同编号："&Now()
	.WebEdit("申请金额（元）").Click
	.WebEdit("申请金额（元）").Set BusinessSum
	.WebEdit("起始日期").Click
	.WebEdit("起始日期").Set SystemTime
'	.WebList("贷款是否投向工业转型升级项目").Click
'	.WebList("贷款是否投向工业转型升级项目").Select "是"
'	.WebList("贷款是否投向战略新兴产业").Click
'	.WebList("贷款是否投向战略新兴产业").Select "节能环保"
'	.WebList("贷款是否投向文化产业").Click
'	.WebList("贷款是否投向文化产业").Select "是"
'	.WebList("贷款投向（行内行业）").Click
'	.WebList("贷款投向（行内行业）").Select "钢贸"
	.WebEdit("期限").Click
	.WebEdit("期限").Set Term
	.WebList("利率模式").Click
	.WebList("利率模式").Select RateType
	.WebList("利率模式").Click
	Select Case RateType
		Case "固定"
		.WebEdit("执行年利率").Click
		.WebEdit("执行年利率").Set Rate
		Case "浮动"
		.WebList("利率浮动方式").Click
		.WebList("利率浮动方式").Select "浮动点"
		.WebEdit("利率浮动值").Click
		.WebEdit("利率浮动值").Set "0"
	End Select
	.WebList("还款方式").Click
	.WebList("还款方式").Select "等额本息"
	.WebList("还款周期").Click
	.WebList("还款周期").Select "按月"
	.WebEdit("入账账户").Click
	.WebEdit("入账账户").Set AccountNo
	.WebEdit("还款账户").Click
	.WebEdit("还款账户").Set ReAccountNo
	.WebEdit("还款账户账户名").Click
	.WebEdit("还款账户账户名").Set ReAccountNoName
'	.WebList("是否内保外贷").Click
'	.WebList("是否内保外贷").Select "是"
End With 
Browser("合同管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
Browser("合同管理").Window("信贷风险管理系统V7").Close
If Browser("合同管理").Window("信贷风险管理系统V7").Dialog("Windows Internet Explorer").WinButton("确定").exist(2) Then
	Browser("合同管理").Window("信贷风险管理系统V7").Dialog("Windows Internet Explorer").WinButton("确定").Click
End If
rem*选择数据完成登记
Browser("合同管理").Page("合同管理_3").Frame("myiframe0").WebEdit("value:="&environment.Value("serialno")).Click
Browser("合同管理").Page("合同管理_4").Frame("right").WebElement("完成登记").Click
Browser("合同管理").Window("-- 网页对话框").Page("Page").WebElement("检查结果").WaitProperty "visible","true",15000
Browser("合同管理").Window("-- 网页对话框").Page("Page").WebElement("确定").Click
Browser("合同管理").Dialog("来自网页的消息").WinButton("确定").Click
Browser("合同管理").Dialog("来自网页的消息").WinButton("确定").Click
Quit()
print "获取的合同流水号："&Environment("serialno")
print "登记完成"