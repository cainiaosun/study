import unittest,threading
import sys,time
import multiprocessing
from selenium.webdriver.common.by import By
sys.path.append("..//04.util")
import Function as F#"..//04.util//Function.py"
import HTMLTestRunner
import server
from write_user_command import WriteUserCommand
from log import Log
sys.path.append("..//05.page")
import login_page
sys.path.append("..//07.business")
import login_bussiness
sys.path.append("..//03.base")
from appium_init import BaseDriver

class ParameTestCase(unittest.TestCase):
	def __init__(self,methodName='runTest',parame=None):
		super(ParameTestCase,self).__init__(methodName)
		self.parame=parame

class mukewang(ParameTestCase):
	@classmethod
	def setUpClass(cls):
		pass

	def setUp(self):
		F.driver=BaseDriver().android_driver(self.parame)

	def test_a(self):
		Log().info("执行案例：test_a")
		
		result=login_bussiness.to_login_page()
		self.assertNotEqual(result,0)
		#self.assertTrue(result)
		#self.assertNotEqual(1,2)
		#self.assertNotEqual(1,2)
		#self.assertTrue(flag)
		#self.assertFalse(flag)

	#@unittest.skip("CaseTest")
	def test_b(self):
		Log().info("执行案例：test_b")
		login_bussiness.to_login_page()
		result=login_bussiness.login_sucess()
		time.sleep(5)
		print(result)
		self.assertNotEqual(result,0)

	def tearDwon(self):
		pass


	@classmethod
	def tearDwonClass(cls):
		pass





def get_suite(i,title='测试报告_title',description='用例执行情况：'):	
	time.sleep(20)
	#连接手机
	#F.driver=BaseDriver().android_driver(i)
	#F.driver=F.get_driver()
	time.sleep(15)
	suite = unittest.TestSuite()#获取套件
	mukewang()
	suite.addTest(mukewang('test_a',parame=i))#添加案例
	suite.addTest(mukewang('test_b',parame=i))#添加案例
	#runner=unittest.TextTestRunner()#
	filename = "../08.report/report"+str(1)+".html"
	with open(filename, 'wb') as fp:        
		# 定义测试报告        
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title, description=description)        
		# 运行测试用例        
		runner.run(suite)#执行套件       
		# 关闭测试报告        
		#fp.close()

if __name__ == "__main__":


	#server.Server().main()
	#time.sleep(15)
	#F.driver=BaseDriver().android_driver(0)
	#unittest.main()
	"""启动服务"""
	server.Server().main()
	processes = []
	print(type(processes))
	device_list_len=len(server.Server().device_list)
	for i in range(device_list_len):
		p=multiprocessing.Process(target=get_suite,args=(i,))
		processes.append(p)
	for p in processes:
		p.start()

	#print(WriteUserCommand().get_file_lines())
	#threading.Thread(server.Server().main())
	#get_suite()
	
