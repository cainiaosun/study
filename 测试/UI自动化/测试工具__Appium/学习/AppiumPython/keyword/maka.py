import unittest,threading
import sys,time
import multiprocessing
from selenium.webdriver.common.by import By
sys.path.append("..//04.util")
import Function as MyDriverFuction#"..//04.util//Function.py"
import HTMLTestRunner
import server
from write_user_command import WriteUserCommand
from log import Log
sys.path.append("..//05.page")
import login_page as PageElement
sys.path.append("..//07.business")
import login_bussiness
sys.path.append("..//03.base")
from appium_init import BaseDriver

sys.path.append("..//04.util")
from opera_xlrd import OperaExcel

class ParameTestCase(unittest.TestCase):
	def __init__(self,methodName='runTest',parame=None):
		super(ParameTestCase,self).__init__(methodName)
		self.parame=parame

class mukewang(ParameTestCase):
	@classmethod
	def setUpClass(cls):
		pass

	def setUp(self):
		MyDriverFuction.driver=BaseDriver().android_driver(self.parame)
		#self.Case_ID=
		
	def operate_action(self):
		action=OperaExcel().get_value(self.Case_ID,"操作")
		return action

	def operate_element(self):
		handle=OperaExcel().get_value(self.Case_ID,"操作元素")
		handle=eval("PageElement."+handle)
		return handle

	def operate_value(self):
		value=OperaExcel().get_value(self.Case_ID,"操作值")
		return value

	def expect_element(self):
		o_handle=OperaExcel().get_value(self.Case_ID,"预期元素")
		handle=eval("PageElement."+o_handle)
		return handle

	def expect_action(self):
		action=OperaExcel().get_value(self.Case_ID,"预期操作")
		return action

	def myrun(self,i):
		Log().info("myrun()运行")
		for i in range(1,OperaExcel().get_rows()):
			self.Case_ID=OperaExcel().get_cell(i,0)
			Log().info(self.Case_ID)
			operate_action=self.operate_action()
			operate_element=self.operate_element()
			operate_value=self.operate_value()
			print(str(operate_action)+" ; "+str(operate_element)+" ; "+str(operate_value)+" .")
			#expect_action=get.expect_action()
			#expect_element=get.expect_element()
			if operate_action==None:
				pass
			else:
				if operate_element:
					Log().info("元素操作！")
					Log().info(str(operate_action)+' ; '+str(operate_element)+' ; '+str(operate_value)+' . ')
					MyDriverMethod=getattr(MyDriverFuction.Element(operate_element),operate_action)
				else:
					Log().info("非元素操作！")
					MyDriverMethod=getattr(MyDriverFuction,operate_action)
				if operate_value:
					MyDriverMethod(operate_value)
				else:
					MyDriverMethod()

	def test_0001(self):
		Log().info("执行案例：001")
		self.myrun(1)

	def test_0002(self):
		Log().info("执行案例：002")
		self.myrun(2)

	def test_0003(self):
		Log().info("执行案例：003")
		self.myrun(3)

	def test_0004(self):
		Log().info("执行案例：004")
		self.myrun(4)

	def test_0005(self):
		Log().info("执行案例：005")
		self.myrun(5)

	def test_0006(self):
		Log().info("执行案例：test_a")
		self.myrun(6)

	def tearDwon(self):
		pass


	@classmethod
	def tearDwonClass(cls):
		pass




def get_suite(i,title='title-测试报告',description='用例执行情况：'):	
	suite = unittest.TestSuite()#获取套件
	for j in range(1,OperaExcel().get_rows()):
		if True==True:
			while len(str(j))<4:
				j="0"+str(j)
			Log().info("添加案例！")
			print("suite.addTest(mukewang('test_"+j+"',parame=i))")
			eval("suite.addTest(mukewang('test_"+j+"',parame=i))")
	#runner=unittest.TextTestRunner()#
	filename = "../08.report/report"+str(1)+".html"
	with open(filename, 'wb') as fp:        
		# 定义测试报告        
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title, description=description)        
		# 运行测试用例        
		runner.run(suite)#执行套件       
		# 关闭测试报告        
		#fp.close()

"""案例执行入口"""
def run():
	"""启动服务"""
	server.Server().main()
	"""添加并启动进程"""
	processes = []
	device_list_len=len(server.Server().device_list)
	for i in range(device_list_len):
		p=multiprocessing.Process(target=get_suite,args=(i,))
		processes.append(p)
	for p in processes:
		p.start()

if __name__ == "__main__":
	run()