rem*进入菜单
Browser("客户管理").Page("客户管理").WebElement("个人客户管理").Click
rem*新增客户
Browser("客户管理").Page("客户管理").Frame("新增按钮框左侧").WebElement("客户新增按钮").Click @@ hightlight id_;_Browser("客户管理").Page("客户管理").Frame("right").WebElement("1x1")_;_script infofile_;_ZIP::ssf1.xml_;_
Browser("客户管理").Window("请输入客户信").Page("客户基本信息").WebList("选择证件类型").select Environment("CertType") @@ hightlight id_;_Browser("客户管理").Window("请输入客户信息 -- 网页对话框").Page("请输入客户信息").WebList("CertType")_;_script infofile_;_ZIP::ssf2.xml_;_
Browser("客户管理").Window("请输入客户信").Page("客户基本信息").WebEdit("证件号码").Set Environment("CertID") @@ hightlight id_;_Browser("客户管理").Window("请输入客户信息 -- 网页对话框").Page("请输入客户信息").WebEdit("CertID")_;_script infofile_;_ZIP::ssf3.xml_;_
Browser("客户管理").Window("请输入客户信").Page("客户基本信息").WebEdit("证件号码确认").set Environment("CertID") @@ hightlight id_;_Browser("客户管理").Window("请输入客户信息 -- 网页对话框").Page("请输入客户信息").WebEdit("CertID1")_;_script infofile_;_ZIP::ssf4.xml_;_
Browser("客户管理").Window("请输入客户信").Page("客户基本信息").WebEdit("客户全称").Set Environment("CustomerName") @@ hightlight id_;_Browser("客户管理").Window("请输入客户信息 -- 网页对话框").Page("请输入客户信息").WebEdit("CustomerName")_;_script infofile_;_ZIP::ssf5.xml_;_
Browser("客户管理").Window("请输入客户信").Page("客户基本信息").WebButton("确认").Click @@ hightlight id_;_Browser("客户管理").Window("请输入客户信息 -- 网页对话框").Page("请输入客户信息").WebButton("确认")_;_script infofile_;_ZIP::ssf6.xml_;_
Browser("客户管理").Dialog("客户新增成功弹出框").WinButton("确定").Click
rem*填写客户信息
rem*判断如果不是身份证，此处字段没有默认值，需要填写
If Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("证件类型（详情页面）").getroproperty("value")<>"身份证" Then
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("性别").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("性别").Select "男性"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebButton("出生年月日").Click @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebButton("...")_;_script infofile_;_ZIP::ssf62.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("选框").WebList("选择年份").Select "1990" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebList("calendarYear")_;_script infofile_;_ZIP::ssf63.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("选框").WebList("选择月份").Select "1" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebList("calendarMonth")_;_script infofile_;_ZIP::ssf64.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("选框").WebElement("日选择按钮").Click
End If @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("calendarHour 3")_;_script infofile_;_ZIP::ssf65.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("最高学历").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("最高学历").Select "研究生"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("最高学位").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("最高学位").Select "硕士"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("社会保险号").Set "社保号"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebButton("省份、直辖市、自治区").Click
Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("frameleft").WebElement("行政区划大类").WaitProperty "visible","true",5
Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("left").Image("gray_arrow").Click @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("left").Image("gray arrow")_;_script infofile_;_ZIP::ssf12.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("left").WebElement("广东省-广州市").Click @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("left").WebElement("广东省-广州市")_;_script infofile_;_ZIP::ssf13.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("frameright").WebElement("行政区划子类").WaitProperty "visible","true",5
Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("left_2").Image("gray_arrow").Click
Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("left_2").WebElement("广东省-广州市-市辖区").Click @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("left 2").WebElement("广东省-广州市-市辖区")_;_script infofile_;_ZIP::ssf15.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("frameright").WebElement("确定").Click @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("frameright").WebElement("1x1")_;_script infofile_;_ZIP::ssf16.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("户籍地址").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("户籍地址").Set "户籍地址" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F15")_;_script infofile_;_ZIP::ssf17.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("政治面貌").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("政治面貌").Select "群众"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("婚姻状况").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("婚姻状况").Select "未婚"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("居住地址").Click @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("居住地址")_;_script infofile_;_ZIP::ssf114.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("居住地址").Set "居住地址"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("居住地邮编").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("居住地邮编").Set "432900" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F21")_;_script infofile_;_ZIP::ssf19.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("住宅电话").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("住宅电话").Set "020-1234567" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F22")_;_script infofile_;_ZIP::ssf20.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("居住状况").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("居住状况").Select "自置"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("手机号码").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("手机号码").Set "18778763542" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F24")_;_script infofile_;_ZIP::ssf21.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("电子邮箱").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("电子邮箱").Set "1551577@qq.com" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F25")_;_script infofile_;_ZIP::ssf22.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("通讯地址").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("通讯地址").Set "通讯地址" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F26")_;_script infofile_;_ZIP::ssf23.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("通讯地址邮编").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("通讯地址邮编").Set "432788" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F27")_;_script infofile_;_ZIP::ssf24.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("职业").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("职业").Select "专业技术人员"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("职务").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("职务").Select "其他"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("职称").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("职称").Select "高级"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("家庭月收入").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("家庭月收入").Set "10,000.00" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F32")_;_script infofile_;_ZIP::ssf25.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("个人年收入").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("个人年收入").Set "100,000.00" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F33")_;_script infofile_;_ZIP::ssf26.xml_;_
If Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("个人类型").GetROProperty("disabled")=0 Then
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("个人类型").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("个人类型").Select "其它"	
End If
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("兴趣爱好").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("兴趣爱好").Set "兴趣爱好" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F35")_;_script infofile_;_ZIP::ssf27.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("单位所属行业").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("单位所属行业").Select "采矿业"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("单位名称").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("单位名称").Set "单位名称" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F38")_;_script infofile_;_ZIP::ssf28.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("单位地址").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("单位地址").Set "单位地址" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F39")_;_script infofile_;_ZIP::ssf29.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("单位邮编").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("单位邮编").Set "432877" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F40")_;_script infofile_;_ZIP::ssf30.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("单位电话").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("单位电话").Set "020-1235464"
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebButton("本单位工作起始时间").Click @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebButton("本单位工作起始时间")_;_script infofile_;_ZIP::ssf66.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("选框").WebList("选择年份").Select "2010" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebList("calendarYear")_;_script infofile_;_ZIP::ssf67.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("选框").WebList("选择月份").Select "1" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebList("calendarMonth")_;_script infofile_;_ZIP::ssf68.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("选框").WebElement("日选择按钮").Click @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("calendarHour 3")_;_script infofile_;_ZIP::ssf69.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("毕业学校").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebEdit("毕业学校").Set "毕业学校" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebEdit("R0F43")_;_script infofile_;_ZIP::ssf34.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("是否异地客户").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("是否异地客户").Select "本市客户"
If Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("是否农户").GetROProperty("disabled")=0 Then
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("是否农户").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").WebList("是否农户").Select "否"	
End If
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").Weblist("是否存量微小客户").Click
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("个人概况填写页面").Weblist("是否存量微小客户").Select "否" @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("1x1 2")_;_script infofile_;_ZIP::ssf98.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("选框").WebElement("保存").Click @@ hightlight id_;_Browser("客户管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("right").WebElement("1x1")_;_script infofile_;_ZIP::ssf35.xml_;_
Browser("客户管理").Window("信贷风险管理系统V7").Close
wait 1
