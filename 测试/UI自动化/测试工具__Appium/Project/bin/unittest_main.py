import sys,time,unittest,threading,multiprocessing
from selenium.webdriver.common.by import By
sys.path.append("..")
import base.Function as MyDriverFuction#"..//04.util//Function.py"
from util import HTMLTestRunner
from util import server
from util.write_user_command import WriteUserCommand
from util.write_log import Log
import po.page.login_page as PageElement
from po.business import login_bussiness
from util.opera_xlrd import OperaExcel
from base.appium_init import BaseDriver


class ParameTestCase(unittest.TestCase):
	def __init__(self,methodName='runTest',parame=None):
		super(ParameTestCase,self).__init__(methodName)
		self.parame=parame
		# self.casepase=casepase

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

	#构建测试脚本
	def crete_step(self,i):
		Log().info("crete_step()运行")
		for i in range(1,OperaExcel().get_rows()):
			self.Case_ID=OperaExcel().get_cell(i,0)
			Log().info(self.Case_ID)
			operate_action=self.operate_action()
			operate_element=self.operate_element()
			operate_value=self.operate_value()
			print(str(operate_action)+" ; "+str(operate_element)+" ; "+str(operate_value)+" .")
			#expect_action=get.expect_action()
			#expect_element=get.expect_element()
			if operate_action==None:#案例操作为必输选项，不输入打印错误日志
				Log().error("案例缺少操作(步骤)，检查案例是否正确！")
			elif operate_action in ["click","send_keys"]:
				#如果遇到Function中封装的方法，那么调用Function模块
				if operate_element:
					#操作元素存在调用Element类
					Log().info("元素操作！")
					Log().info(str(operate_action)+' ; '+str(operate_element)+' ; '+str(operate_value)+' . ')
					MyDriverMethod=getattr(MyDriverFuction.Element(operate_element),operate_action)
				else:
					#操作元素不存在调用Element类以外的方法
					Log().info("非元素操作！")
					MyDriverMethod=getattr(MyDriverFuction,operate_action)
			elif operate_action in ["assertNotEqual","assertNotEqual","assertTrue","assertFalse"]:
				MyDriverMethod=getattr(self,operate_action)
			else:
				MyDriverMethod=getattr(login_bussiness,operate_action)
			if operate_action==None:
				getattr(login_bussiness,operate_action)
			if operate_value:
					MyDriverMethod(operate_value)
			else:
					MyDriverMethod()



	@classmethod
	def tearDwonClass(cls):
		pass



def get_suite(i,title='title-测试报告',description='用例执行情况：'):	
	suite = unittest.TestSuite()#获取套件
	Log().info("添加案例！")
	for j in range(1,OperaExcel().get_rows()):
		if True==True:
			while len(str(j))<4:
				j="0"+str(j)
			#print("suite.addTest(mukewang('test_"+j+"',parame=i))")
			eval("suite.addTest(mukewang('test_"+j+"',parame=i))")
	#runner=unittest.TextTestRunner()#
	filename = "../report/report"+str(1)+".html"
	with open(filename, 'wb') as fp:        
		# 定义测试报告        
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title, description=description)        
		# 运行测试用例        
		runner.run(suite)#执行套件       
		# 关闭测试报告        
		#fp.close()