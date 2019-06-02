#coding:utf-8
import sys,unittest
sys.path.append("../../..")
from util import HTMLTestRunner
from base.datatable import DataTable
from base.environment import Environment
from util.write_log import Log
from base import unittest_base
class AutoCase(unittest_base.UnitTestBase):
	def test_00000(self):
		print("========================================")
		Log().info("Excute Case:test"+str("00000"))
		index=int(0)
		case_list=DataTable("Case_ID").case_list()
		col_values=DataTable("Case_ID").col_values()
		start=col_values.index(case_list[index])
		count=col_values.count(case_list[index])
		end=start+count
		Log().info("Case Name:"+DataTable("Case_ID").value())
		result=[]
		for i in range(start,end):
			Environment("row").set(start)
			result.append(self.crete_step())
		self.assertEqual("1","2")

		
	def test_00001(self):
		print("========================================")
		Log().info("Excute Case:test"+str("00001"))
		index=int(1)
		case_list=DataTable("Case_ID").case_list()
		col_values=DataTable("Case_ID").col_values()
		start=col_values.index(case_list[index])
		count=col_values.count(case_list[index])
		end=start+count
		Log().info("Case Name:"+DataTable("Case_ID").value())
		result=[]
		for i in range(start,end):
			Environment("row").set(start)
			result.append(self.crete_step())
		print(result)
		return result
		
	def test_00002(self):
		print("========================================")
		Log().info("Excute Case:test"+str("00002"))
		index=int(2)
		case_list=DataTable("Case_ID").case_list()
		col_values=DataTable("Case_ID").col_values()
		start=col_values.index(case_list[index])
		count=col_values.count(case_list[index])
		end=start+count
		Log().info("Case Name:"+DataTable("Case_ID").value())
		result=[]
		for i in range(start,end):
			Environment("row").set(start)
			result.append(self.crete_step())
		print(result)
		return result
		
	def test_00003(self):
		print("========================================")
		Log().info("Excute Case:test"+str("00003"))
		index=int(3)
		case_list=DataTable("Case_ID").case_list()
		col_values=DataTable("Case_ID").col_values()
		start=col_values.index(case_list[index])
		count=col_values.count(case_list[index])
		end=start+count
		Log().info("Case Name:"+DataTable("Case_ID").value())
		result=[]
		for i in range(start,end):
			Environment("row").set(start)
			result.append(self.crete_step())
		print(result)
		return result
		

if __name__ == '__main__':
	# unittest.main()
	suite = unittest.TestSuite()#获取套件   
	suite.addTest(AutoCase('test_00000'))
	#runner=unittest.TextTestRunner()#
	filename="./report.html"
	with open(filename, 'wb') as fp:        
		# 定义测试报告        
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="报告标题", description="报告描述")  
		runner.run(suite)#执行套件   