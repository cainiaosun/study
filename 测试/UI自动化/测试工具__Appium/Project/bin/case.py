
import sys,unittest
sys.path.append("..")
from util.case_excel_deal import DataTable
from util.write_log import Log
import unittest_main
class AutoCase(unittest_main.mukewang):
	def test_00000(self):
		Log().info("Excute Case:test"+str("00000"))
		index=int(0)
		case_list=DataTable("Case_ID",path+"/runningcase.xls").case_list()
		col_values=DataTable("Case_ID",path=path+"/runningcase.xls").col_values
		start=col_values.index(case_list[index])
		count=col_values.count(case_list[index])
		end=start+count
		Log().info("Case Name:"+DataTable("Case_ID",path=path+"/runningcase.xls").value)
		for i in range(start,end):
			self.crete_step(i)
				
	def test_00001(self):
		Log().info("Excute Case:test"+str("00001"))
		index=int(1)
		case_list=DataTable("Case_ID",path+"/runningcase.xls").case_list()
		col_values=DataTable("Case_ID",path=path+"/runningcase.xls").col_values
		start=col_values.index(case_list[index])
		count=col_values.count(case_list[index])
		end=start+count
		Log().info("Case Name:"+DataTable("Case_ID",path=path+"/runningcase.xls").value)
		for i in range(start,end):
			self.crete_step(i)
				
	def test_00002(self):
		Log().info("Excute Case:test"+str("00002"))
		index=int(2)
		case_list=DataTable("Case_ID",path+"/runningcase.xls").case_list()
		col_values=DataTable("Case_ID",path=path+"/runningcase.xls").col_values
		start=col_values.index(case_list[index])
		count=col_values.count(case_list[index])
		end=start+count
		Log().info("Case Name:"+DataTable("Case_ID",path=path+"/runningcase.xls").value)
		for i in range(start,end):
			self.crete_step(i)
				

if __name__=="__main__":
	unittest.main()