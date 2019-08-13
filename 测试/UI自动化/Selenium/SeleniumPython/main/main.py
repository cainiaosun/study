import os,sys,time,shutil,multiprocessing
from selenium.webdriver.common.by import By
sys.path.append("../")
from base.mykeyword import *
from base import method as F
from base.get_config import MyConfig
from base.datatable import DataTable
from base.environment import Environment
from base import running_folder as CreateRunningFolder
from base.getElement import getElement
from util.send_email import SendEmail

def environment_ini(testsuite="../case/testcase.xls"):
	pid=multiprocessing.current_process().pid#获取进程pid
	case_name=os.path.basename(testsuite).split(".")[0]#获取案例名称
	rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))#时间字符串
	path_running=MyConfig("project","project_path").value+MyConfig("project","data_path").value#获取运行数据存放主目录
	path_running=path_running+"/"+case_name+"-"+str(rq)+"-pid-"+str(pid)#线程数据的目录
	MyConfig().set("running",str(pid),path_running)#写每个进程存放数据的子目录路径到配置文件
	CreateRunningFolder.folder_create(path_running)#为每个线程新建运行的数据存放子目录
	DataTable.load(testsuite)#加载数据表


def run_test(row,testsuite=None,elementsdata=None,reload=False):
	'''
	执行一条案例，放在执行测试集中调用
	参数：
		--row：案例数据所在行
		--testsuite：案例集,reload为真，需从案例数据表中初始数据
		--elementsdata：页面元素集，reload为真，需从页面元素数据表中读取
	'''
	if reload:
		environment_ini(testsuite)
		F.driver=F.creat_driver()
		F.maximize()
		ele=getElement().get(elementsdata)
	else:
		ele=elementsdata
	Environment("row").set(row)#设置执行行
	Case_ID=DataTable("Case_ID").value()
	execute_status=DataTable("执行状态")
	execute_status.set("失败")#设置为失败，通过后重置状态为成功
	element=DataTable("操作元素").value()
	if element:
		element=ele[DataTable("操作元素").value()]
	operate=DataTable("操作").value()
	value=DataTable("操作值").value() 
	expect_element=DataTable("预期元素").value()
	if expect_element:
		expect_element=ele[DataTable("预期元素").value()]
	expect_operate=DataTable("预期操作").value()
	expect_value=DataTable("预期操作值").value()
	expect_result=DataTable("预期结果").value()
	compare_type=DataTable("结果比较方式").value()
	if DataTable("是否执行").value()=="是":
		test_operate(element,operate,value)
		result=test_expect(expect_element,expect_operate,expect_value)
		status=write_result(expect_result,result,compare_type,execute_status)	
	else:
		execute_status.set("跳过")
	rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))#时间字符串
	F.save_screenshot("../picture"+"/"+rq+"-"+Case_ID+".png")
	return 0

def run_testsuite():
	environment_ini()
	ele=getElement().get("../case/page.xls")
	F.driver=F.creat_driver()
	F.maximize()
	rows=DataTable("Case_ID").rows()
	for i in range(1,rows):
		run_test(row=i,elementsdata=ele)

	#邮件内容
	col_values=DataTable().col_values("执行状态")
	adopt=col_values.count("通过")
	fail=col_values.count("失败")
	skip=col_values.count("跳过")
	shutil.copyfile(Environment("case_path").value,"../case/result_testcase.xls")
	user_list=["1396677105@qq.com"]
	title="Jenkins登录测试"
	content="案例集总数："+str(rows-1)+"条；本次执行数："+str(adopt+fail+skip)+"条；通过："\
		+str(adopt)+"条；失败："+str(fail)+"条；跳过："+str(skip)+"条。"
	print(content)
	SendEmail().send_email(user_list,title,content)


"""案例执行入口：为每个设备开辟进程，并启动进程"""
def run_main():
	"""启动服务"""
	# Log().info("启动服务！")
	# server.Server().main()
	"""添加并启动进程"""
	processes = []
	for i in range(1):
		#添加进程
		p=multiprocessing.Process(target=run_testsuite)
		processes.append(p)
	for p in processes:
		#启动进程
		# Log().info("启动进程："+str(p))
		p.start()

if  __name__=="__main__":
	run_main()
	#run_test(1,"../case/testcase.xls","../case/page.xls",True)