rem-调试参数
'	Environment("BusinessSum")="100000.00"
'	Environment("Limit")="12"
'	Environment("LowRisk" )="是"
'	Environment("IsCycle")="是"
'	Environment("GuaranteeType_0" )="0"rem-顶级担保方式大类，无时填0
'	Environment("GuaranteeType_1" )="0"rem-次级担保方式大类，无时填0
'	Environment("GuaranteeType" )="信用"rem-担保方式

Set Object=Browser("授信额度申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
	Environment("Serialno")=Element(Object,"流水号","WebEdit",0,0).GetRoProperty("value")
	Print("获取的申请编号是："&Environment("Serialno"))
	Element(Object,"名义金额(元)","WebEdit",0,0).Set						Environment("BusinessSum")
	Element(Object,"敞口金额(元)","WebEdit",0,0).Set						Environment("BusinessSum")
	Element(Object,"期限","WebEdit",0,0).Set						                Environment("Limit")
	Element(Object,"是否循环","WebList",0,0).Select 					        Environment("IsCycle")
	Element(Object,"用途(限100个汉字)","WebEdit",0,0).Set				 	"用途00001"
	Element(Object,"主要担保方式","WebButton",0,0).Click
	Set Object_child=Browser("授信额度申请").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
	Call ItemSelection(Object_child,Environment("GuaranteeType_0" ),Environment("GuaranteeType_1" ),"信用")
	Element(Object,"有无其他担保方式","WebList",0,0).Select 				"无"
	Element(Object,"是否低风险业务","WebList",0,0).Select 				        Environment("LowRisk" )
Browser("授信额度申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
Browser("授信额度申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Sync
Browser("授信额度申请").Window("信贷风险管理系统V7").Close