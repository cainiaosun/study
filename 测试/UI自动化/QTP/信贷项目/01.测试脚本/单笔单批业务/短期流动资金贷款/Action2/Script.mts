rem-调试数据：
	Environment("BusinessSum")="10000"
	Environment("Limit")="12"
	Environment("RateType")="固定"
	Environment("Rate")="12"	
	Environment("RepayType")="利随本清"
	Environment("RepayCycle")="一次"
	Environment("DrawingType")="分次提款"
	Environment("GuaranteeType_0" )="0"
	Environment("GuaranteeType_1" )="0"
	Environment("GuaranteeType" )="信用"
	Environment("LowRisk" )="是"
	
	
	
text=Browser("浏览器主窗口").WinStatusBar("msctls_statusbar32").GetRoProperty("text")
Print(text)
Environment("OrginNum" )=split(split(text,"：")(1),"-")(0)
Set Object=Browser("浏览器主窗口").Window("二级窗口").Page("信贷风险管理系统V7").Frame("myiframe0")
	Environment("Serialno")=Element(Object,"流水号","WebEdit",0,0).GetRoProperty("value")
	Print("获取的申请编号是："&Environment("Serialno"))
	Element(Object,"业务子品种","WebList",0,0).Select 						"诚信通"
	Element(Object,"用途","WebEdit",0,0).Set								"用途"
	Element(Object,"贷款投向","WebButton",0,0).Click
	Set Mypage=Browser("浏览器主窗口").Window("二级窗口").Window("三级窗口").Page("请选择所需信息")
	Call IndustrySelection(Mypage,"制造业","食品制造业","其他食品制造","营养食品制造")
	Element(Object,"金额(元)","WebEdit",0,0).Set							Environment("BusinessSum")
	Element(Object,"敞口金额(元)","WebEdit",0,0).Set						Environment("BusinessSum")
	Element(Object,"期限(月)","WebEdit",0,0).Set						        Environment("Limit")
	Element(Object,"利率模式","WebList",0,0).Select 					        Environment("RateType")	
	Element(Object,"执行年利率(%)","WebEdit",0,0).Set				 		Environment("Rate")	
	Element(Object,"还款方式","WebList",0,0).Select 						Environment("RepayType")
	Element(Object,"入账机构","WebButton",0,0).Click
	Set Mypage=Browser("浏览器主窗口").Window("二级窗口").Window("三级窗口").Page("请选择所需信息")
	Call FindSelection(Mypage,Environment("OrginNum" ),"1","0","0","0","0")
	If Browser("浏览器主窗口").Window("二级窗口").Dialog("二级弹框").Exist(3) Then
		Text=Browser("浏览器主窗口").Window("二级窗口").Dialog("二级弹框").Static("弹框内容").GetRoProperty("text")
		Browser("浏览器主窗口").Window("二级窗口").Dialog("二级弹框").WinButton("确定").Click
	End If   
	Element(Object,"还款周期","WebList",0,0).Select 						Environment("RepayCycle")
	Element(Object,"提款方式","WebList",0,0).Select 						Environment("DrawingType")	
	Element(Object,"主要担保方式","WebButton",0,0).Click
	Set Mypage=Browser("浏览器主窗口").Window("二级窗口").Window("三级窗口").Page("请选择所需信息")
	Call ItemSelection(Mypage,Environment("GuaranteeType_0" ),Environment("GuaranteeType_1" ),Environment("GuaranteeType" ))
	Element(Object,"有无其他担保方式","WebList",0,0).Select 				"无"
	Element(Object,"是否低风险业务","WebList",0,0).Select 				        Environment("LowRisk" )
Browser("浏览器主窗口").Window("二级窗口").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
Browser("浏览器主窗口").Window("二级窗口").Page("信贷风险管理系统V7").Sync
Browser("浏览器主窗口").Window("二级窗口").Close
For i = 1 To 3 Step 1
	If Browser("浏览器主窗口").Window("二级窗口").Dialog("二级弹框").Exist(5) Then
		Text=Browser("浏览器主窗口").Window("二级窗口").Dialog("二级弹框").Static("弹框内容").GetRoProperty("text")
		Browser("浏览器主窗口").Window("二级窗口").Dialog("二级弹框").WinButton("确定").Click
	Else:Exit For
	End If   
Next
