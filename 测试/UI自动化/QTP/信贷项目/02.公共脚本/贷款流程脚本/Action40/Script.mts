'rem-调试数据
'	Environment("BusinessSum" )="10000.00"
'	Environment("Limit")="12"
'	Environment("Rate")="12"
'	Environment("RepayType")="利随本清"
'	Environment("AccountNo")="010001230900006066"'rem*入账账户
'	Environment("ReAccountNo")="010001230900006066"rem*还款账户
'	Environment("ReAccountNoName")="TESTB0000183337"'rem*还款账户账户名

rem-获取页面显示的系统时间
str=Browser("合同管理").WinStatusBar("msctls_statusbar32").GetROProperty("text")
arr=split(str,"：")
SystemTime=arr(Ubound(arr))
Set Object=Browser("合同管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
	Environment("Serialno")=Element(Object,"流水号","WebEdit",0,0).GetRoProperty("value")
	Print("获取到的合同号："&Environment("Serialno"))
	Element(Object,"业务子品种","WebList",0,0).Select						"诚信通"
	Element(Object,"合同编号","WebEdit",0,0).Set							"合同编号："&Now()
	Element(Object,"金额(元)","WebEdit",0,0).Set						        Environment("ContractSum")
	Element(Object,"起始日期","WebEdit",0,0).Set							SystemTime
	Element(Object,"用途","WebEdit",0,0).Set								"合同用途0001"
	Element(Object,"贷款投向","WebButton",0,0).Click
	Set Mypage=Browser("合同管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	Call IndustrySelection(Mypage,"制造业","食品制造业","其他食品制造","营养食品制造")
	Element(Object,"贷款投向(行内行业)","WebList",0,0).Select				"钢贸"
	Element(Object,"期限(月)","WebEdit",0,0).Set							Environment("ContractLimit")
	Element(Object,"利率模式","WebList",0,0).Select						Environment("RateType")
	Element(Object,"执行年利率(%)","WebEdit",0,0).Set						Environment("Rate")
	Element(Object,"还款方式","WebList",0,0).Select						Environment("RepayType")
	Element(Object,"还款周期","WebList",0,0).Select						Environment("RepayCycle")
	Element(Object,"入账账户","WebEdit",0,0).Set							Environment("AccountNo")
	Element(Object,"还款账户","WebEdit",0,0).Set							Environment("ReAccountNo")
	Element(Object,"还款账户名","WebEdit",0,0).Set							Environment("ReAccountNoName")
	Element(Object,"提款方式","WebList",0,0).Select						Environment("DrawingType")
	Element(Object,"主要担保方式","WebButton",0,0).Click
	Set Mypage=Browser("合同管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	Call ItemSelection(Mypage,"0","0","信用")
	Element(Object,"有无其他担保方式","WebList",0,0).Select				"无"
	Element(Object,"是否低风险业务","WebList",0,0).Select					Environment("LowRisk" )
	Element(Object,"是否异地业务","WebList",0,0).Select					"本市"
	Element(Object,"是否外保内贷","WebList",0,0).Select					"否"

Browser("合同管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
Browser("合同管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Sync
Browser("合同管理").Window("信贷风险管理系统V7").Close
If Browser("合同管理").Window("信贷风险管理系统V7").Dialog("二级弹框").Exist(5) Then
	Browser("合同管理").Window("信贷风险管理系统V7").Dialog("二级弹框").WinButton("确定").Click
End If  

rem-点击完成登记
Browser("合同管理").Page("合同管理").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click
Browser("合同管理").Page("合同管理").Frame("right").WebElement("完成登记").Click
Browser("合同管理").Dialog("一级弹框").WinButton("确定").Click
If Browser("合同管理").Dialog("一级弹框").Page("Page").WebElement("通过").Exist(30) Then
	Print("项下合同登记成功！")
Else
	msgbox("项下合同登记风险探测不通过！")
End If
Browser("合同管理").Dialog("一级弹框").Page("Page").WebElement("确定").Click
Browser("合同管理").Dialog("一级弹框").WinButton("确定").Click
Browser("合同管理").Dialog("一级弹框").WinButton("确定").Click