rem-调试参数
'	Environment("CustomerName")="TEST"
'	Environment("Serialno")="pf2018112600000001"

Browser("合同管理").Page("合同管理").WebElement("登记合同（下拉菜单）").Click
Browser("合同管理").Page("合同管理").Frame("left").WebElement("未登记完成的合同").Click
Browser("合同管理").Page("合同管理").Frame("right").WebElement("登记合同").Click
Set Mypage=Browser("合同管理").Window("请选择所需信息").Page("请选择所需信息")
Call FindSelection(Mypage,Environment("CustomerName"),"0","0","0","0",Environment("Serialno"))