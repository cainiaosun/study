rem-t调试数据
'	Environment("EmployType")="自雇人士客户"
'	Environment("CellphoneNumber")= "13499880350"
'	Environment("MaritalStatus")="未婚"rem-婚姻状态
'	Environment("HouseholdRegister")="本地"rem-户口所在地
'	Environment("EducationLevel")="本科"rem-教育程度
'	Environment("Sex")="男性"rem-性别
	
rem-加载共享对象库
path="C:\Users\922004\Desktop\孙洪斌\学习文档集\信贷项目\08.公共对象库\信用速贷_01.tsr"
Call RepositoriesAdd(path)

With Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")
	Set Browser_0=Browser("主窗口（浏览器）")
	Set First_Window=Browser("主窗口（浏览器）").Window("一级窗口")rem-录入弹窗
	Set First_Page=Browser("主窗口（浏览器）").Window("一级窗口").Page("一级窗口Page页")rem-录入Page页面
	Set Second_Page=Browser("主窗口（浏览器）").Window("一级窗口").Window("二级窗口").Page("二级窗口Page页")rem-弹出窗口Page页面
	Set First_myiframe0_0=.Frame("myiframe0_0")rem-面签信息填写Frame页面
	Set First_right=.Frame("right_0")rem-面签信息保存按钮所在Frame页面
	Set First_myiframe0_1=.Frame("myiframe0_1")rem-贷款相关信息填写Frame页面
	Set First_DetailFrame_0=.Frame("DetailFrame_0")rem-各个页面切换标签所在页面，如：客户详情、贷款信息
	Set TabContentFrame=.Frame("TabContentFrame")rem-各个页面切换标签所在页面，如：主借款人、其他联系人
	Set First_DetailFrame_1=.Frame("DetailFrame_1")rem-贷款相关信息保存、更新核心客户编号按钮所在Frame页面
End With
	rem--基本信息
	Element(First_DetailFrame_1,"更新核心客户编号","WebElement","html tag","TD",,,1).Click
	Call Dialog_Handle(First_Window,"确定",60)	
	Call Dialog_Handle(First_Window,"确定",10)	
	Element_Relation(First_myiframe0_1,"核心客户号","WebEdit",0,0,0).highlight
	Environment("ECIFID")=Element_Relation(First_myiframe0_1,"核心客户号","WebEdit",0,0,0).GetRoproperty("value")   
	Print("核心客户号："&Environment("ECIFID"))
	Element_Relation(First_myiframe0_1,"性别","WebList",1,0,0).Select                                     Environment("Sex")
	Element_Relation(First_myiframe0_1,"婚姻状况","WebList",1,0,0).Select                            Environment("MaritalStatus")
	Element_Relation(First_myiframe0_1,"身份证发证机关所在地","WebEdit",1,0,0).Set        "发证机关地址"
	Element_Relation(First_myiframe0_1,"教育程度","WebList",1,0,0).Select                            Environment("EducationLevel")
	Element_Relation(First_myiframe0_1,"手机","WebEdit",1,0,0).Set                                           Environment("CellphoneNumber")
	Environment("CellphoneNumber")=Element_Relation(First_myiframe0_1,"手机","WebEdit",1,0,0).GetRoproperty("value")
	Select Case Environment.Value("EmployType")
		Case "自雇人士客户"
			Element_Relation(First_myiframe0_1,"个人类型","WebList",1,0,0).Select                            "小微企业法人代表"
		Case else
			Element_Relation(First_myiframe0_1,"个人类型","WebList",1,0,0).Select                           "其它"
	End Select
	If Element_Relation(First_myiframe0_1,"省份、直辖市、自治区","WebEdit",1,0,0).GetRoproperty("value")="" Then
		Element_Relation(First_myiframe0_1,"省份、直辖市、自治区","WebButton",1,0,0).Click
		Call AddressSelection(Second_Page,"广东省","广州市","市辖区")
	End If
	Element_Relation(First_myiframe0_1,"居住地址","WebEdit",1,0,0).Set                                            "居住地址"
	Element_Relation(First_myiframe0_1,"住宅邮编","WebEdit",1,0,0).Set                                            "123456"
	Element_Relation(First_myiframe0_1,"工作关系是否在我行经办分部所在地","WebList",1,0,0).Select "是"
	Element_Relation(First_myiframe0_1,"是否农户","WebList",1,0,0).Select                                       "否"
	rem-工作信息
	Element_Relation(First_myiframe0_1,"单位名称","WebEdit",1,0,0).Set                                                     "优良单位"
	Element_Relation(First_myiframe0_1,"部门","WebEdit",1,0,0).Set                                                              "部门"
	Element_Relation(First_myiframe0_1,"单位性质","WebList",1,0,0).Select                                               "国有"
	Element_Relation(First_myiframe0_1,"单位所属行业","WebList",1,0,0).Select                                       "采矿业"
	Element_Relation(First_myiframe0_1,"职业","WebList",1,0,0).Select                                                        "专业技术人员"
	Element_Relation(First_myiframe0_1,"职务类型","WebList",1,0,0).Select                                               "部门负责人或处级"
	Element_Relation(First_myiframe0_1,"现单位工作年限","WebEdit",1,0,0).Set                                        "10"
	Element_Relation(First_myiframe0_1,"企业成立年限","WebEdit",1,0,0).Set                                            "10"
	If Element_Relation(First_myiframe0_1,"省份、直辖市、自治区","WebEdit",1,1,0).GetRoproperty("value")="" Then
		Element_Relation(First_myiframe0_1,"省份、直辖市、自治区","WebButton",1,1,0).Click
		Call AddressSelection(Second_Page,"广东省","广州市","市辖区")
	End If
	Element_Relation(First_myiframe0_1,"单位地址","WebEdit",1,0,0).Set                                                    "单位地址"
	Element_Relation(First_myiframe0_1,"单位邮编","WebEdit",1,0,0).Set                                                    "123456" 
	Element_Relation(First_myiframe0_1,"区号","WebEdit",1,1,0).Set                                                             "020" 
	Element_Relation(First_myiframe0_1,"号码","WebEdit",1,1,0).Set                                                             "2765387" 
	rem-综合财务信息
	Element_Relation(First_myiframe0_1,"月收入","WebEdit",1,0,0).Set                                    "2765387" 
	Element_Relation(First_myiframe0_1,"家庭本地房产","WebList",1,0,0).Select                 "有"
	Element_Relation(First_myiframe0_1,"居住状况","WebList",1,0,0).Select                          "自置"
	Element_Relation(First_myiframe0_1,"户口所在地","WebList",1,0,0).Select                      Environment("HouseholdRegister")
	Element(First_DetailFrame_1,"保存","WebElement","html tag","TD",,,1).Click
	Call IsFinish(First_myiframe0_1)
