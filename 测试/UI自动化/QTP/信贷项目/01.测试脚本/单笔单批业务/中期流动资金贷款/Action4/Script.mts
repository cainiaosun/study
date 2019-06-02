'environment("customertype")="公司客户"
'environment("customername")="TESTB0000531530"
'environment("certid")="45624541-X"
'environment("businesstype")="短期流动资金贷款"
rem*打开单笔单批申请菜单
Set Page1=browser("单笔单批业务申请").page("单笔单批业务申请")
Page1.webelement("单笔单批业务申请").Click
Page1.Frame("right").WebElement("新增申请").Click'点击新增申请按钮
Set Page2=browser("单笔单批业务申请").window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
Page2.Frame("新增弹框填写页").WebList("客户类型").Select environment("CustomerType")'rem选择客户类型
Page2.Frame("按钮").WebElement("下一步").Click'选择客户类型后点击“下一步”
Page2.Frame("选择").WebButton("客户编号").WaitProperty "visible","ture",3000'rem*等待下一页面的“客户编号字段出现“
'////////////////////////////////
Page2.Frame("选择").WebButton("客户编号").Click'rem*点击客户编号进入选择客户
Set Page3=browser("单笔单批业务申请").window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
Page3.frame("查询条件(上层)").link("查询条件").Click'rem*点击查询展开按钮
Page3.frame("查询条件(上层)").WebEdit("客户名称").Set environment("CustomerName")'rem*输入客户姓名
Page3.frame("查询条件(上层)").WebEdit("证件号码").Set environment("CertID")'rem*输入客户证件号码
Page3.frame("查询条件(上层)").WebButton("查询").Click'rem*点击查询
Page3.Frame("客户选择列表").WebEdit("选择的客户").WaitProperty "visible",ture,8000'rem*等待客户查询结果
Page3.Frame("客户选择列表").WebEdit("选择的客户").Click'rem*选择客户
Page3.WebButton("确认").Click'rem*点击确认
Page2.Frame("选择").WebButton("业务品种").Click'rem*点击业务品种按钮
Set Page3=browser("单笔单批业务申请").window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
'Select Case environment("customertype")'rem*此处是一个展开操作，但是进入界面后已展开，可省略
'	Case "公司客户"
'	Page3.Frame("left").Image("授信额度").Click
'End Select
Page3.Frame("left").Image("流动资金贷款").Click'rem*展开流动资金贷款目录
Page3.Frame("left").WebElement("innertext:="&environment("BusinessType"),"html tag:=A").Click'rem*选择业务
Page3.WebButton("确认").Click'rem*选择业务品种完成点击确定
Page2.Frame("ObjectList").WebElement("确认").Click'新增信息填写完成，点击确认
