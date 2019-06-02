Set Object=Browser("合同管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
Environment("Serialno")=Element(Object,"流水号","WebEdit",0,0).GetRoProperty("value")
Print("获取到的协议合同号："&Environment("Serialno"))
Element(Object,"文本合同编号","WebEdit",0,0).Set						"合同编号："&Now()
Begin_Date=Element(Object,"额度生效日","WebEdit",0,0).GetRoProperty("value")
Element(Object,"起始日期","WebEdit",0,0).Set							Begin_Date
Browser("合同管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
Browser("合同管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Sync
Browser("合同管理").Window("信贷风险管理系统V7").Close

'rem-点击完成登记
'Browser("合同管理").Page("合同管理").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click
'Browser("合同管理").Page("合同管理").Frame("right").WebElement("完成登记").Click
'Browser("合同管理").Dialog("来自网页的消息").WinButton("确定").Click
'If Browser("合同管理").Window("-- 网页对话框").Page("Page").WebElement("通过").Exist(30) Then
'	Print("协议登记成功！")
'Else
'	msgbox("协议额度登记风险探测不通过！")
'End If 
'Browser("合同管理").Window("-- 网页对话框").Page("Page").WebElement("确定").Click
'Browser("合同管理").Dialog("来自网页的消息").WinButton("确定").Click
'Browser("合同管理").Dialog("来自网页的消息").WinButton("确定").Click


rem-点击完成登记
Browser("合同管理").Page("合同管理").Frame("myiframe0").WebEdit("value:="&Environment("Serialno")).Click
Browser("合同管理").Page("合同管理").Frame("right").WebElement("完成登记").Click
Browser("合同管理").Dialog("一级弹框").WinButton("确定").Click
If Browser("合同管理").Dialog("一级弹框").Page("Page").WebElement("通过").Exist(30) Then
	Print("协议登记成功！")
Else
	msgbox("协议额度登记风险探测不通过！")
End If
Browser("合同管理").Dialog("一级弹框").Page("Page").WebElement("确定").Click
Browser("合同管理").Dialog("一级弹框").WinButton("确定").Click
Browser("合同管理").Dialog("一级弹框").WinButton("确定").Click