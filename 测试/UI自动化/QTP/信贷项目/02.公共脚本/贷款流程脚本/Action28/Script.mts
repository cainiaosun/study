'rem-调试数据
'	Environment("BusinessSum" )="10000.00"
'	Environment("Limit")="12"
'	Environment("Rate")="12"
'	Environment("RepayType")="利随本清"
'	Environment("AccountNo")="010001230900006066"'rem*入账账户
'	Environment("ReAccountNo")="010001230900006066"rem*还款账户
'	Environment("ReAccountNoName")="TESTB0000183337"'rem*还款账户账户名
'	Environment("PayType" )="自主支付"

rem-获取页面显示的系统时间
str=Browser("浏览器").WinStatusBar("msctls_statusbar32").GetROProperty("text")
arr=split(str,"：")
SystemTime=arr(Ubound(arr))
Set Object=Browser("浏览器").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	Environment("Serialno")=Element(Object,"出帐流水号","WebEdit",0,0).GetRoProperty("value")
	Print("获取到的出账流水号："&Environment("Serialno"))
	Element(Object,"发放金额","WebEdit",0,0).Set						        Environment("LoanSum" )
	Element(Object,"是否绿色信贷","WebList",0,0).Select					"否"
	Element(Object,"是否环境、安全等重大风险企业贷款","WebList",0,0).Select	"否"
	Element(Object,"支付方式","WebList",0,0).Select	                                       Environment("PayType" )

Browser("浏览器").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
Browser("浏览器").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Sync
Browser("浏览器").Window("信贷风险管理系统V7").Close
If Browser("浏览器").Window("信贷风险管理系统V7").Dialog("二级弹框").Exist(5) Then
	Browser("浏览器").Window("信贷风险管理系统V7").Dialog("二级弹框").WinButton("确定").Click
End If  



'With Browser("浏览器").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
'	 Environment.Value("Serialno")=.Frame("myiframe0").WebEdit("出账流水号").getroproperty("value")
'	.Frame("myiframe0").WebEdit("发放金额").Click
'	.Frame("myiframe0").WebEdit("发放金额").Set environment("Payment")
'	.Frame("myiframe0").WebList("支付方式").Click
'	.Frame("myiframe0").WebList("支付方式").Select "自主支付"
'	.Frame("right").WebElement("保存").Click
'End With
'Browser("浏览器").Window("信贷风险管理系统V7").Close
'Browser("浏览器").Window("信贷风险管理系统V7").Dialog("Windows Internet Explorer").WinButton("确定").Click