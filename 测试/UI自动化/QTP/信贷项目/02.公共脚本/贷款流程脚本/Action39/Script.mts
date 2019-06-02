rem-调试参数
'	Environment("CustomerName")="TESTB0000531530"
'	Environment("Serialno")="pf2019011700000001"

Browser("合同管理").Page("合同管理").WebElement("登记合同（下拉菜单）").Click
Browser("合同管理").Page("合同管理").Frame("left").WebElement("未登记完成的额度协议").Click
Browser("合同管理").Page("合同管理").Frame("right").WebElement("登记协议").Click
Set Mypage=Browser("合同管理").Window("请选择所需信息").Page("请选择所需信息")
Call FindSelection(Mypage,Environment("CustomerName"),"0","0","0","0",Environment("Serialno"))
