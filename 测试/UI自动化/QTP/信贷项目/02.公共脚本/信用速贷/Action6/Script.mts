'Environment.Value("Serialno")="UPL2018042500000014"
'获取任务
Browser("面签处理管理").Page("面签处理管理").WebElement("面签处理").Click
Browser("面签处理管理").Page("面签处理管理").Frame("myiframe0").WebEdit("value:="&Environment.Value("Serialno"),"type:=text").Click
Browser("面签处理管理").Page("面签处理管理").Frame("right").WebElement("获取面签").Click
'处理
Browser("面签处理管理").Page("面签处理管理").Frame("myiframe0").WebEdit("value:="&Environment.Value("Serialno"),"type:=text").Click
Browser("面签处理管理").Page("面签处理管理").Frame("right").WebElement("处理面签").Click
