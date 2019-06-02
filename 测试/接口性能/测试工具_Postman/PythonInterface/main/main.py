#coding:utf-8
import os,sys,time,unittest,threading,multiprocessing
sys.path.append("..")
from util import HTMLTestRunner
from util.write_log import Log
from base.unittest_base import UnitTestBase
# import running_folder as CreateRunningFolder
import base.generate_case as GenerateCase#生成unittest案例脚本模块
from base.environment import Environment
from base.datatable import DataTable
from base.get_config import MyConfig as myconfig
class RunMain:
	def __init__(self):
		pass

	def run_test(self,filename):
		DataTable.load(filename)
		# case_list=DataTable().case_list
		# case_count=len(case_list)

		# temppath=CreateRunningFolder.folder_create(casepath)#为当前运行测试套件创建一个临时的运行文件夹，存放运行案例、运行参数、自动生成的测试脚本
		# temppath=os.path.abspath(temppath)
		running_path=Environment("running_path").value
		GenerateCase.GenerateCase(Environment("running_path").value)#生成unittest案例脚本
		sys.path.append(running_path)#添加创建的临时目录到环境变量，以使得可以找到临时生成的测试脚本文件case.py
		from autocase import AutoCase
		suite = unittest.TestSuite()#获取套件
		Log().info("添加案例！")
		case_list=DataTable("Case_ID").case_list()
		for i in range(0,len(case_list)):
			# while len(str(i))<5:
			stri=str(i).rjust(5,"0")
			#print("suite.addTest(mukewang('test_"+j+"',parame=i))")
			print("suite.addTest(AutoCase('test_"+stri+"_"+case_list[i]+"'))")
			eval("suite.addTest(AutoCase('test_"+stri+"_"+case_list[i]+"'))")
		#runner=unittest.TextTestRunner()#
		filename = myconfig("project","project_path").value+myconfig("project","report_path").value+"/report.html"
		with open(filename, 'wb') as fp:        
			# 定义测试报告        
			runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="报告标题", description="报告描述")        
			# 运行测试用例        
			runner.run(suite)#执行套件

if __name__=="__main__":
	RunMain().run_test("../case/testcase.xls")