import sys,time,unittest,threading,multiprocessing
sys.path.append("..")
from base.datatable import DataTable
from base.method import RunMethod
from base.environment import Environment




class ParameTestCase(unittest.TestCase):
	def __init__(self,methodName='runTest',parame=None):
		super(ParameTestCase,self).__init__(methodName)
		self.parame=parame
		# self.casepase=casepase

class UnitTestBase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		pass

	def setUp(self):
		pass
		#self.Case_ID=

	def tearDown(self):
		pass

	@classmethod
	def tearDwonClass(cls):
		pass
		
	def get_request_method(self):
		request_method=DataTable("请求方式").value()
		return request_method

	def get_url(self):
		url=DataTable("url").value()
		return url

	def get_data(self):
		data=DataTable("请求数据").value()
		return data


	#构建测试脚本
	def crete_step(self):
		# Log().info("crete_step()运行")
		request_method=self.get_request_method()
		url=self.get_url()
		data=eval(self.get_data())
		# print(type(data))
		#print(str(request_method)+" ; "+str(url)+" ; "+str(data)+" .")
		return RunMethod().request(request_method,url,data)

	# def test_001(self):
	# 	print(self.crete_step())


if __name__ == '__main__':
	unittest.main()
	# request_method=DataTable("请求方式").value()
	# url=DataTable("url").value()
	# data=DataTable("请求数据").value()
	# print(type(data))
	# print(request_method,url,data)
