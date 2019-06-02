rem--调试数据
'	Environment("FileName")="信用速贷流程"rem--案例文件名称
'	Environment("PublicScript")="信用速贷（build）"rem--公共脚本名称
i=DataTable.GetCurrentRow
rem*DataTable.GetCurrentRow获取的首次迭代值因还未导入数据表，如果默认的数据表是空的，则会是0，非空时1
rem*第一次迭代的时候加载函数库和数据表
If i=0 or i=1 Then
	rem--加载函数库
	cFolder=Environment("TestDir")
	List=Array("Public","LoginAndQuit","Element","Repository","Log","ItemSelection","Dialog"_
	,"Browser","PopBox","Recovery","DataTable")
	For Each Library in List
		LibraryPath=split(cFolder,"信贷项目")(0)&"信贷项目\04.函数库"&"/"&Library&".qfl"
		LoadFunctionLibrary LibraryPath
		Libraries=Libraries&"、"&Library
	Next
	Call LogNote("已导入的函数库："&Right(Libraries,Len(Libraries)-1))
	Print("已导入的函数库："&Right(Libraries,Len(Libraries)-1))
	rem*导入数据表
	filename=Environment("FileName")rem--输入需要导入的Excel文件名称
	DataTablePath=split(cFolder,"信贷项目")(0)&"信贷项目/03.导入案例"&"/"&filename&".xlsx"
	DataTable.Import  DataTablePath
	Print("案例路径："&DataTablePath)
	Call LogNote("案例路径："&DataTablePath)
	rem*使用的测试脚本路径(上级目录)
	Environment("TestPath")=split(cFolder,"信贷项目")(0)&"信贷项目/01.测试脚本"
	rem*使用的公共脚本路径
	Environment("Path")=split(cFolder,"信贷项目")(0)&"信贷项目/02.公共脚本/"&Environment("PublicScript")
	Call LogNote("公共脚本路径："&Environment("Path"))
	Print("公共脚本路径："&Environment("Path"))
	rem*恢复场景网址参数
	Environment("URL")="http://11.8.121.150:7001/GDNY_CZ/logon.html"
End If
rem--初始脚本部分数据
	Environment("TestCaseNum")=DataTable("案例编号",1)
	Environment("Module")=DataTable("所属模块",1)
	Environment("TestClass")=DataTable("脚本类",1)
	Environment("ScriptName")=DataTable("脚本名称",1)
rem-根据脚本模块、测试类、脚本名称动态执行对应脚本
	Print("执行第"&i&"条："&Environment("ScriptName"))
	Call LogNote("执行第"&i&"条："&Environment("ScriptName"))
	ScriptPath=Environment("TestPath")&"/"&Environment("Module")&"/"&Environment("TestClass")
	Print("脚本路径："&ScriptPath)
	Call LogNote("脚本路径："&ScriptPath)
	LoadAndRunAction ScriptPath,Environment("ScriptName")
	Print("执行第"&i&"条完成："&Environment("ScriptName"))
	Call LogNote("执行第"&i&"条完成："&Environment("ScriptName"))
	
	
	
	
