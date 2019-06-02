import os,sys,time,unittest,threading,multiprocessing
sys.path.append("..")
from util import HTMLTestRunner
from util import server
from util.write_log import Log
from unittest_main import mukewang
import running_folder as CreateRunningFolder
import case_generate as GenerateCase#生成unittest案例脚本模块
from util.write_user_command import WriteUserCommand as WC
from util.write_environment import Environment
from util.case_excel_deal import DataTable
"""
有待参数化解决的问题：
	title:报告标题
	description：报告描述
	filename：报告路径和名称
	OperaExcel().get_rows()：案例个数
"""

"""
	--get_suite():添加unittest测试集
	--run_main():为每个检测到的设备启动一个appium进程服务
"""

def auto_environment(casepath):
	# pid=multiprocessing.current_process().pid
	# Log().error("进程PID"+str(pid))
	#temppath=CreateRunningFolder.folder_clear()
	# temppath=CreateRunningFolder.folder_create(casepath)#为当前运行测试套件创建一个临时的运行文件夹，存放运行案例、运行参数、自动生成的测试脚本
	# temppath=os.path.abspath(temppath)
	# casefile=temppath+"/runningcase.xls"
	# Environment(path=temppath).add("case_path",casefile)#将运行案例写入环境变量中，后面读取使用
	# Environment(path=temppath).add("sheet",0)#将sheet写入环境变量中，默认使用第一个sheet页的内容
	# Environment(path=temppath).add("row",1)#将row写入环境变量中，默认从数据表的第一行读数
	# DataTable.load(casepath,temppath)	
	# GenerateCase.GenerateCase(temppath)#生成unittest案例脚本
	# sys.path.append(temppath)#添加创建的临时目录到环境变量，以使得可以找到临时生成的测试脚本文件case.py
	# from autocase import AutoCase
	pass

#测试套件，获取测试集，并运行
def get_suite(i,casepath,title='title-测试报告',description='用例执行情况：'):	
	auto_environment(casepath)#创建线程运行环境

	temppath=CreateRunningFolder.folder_create(casepath)#为当前运行测试套件创建一个临时的运行文件夹，存放运行案例、运行参数、自动生成的测试脚本
	temppath=os.path.abspath(temppath)
	casefile=temppath+"/runningcase.xls"
	Environment(path=temppath).add("case_path",casefile)#将运行案例写入环境变量中，后面读取使用
	Environment(path=temppath).add("sheet",0)#将sheet写入环境变量中，默认使用第一个sheet页的内容
	Environment(path=temppath).add("row",1)#将row写入环境变量中，默认从数据表的第一行读数
	DataTable.load(casepath,temppath)	
	GenerateCase.GenerateCase(temppath)#生成unittest案例脚本
	sys.path.append(temppath)#添加创建的临时目录到环境变量，以使得可以找到临时生成的测试脚本文件case.py
	from autocase import AutoCase

	suite = unittest.TestSuite()#获取套件
	Log().info("添加案例！")
	#for j in range(1,OperaExcel().get_rows()):
	for j in range(1,3):
		if True==True:
			while len(str(j))<5:
				j="0"+str(j)
			#print("suite.addTest(mukewang('test_"+j+"',parame=i))")
			eval("suite.addTest(AutoCase('test_"+j+"',parame=i))")
	#runner=unittest.TextTestRunner()#
	filename = "../report/report"+str(1)+".html"
	with open(filename, 'wb') as fp:        
		# 定义测试报告        
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title, description=description)        
		# 运行测试用例        
		runner.run(suite)#执行套件       
		# 关闭测试报告        
		#fp.close()

"""案例执行入口：为每个设备开辟进程，并启动进程"""
def run_main(casepath):
	"""启动服务"""
	Log().info("启动服务！")
	server.Server().main()
	"""添加并启动进程"""
	processes = []
	device_list_len=len(server.Server().device_list)
	for i in range(device_list_len):
		#添加进程
		p=multiprocessing.Process(target=get_suite,args=(i,casepath,))
		processes.append(p)
	for p in processes:
		#启动进程
		Log().info("启动进程："+str(p))
		p.start()


if __name__ == "__main__":
	pid=multiprocessing.current_process().pid
	Log().error("开始执行测试，主进程PID："+str(pid))
	run_main("../case/testcase.xls")