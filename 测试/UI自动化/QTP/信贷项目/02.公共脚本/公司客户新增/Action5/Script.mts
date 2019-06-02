'LoadFunctionLibrary "C:\Users\922004\Desktop\孙洪斌\学习文档集\QTP脚本集\函数库\ActionLibrary.qfl"
'LoadFunctionLibrary "C:\Users\922004\Desktop\孙洪斌\学习文档集\QTP脚本集\函数库\CreditLibrary.qfl"
'DataTable.Import "C:\\Users\\922004\\Desktop\\孙洪斌\\学习文档集\\信贷脚本\\导入数据\\公司客户.xlsx"
'Environment.Value("CustomerType")=DataTable("客户类型",1)
'Environment.Value("CustomerName")=DataTable("客户名称",1)
'Environment.Value("CertID")=DataTable("组织机构号码",1)
'Environment.Value("SocialCreditID")=DataTable("社会统一信用代码",1)

rem*1、进入菜单
Browser("客户管理").Page("客户管理").WebElement("公司客户管理").Click
'rem*2、新增客户
Browser("客户管理").Page("客户管理").Frame("right").WebElement("新增").Click
With Browser("客户管理").Window("请输入客户信息 -- 网页对话框").Page("请输入客户信息")
	.WebList("选择客户类型").Select "法人企业"
	.WebEdit("证件号码").Set Environment("CertID")
	.WebEdit("证件号码确认").Set Environment("CertID")
	.WebEdit("统一社会信用代码").Set Environment("SocialCreditID")
	.WebEdit("统一社会信用代码确认").Set Environment("SocialCreditID")
	.WebEdit("客户全称").Set Environment("CustomerName")
	.WebButton("确认").Click
Browser("客户管理").Dialog("来自网页的消息").WinButton("确定").Click
End With