Print("工作信息，时点："&time)
t=timer
With Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
	.WebEdit("单位名称").Click
	.WebEdit("单位名称").Set "优良单位"
	.WebEdit("部门").Click
	.WebEdit("部门").Set "部门"
	.WebList("单位性质").Click
	.WebList("单位性质").Select "国有"
	.WebList("单位所属行业").Click
	.WebList("单位所属行业").Select "采矿业"
	.WebList("职业").Click
	.WebList("职业").Select "专业技术人员"
	.WebList("职务类型").Click
	.WebList("职务类型").Select "部门负责人或处级"
	.WebEdit("现单位工作年限").Click
	.WebEdit("现单位工作年限").Set "10"
	.WebEdit("企业成立年限").Click
	.WebEdit("企业成立年限").Set "10"
	'这一部分是"省份、直辖市、自治区"的录入
	With Browser("信用速贷申请").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7").Frame("myiframe0")
		If .WebEdit("省份、直辖市、自治区").GetROProperty("value")="" Then
			.WebButton("省份、直辖市、自治区").Click
			Set Object=Browser("信用速贷申请").Window("信贷风险管理系统V7").Window("信贷风险管理系统V7").Page("信贷风险管理系统V7")
			Call AddressSelection(Object)
		End If
	End with
	.WebEdit("单位地址").Click
	.WebEdit("单位地址").Set "单位地址"
	.WebEdit("单位邮编").Click
	.WebEdit("单位邮编").Set "123456"
	.WebEdit("区号").Click
	.WebEdit("区号").Set "020"
	.WebEdit("号码").Click
	.WebEdit("号码").Set "2765387"
End With
Print("工作信息完成，用时："&timer-t&"s；时点："&time&"。")