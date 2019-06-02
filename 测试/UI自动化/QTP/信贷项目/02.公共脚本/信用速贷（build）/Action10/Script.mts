rem-调试数据
'	Environment("UserID")="008268"'
'	Environment("Serialno")=""
'	Environment("ECIFID")=""
'	
'	Environment("CustomerName")="TESTA0000931393"
'	Environment("CertID")="440823199102250619"
'	Environment("CellphoneNumber")= "13499880350"
'	Environment("EmployType")="自雇人士客户"
'	Environment("BusinessSum")="100000.00"
'	Environment("Term")="36"
'	Environment("BusinessType")="经营类标准信用速贷"
'	Environment("MarketingProgram")="普通方案"'营销方案
'	Environment("RepaymentType")="等额本息"'还款方式
'	Environment("IsCycle")="是"'额度是否循环
'	Environment("Account")="6217270010001364617"'账号
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


path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)
rem--信用评估
Environment("评分数据")="136"&Cstr(RandomNumber(10000000,99999999))
Print(Environment("评分数据"))
Set Home_Page=Browser("主窗口（浏览器）").Page("主窗口Page页")
	Element(Home_Page,"信用评估查询","WebElement","html tag","SPAN",,,0).Click

Set Home_Frame_Left=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("left")

Set Home_Frame_Right=Browser("主窗口（浏览器）").Page("主窗口Page页").Frame("right")
	Element(Home_Frame_Right,"新增","WebElement","html tag","TD",,,1).Click

Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")
Set First_Page=Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")
Set myiframe0=Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页").Frame("myiframe0_0")
	Element_Relation(myiframe0,"客户名称","WebEdit",1,0,0).Set                             Environment("CustomerName")
	Element_Relation(myiframe0,"证件号码","WebEdit",1,0,0).Set                             Environment("CertID")
	Element_Relation(myiframe0,"手机号码","WebEdit",1,0,0).Set                             Environment("评分数据")  
	Element_Relation(myiframe0,"客户性质","WebList",1,0,0).Select                       Environment("EmployType")
	Element_Relation(myiframe0,"婚姻状态","WebList",1,0,0).Select                       Environment("MaritalStatus")
	Element_Relation(myiframe0,"贷款金额","WebEdit",1,0,0).Set                             Environment("BusinessSum")
	Element_Relation(myiframe0,"贷款期限","WebList",1,0,0).Select                       Environment("Term")
	Element_Relation(myiframe0,"户口所在地","WebList",1,0,0).Select                   Environment("HouseholdRegister")
	Element_Relation(myiframe0,"家庭有本地房产","WebList",1,0,0).Select          Environment("LocalProperty")
	If Environment("EmployType")<>"自雇人士客户" Then
		Element_Relation(myiframe0,"职业类型","WebList",1,0,0).Select               Environment("OccupationalType")
	End If
	Element_Relation(myiframe0,"所得税缴费基数","WebEdit",1,0,0).Set                                  "100000.00"
	Element_Relation(myiframe0,"月均银行流水/利润经营","WebEdit",1,0,0).Set                    "100000.00"
	Element_Relation(myiframe0,"住房公积金缴费基数","WebEdit",1,0,0).Set                         "100000.00"
	Element_Relation(myiframe0,"社保缴费基数","WebEdit",1,0,0).Set                                      "100000.00"
	Element_Relation(myiframe0,"寿险年缴金额","WebEdit",1,0,0).Set                                      "100000.00"
	If Element_Relation(myiframe0,"职称级别","WebList",1,0,0).GetROProperty("disabled")=0 Then
		Element_Relation(myiframe0,"职称级别","WebList",1,0,0).Select                                 ""
	End If
	If Element_Relation(myiframe0,"公务员级别","WebList",1,0,0).GetROProperty("disabled")=0 Then
		Element_Relation(myiframe0,"公务员级别","WebList",1,0,0).Select                             ""
	End If
	Element_Relation(myiframe0,"职务","WebList",1,0,0).Select                                                  "无"
	Element_Relation(myiframe0,"自然村人口数量","WebList",1,0,0).Select                            ""
	Element_Relation(myiframe0,"业务品种","WebList",1,0,0).Select                                         Environment("BusinessType")
	Element_Relation(myiframe0,"营销专属方案","WebList",1,0,0).Select                                Environment("MarketingProgram")
	Element_Relation(myiframe0,"入账机构","WebList",1,0,0).Select                                         Environment("AccountEntryOrgan")
	Element_Relation(myiframe0,"城市","WebList",1,0,0).Select                                    left(Environment("AccountEntryOrgan"),2)
	Element_Relation(myiframe0,"还款方式","WebList",1,0,0).Select                                         Environment("RepaymentType")
	Element_Relation(myiframe0,"教育程度","WebList",1,0,0).Select                                         Environment("EducationLevel")
	Element_Relation(myiframe0,"额度是否可循环","WebList",1,0,0).Select                            Environment("IsCycle")
	
	Element(First_Page,"保存","WebElement","html tag","TD",,,1).Click
	Element(First_Page,"信用评估","WebElement","html tag","TD",,,1).Click
	rem--判断近30的有效报告，
	If Left(Dialog_Handle(First_Window,"",60),4)="信用评估" Then
		text=Dialog_Handle(First_Window,"确定",60)
	Else
		Call Dialog_Handle(First_Window,"取消",10)	
		text=Dialog_Handle(First_Window,"确定",60)
	End If
	If Left(text,6)="信用评估成功" Then
		Call LogNote("信用评估成功")
	Else
		rem--出错进入下一个迭代
	End If
	print(text)
	First_Window.Close