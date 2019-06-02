#coding:utf-8
import sys,unittest
sys.path.append("../")
from base.datatable import DataTable
from base.environment import Environment
from util.write_log import Log
from base import unittest_base
class AutoCase(unittest_base.UnitTestBase):
	def test_00000_test_01(self):
		print("========================================")
		Log().info("Excute Case:"+str("test_01"))
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
		print(result)
		return result
		
	def test_00001_test_02(self):
		print("========================================")
		Log().info("Excute Case:"+str("test_02"))
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
		
	def test_00002_test_03(self):
		print("========================================")
		Log().info("Excute Case:"+str("test_03"))
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
		
	def test_00003_test_04(self):
		print("========================================")
		Log().info("Excute Case:"+str("test_04"))
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
	unittest.main()