import sys,multiprocessing
sys.path.append("../")
from base import method as F
from base.get_config import MyConfig
from base.datatable import DataTable
from base.environment import Environment

def test_operate(element=None,operate=None,value=None):
	"""
	根据关键字，执行对应操作
	"""
	if operate:
		if element:
			if value:
				getattr(F.Element(element),operate)(value)
			else:
				getattr(F.Element(element),operate)()
		else:
			if value:
				getattr(F,operate)(value)
			else:
				getattr(F,operate)()

def test_expect(expect_element=None,expect_operate=None,expect_value=None):
	pid=multiprocessing.current_process().pid
	# print("调用进程是：",pid)
	# print("元素是：",expect_element)
	#执行预期操作
	# # print("获取预期结果")
	# # print(expect_element,expect_operate,expect_value)
	if expect_operate:
		if expect_element:
			if expect_value:
				result=getattr(F.Element(expect_element),expect_operate)(expect_value)
			else:
				result=getattr(F.Element(expect_element),expect_operate)()
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
	# # print("写执行结果")
	run_status=None
	result=str(result)
	if compare_type=="等于":
		# # print("等于分支！",type(expect_result),type(result))
		# # print("va1",expect_result,"va2",result)
		if expect_result==result:
			run_status="通过"
			# # print(run_status)
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