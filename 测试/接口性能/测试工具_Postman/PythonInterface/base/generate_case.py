#创建可执行的unittest案例
import sys
sys.path.append("..")
from base.datatable import DataTable
from base.get_config import MyConfig as myconfig

project_path=myconfig("project","project_path").value
data_path=myconfig("project","data_path").value
path=project_path+data_path

def GenerateCase(path):
	file=path+"/autocase.py"
	with open(file,"w") as fp:
		fp.write("""#coding:utf-8
import sys,unittest
sys.path.append("../")
from base.datatable import DataTable
from base.environment import Environment
from util.write_log import Log
from base import unittest_base
class AutoCase(unittest_base.UnitTestBase):""")
		case_list=DataTable(path+"/runningcase.xls").case_list()
		for i in range(0,len(case_list)):
			testid=str(i).rjust(5,"0")
			fp.write("""
	def test_"""+testid+"_"+case_list[i]+"""(self):
		print("========================================")
		Log().info("Excute Case:"+str(\""""+case_list[i]+"""\"))
		index=int("""+str(i)+""")
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
		""")
		fp.write("""

if __name__ == '__main__':
	unittest.main()""")	
	#fp.close()


if __name__=="__main__":
	GenerateCase(path)