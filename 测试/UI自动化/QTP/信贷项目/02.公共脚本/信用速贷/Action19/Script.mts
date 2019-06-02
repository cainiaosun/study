'Environment.Value("Serialno")=""
'Environment.Value("CustomerName")="44010019800101023X-白金客户"
'Environment.Value("CertID")="44010019800101023X"
'Environment.Value("EmployType")="自雇人士客户"
'Environment.Value("BusinessSum")="100000"
'Environment.Value("Term")="12"
'Environment.Value("BusinessType")="经营类房贷信用速贷"
'Environment.Value("ECIFID")="A0003070287"
' Environment.Value("CellphoneNumber")="18774536565"
'Environment.Value("MarketingProgram")="普通方案"'营销方案
'Environment.Value("RepaymentType")="等额本息"
 Print("关键信息复核，时点："&time)
t=timer
 Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("DetailFrame").WebElement("关键信息复核").Click
Set Object=Browser("信用速贷申请").Window("信贷风险管理系统V7")	
If Object.Dialog("micclass:=Dialog").WinButton("text:=确定").Exist(4) Then
	Object.Dialog("micclass:=Dialog").WinButton("text:=确定").Click
End If
'''校验信息
For i = 1 To 5 Step 1
	If Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebTable("text:=客户编号.*").Exist(5) Then
		Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebTable("text:=客户编号.*").Highlight
		Exit For
	Else
		msgbox "表单识别异常，请刷新重试或重跑脚本"
	End If
Next
set biaodan=Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebTable("客户编号  *")
R=biaodan.RowCount()
For i = 1 To R Step 1
	C=biaodan.ColumnCount(i)
	For j = 1 To C Step 1
		MV=biaodan.GetCellData(i,j)
		Select Case MV
			Case "客户类型  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select Environment.Value("EmployType")
			Case "客户名称  * "
				'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
				biaodan.ChildItem(i,j+1,"WebEdit",0).Click
				biaodan.ChildItem(i,j+1,"WebEdit",0).Set Environment.Value("CustomerName")
			Case "客户身份证号  * "
				'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
				biaodan.ChildItem(i,j+1,"WebEdit",0).Click
				biaodan.ChildItem(i,j+1,"WebEdit",0).Set Environment.Value("CertID")
			Case "手机  * "
				'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
				biaodan.ChildItem(i,j+1,"WebEdit",0).Click
				biaodan.ChildItem(i,j+1,"WebEdit",0).Set Environment.Value("CellphoneNumber")
			Case "核心客户编号  * "
				'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
				biaodan.ChildItem(i,j+1,"WebEdit",0).Click
				biaodan.ChildItem(i,j+1,"WebEdit",0).Set Environment.Value("ECIFID")
			Case "贷款金额  * "
				'biaodan.ChildItem(i,j+1,"WebEdit",0).HighLight
				biaodan.ChildItem(i,j+1,"WebEdit",0).Click
				biaodan.ChildItem(i,j+1,"WebEdit",0).Set Environment.Value("BusinessSum")
			Case "贷款期限  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select Environment.Value("Term")
			Case "还款类型  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select Environment.Value("RepaymentType")
			Case "营销方案  * "
				'biaodan.ChildItem(i,j+1,"WebList",0).HighLight
				biaodan.ChildItem(i,j+1,"WebList",0).Click
				biaodan.ChildItem(i,j+1,"WebList",0).Select Environment.Value("MarketingProgram")
		End Select	
	Next
Next
'With Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
'	.WebEdit("客户名称").waitproperty "visible","true",5000
'	.WebList("客户类型").Click
'	.WebList("客户类型").Select Environment.Value("EmployType")
'	.WebEdit("客户名称").Click
'	.WebEdit("客户名称").Set Environment.Value("CustomerName")
'	.WebEdit("客户身份证号").Click
'	.WebEdit("客户身份证号").Set Environment.Value("CertID")
'	.WebEdit("手机").Click
'	.WebEdit("手机").Set Environment.Value("CellphoneNumber")
'	.WebEdit("核心客户编号").Click
'	.WebEdit("核心客户编号").Set Environment.Value("ECIFID")
'	.WebEdit("贷款金额").Click
'	.WebEdit("贷款金额").Set Environment.Value("BusinessSum")
'	.WebList("贷款期限").Click
'	.WebList("贷款期限").Select Environment.Value("Term")
'	.WebList("还款类型").Click
'	.WebList("还款类型").Select Environment.Value("RepaymentType")
'	.WebList("营销方案").Click
'	.WebList("营销方案").Select Environment.Value("MarketingProgram")
'End With
'''校验
Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("TabContentFrame").WebElement("校验").Click
Browser("信用速贷申请").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").Click
'''关闭录入信息填写页面
Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Image("Close 关闭").Click
wait 2
Call BrowserClose()    '关掉除第一个页面的其他网页页面
Print("关键信息复核完成，用时："&timer-t&"s；时点："&time&"。")