import sys,time,shutil
from selenium.webdriver.common.by import By
sys.path.append("../")
from base import method as F
from base.datatable import DataTable
from base.environment import Environment
from base import running_folder as CreateRunningFolder
from util.send_email import SendEmail
def test_operate(element=None,operate=None,value=None):
	"""
	根据关键字，执行对应
	"""
	if operate:
		if element:
			if value:
				getattr(F.Element(eval(element)),operate)(value)
			else:
				getattr(F.Element(eval(element)),operate)()
		else:
			if value:
				getattr(F,operate)(value)
			else:
				getattr(F,operate)()

def test_expect(expect_element=None,expect_operate=None,expect_value=None):
	#执行预期操作
	# print("获取预期结果")
	# print(expect_element,expect_operate,expect_value)
	if expect_operate:
		if expect_element:
			if expect_value:
				result=getattr(F.Element(eval(expect_element)),expect_operate)(expect_value)
			else:
				result=getattr(F.Element(eval(expect_element)),expect_operate)()
		else:
			if expect_value:
				result=getattr(F,expect_operate)(expect_value)
			else:
				result=getattr(F,expect_operate)()
	else:
		result=""
	DataTable("实际结果").set(str(result))
	return str(result)

def write_result(expect_result=None,result=None,compare_type=None,execute_status=None):
	#比较结果，写执行状态
	# print("写执行结果")
	run_status=None
	result=str(result)
	if compare_type=="等于":
		# print("等于分支！",type(expect_result),type(result))
		# print("va1",expect_result,"va2",result)
		if expect_result==result:
			run_status="通过"
			# print(run_status)
	elif compare_type=="小于":
		if expect_result<result:
			run_status="通过"
	elif compare_type=="大于":
		if expect_result>result:
			run_status="通过"
	elif compare_type=="包含于":
		if expect_result in result:
			run_status="通过"
	elif compare_type=="被包含":
		if result in expect_result:
			run_status="通过"
	if run_status:
		execute_status.set("通过")
		return "通过"
	else:
		execute_status.set("失败")
		return "失败"

def run_test():
	DataTable.load("../case/testcase.xls")
	adopt=0#通过数
	fail=0#失败数
	skip=0#跳过数
	for i in range(1,DataTable("Case_ID").rows()):
		Environment("row").set(i)#设置执行行
		Case_ID=DataTable("Case_ID").value()
		execute_status=DataTable("执行状态")
		execute_status.set("失败")#先设置为失败，后面通过以后修改状态为成功
		element=DataTable("操作元素").value()
		operate=DataTable("操作").value()
		value=DataTable("操作值").value() 
		expect_element=DataTable("预期元素").value()
		expect_operate=DataTable("预期操作").value()
		expect_value=DataTable("预期操作值").value()
		expect_result=DataTable("预期结果").value()
		compare_type=DataTable("结果比较方式").value()
		if DataTable("是否执行").value()=="是":
			fail=fail+1
			test_operate(element,operate,value)
			result=test_expect(expect_element,expect_operate,expect_value)
			# print("结果是：",result)
			# print("预期结果是：",expect_result) 
			status=write_result(expect_result,result,compare_type,execute_status)
			if status=="通过":
				fail=fail-1
				adopt=adopt+1
		else:
			execute_status.set("跳过")
			skip=skip+1
		F.save_screenshot("../picture"+"/"+Case_ID+".png")
	print("本次共执行案例",adopt+fail+skip,";通过：",adopt,";失败：",fail,";跳过：",skip,"。")
	shutil.copyfile(Environment("case_path").value,"../case/result_testcase.xls")
	user_list=["1396677105@qq.com"]
	title="Jenkins登录测试"
	content="本次执行案例总数："+str(adopt+fail+skip)+"  通过："+str(adopt)+"  失败："+str(fail)+"  跳过："+str(skip)+"。"
	SendEmail().send_email(user_list,title,content)

if  __name__=="__main__":
	url="http://localhost:8080/"
	用户名输入框=("id","j_username")
	密码输入框=("name","j_password")
	登录按钮=("xpath","/html/body/div/div/form/div[3]/input")
	注销按钮=("xpath","/html/body/div[2]/div[1]/div[2]/span/a[2]/b")
	F.driver=F.creat_driver()
	F.maximize()
	run_test()