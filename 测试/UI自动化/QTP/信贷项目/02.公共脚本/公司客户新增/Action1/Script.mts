
Environment("CustomerType")="公司客户"
Environment("CustomerName")="小茗同学"
Environment("CertID")="66303925-6"
Environment("SocialCreditID")="000000006630392560"
rem*3、客户信息填写
With Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
	.WebEdit("工商营业执照").WaitProperty "visible","true",3
	.WebEdit("工商营业执照").Click
	.WebEdit("工商营业执照").Set  "12345678"&replace(environment("CertID"),"-","")&"9" ''共18位，第1位：阿拉伯数字或大写字母（部分字母不能使用），第2位：机构类别；第3~8位：登记管理机关行政区划码；第9~17：组织机构代码；第18位：校验码
	.WebButton("营业执照登记日").Click
		With Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right")
		.WebList("calendarYear").Select "2001"
		.WebList("calendarMonth").Select "1"
		.WebElement("innertext:=1","html tag:=TD").Click
		End With
	.WebButton("营业执照到期日").Click
		With Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right")
		.WebList("calendarYear").Select "2060"
		.WebList("calendarMonth").Select "1"
		.WebElement("innertext:=1","html tag:=TD").Click
		End With
	.WebList("控股类型").Click
	.WebList("控股类型").Select "国有绝对控股"
	.WebButton("企业类型").Click
		With Browser("客户管理").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
			.Frame("left").WebElement("选择信息列表").WaitProperty "visible","true",5
			.Frame("left").Image("gray_arrow").Click
			.Frame("left").WebElement("国有企业").Click
			.WebButton("确认").Click
		End With
	.WebButton("法定代表人").Click
		With Browser("客户管理").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
			.Frame("myiframe0").WebEdit("客户编号").Click
			.WebButton("确认").Click
		End With
	.WebButton("国标行业分类").Click
		Set  object=Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
		Call IndustrySelection(object,"制造业","食品制造业","其他食品制造","营养食品制造")
	.WebList("我行行业分类").Click
	.WebList("我行行业分类").Select "钢贸"
	.WebEdit("经营范围").Click
	.WebEdit("经营范围").Set "经营范围"
	.WebEdit("职工人数").Click
	.WebEdit("职工人数").Set "100"
	.WebList("企业规模(我行口径)").Click
	.WebList("企业规模(我行口径)").Select "微型企业"
	.WebButton("企业成立日期").Click
		With Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right")
			.WebList("calendarYear").Select "2060"
			.WebList("calendarMonth").Select "1"
			.WebElement("innertext:=1","html tag:=TD").Click
		End With
	.WebEdit("注册资本").Click
	.WebEdit("注册资本").Set "1000000.00"
	.WebEdit("注册地址").Click
	.WebEdit("注册地址").Set "注册地址"
	.WebEdit("实收资本").Click
	.WebEdit("实收资本").Set "1000000.00"
	.WebEdit("上年末销售额").Click
	.WebEdit("上年末销售额").Set "1000000.00"
	.WebEdit("上年末资产总额").Click
	.WebEdit("上年末资产总额").Set "3000000.00"
	.WebButton("企业规模（人行口径）").Click
	Browser("客户管理").Window("信贷风险管理系统V7").Dialog("来自网页的消息").WinButton("确定").Click
	.WebList("是否小微客户").Click
	.WebList("是否小微客户").Select "否"
	.WebButton("省份、直辖市、自治区").Click
	Set Object_Child=Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
	Call AddressSelection(Object_Child,"广东省","广州市","市辖区")
	.WebEdit("借款人通讯地址").Click
	.WebEdit("借款人通讯地址").Set "借款人通讯地址"
	.WebEdit("邮政编码").Click
	.WebEdit("邮政编码").Set "123456"
	.WebEdit("公司E-Mail").Click
	.WebEdit("公司E-Mail").Set "12345@qq.com"
	.WebEdit("行政区划代码").Click
	.WebEdit("行政区划代码").Set "123456"
	.WebEdit("联系电话").Click
	.WebEdit("联系电话").Set "020-5654536"
	.WebEdit("税务登记证(国税)").Click
	.WebEdit("税务登记证(国税)").Set "国税-123456"
	.WebEdit("税务登记证(地税)").Click
	.WebEdit("税务登记证(地税)").Set "地税-123456"
	.WebList("财务报表类型").Click
	.WebList("财务报表类型").Select "通用财务报表"
	.WebList("有无进出口经营权").Click
	.WebList("有无进出口经营权").Select "有"
	.WebList("是否上市公司").Click
	.WebList("是否上市公司").Select "是"
	.WebList("是否战略客户").Click
	.WebList("是否战略客户").Select "是"
	.WebList("是否来料加工").Click
	.WebList("是否来料加工").Select "是"
	''关闭掉所有已打开的号码生成器
	Set Desc=Description.Create()
	Desc("MicClass").Value="Window"
	Desc("regexpwndtitle").Value="号码生成器"
	Set le=Desktop.ChildObjects(Desc)
	m=le.Count
	For i = 0 To m-1 Step 1
		le(i).Close
	Next
	''打开号码生成器
	SystemUtil.Run Pathfinder.Locate("..\..\基础脚本库\公司客户新增\号码生成器\MakeNumber.exe"),"",PathFinder.Locate("..\..\基础脚本库\公司客户新增\号码生成器"),"open"'打开号码生成器，需要到脚本目录下添加号码生成器工具
	Window("号码生成器").InsightObject("InsightObject").Click
	Window("号码生成器").WinObject("生成").Click
	cardid=Window("号码生成器").WinObject("TEdit").GetROProperty("text")
	Window("号码生成器").Close
	.WebEdit("中证码").Click
	.WebEdit("中证码").Set cardid
	.WebEdit("与我行建立信贷关系时间").Click
	.WebEdit("与我行建立信贷关系时间").Set "2001/01/01"
	.WebButton("信用等级评估模板名称").Click
		Browser("客户管理").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息").Frame("left").WebElement("房地产业信用等级评估表").Click
		Browser("客户管理").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息").WebButton("确认").Click
	.WebList("是否异地客户").Click
	.WebList("是否异地客户").Select "本市客户"
	.WebList("是否农业产业化龙头企业").Click
	.WebList("是否农业产业化龙头企业").Select "是"
	.WebList("涉农分类标志").Click
	.WebList("涉农分类标志").Select "农村企业"
	.WebList("是否政府融资平台").Click
	.WebList("是否政府融资平台").Select "是"
	.WebList("是否发改委受限企业").Click
	.WebList("是否发改委受限企业").Select "鼓励"
	.WebList("是否节能减排企业").Click
	.WebList("是否节能减排企业").Select "是"
	.WebList("是否绿色企业").Click
	.WebList("是否绿色企业").Select "否"
	.WebList("企业环境信用评定等级").Click
	.WebList("企业环境信用评定等级").Select "其他企业"
	Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("保存").Click
End With