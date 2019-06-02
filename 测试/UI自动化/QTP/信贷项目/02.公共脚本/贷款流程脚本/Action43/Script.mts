'rem-调试参数
'	Environment("CustomerName")="测试修改"
'	Environment("Serialno")="ht2018092100000004"

Browser("合同管理").Page("合同管理").WebElement("登记合同（下拉菜单）").Click
Browser("合同管理").Page("合同管理").Frame("left").WebElement("未登记完成的合同").Click
Browser("合同管理").Page("合同管理").Frame("right").WebElement("登记合同").Click
Set Mypage=Browser("合同管理").Window("请选择所需信息").Page("请选择所需信息")
Call FindSelection(Mypage,Environment("CustomerName"),"0","0","0","0",Environment("Serialno"))
Browser("合同管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0").WebButton("业务品种").Click
Set Mypage_child=Browser("合同管理").Window("信贷风险管理系统V7").Window("请选择所需信息").Page("请选择所需信息")
Call ItemSelection(Mypage_child,"0","流动资金贷款","短期流动资金贷款")
Browser("合同管理").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("ObjectList").WebElement("确认").Click