#创建可执行的unittest案例
import sys
sys.path.append("..")
from util.case_excel_deal import DataTable

def GenerateCase(path):
	file=path+"/autocase.py"
	with open(file,"w") as fp:
		fp.write("""
import sys
sys.path.append("../")
from util.case_excel_deal import DataTable
from util.write_log import Log
import unittest_main
class AutoCase(unittest_main.mukewang):""")
		case_list=DataTable(path+"/runningcase.xls").case_list()
		for i in range(0,len(case_list)):
			testid=str(i).rjust(5,"0")
			fp.write("""
	def test_"""+testid+"""(self):
		Log().info("Excute Case:test"+str(\""""+testid+"""\"))
		index=int("""+str(i)+""")
		case_list=DataTable("Case_ID",path+"/runningcase.xls").case_list()
		col_values=DataTable("Case_ID",path=path+"/runningcase.xls").col_values
		start=col_values.index(case_list[index])
		count=col_values.count(case_list[index])
		end=start+count
		Log().info("Case Name:"+DataTable("Case_ID",path=path+"/runningcase.xls").value)
		for i in range(start,end):
			self.crete_step(i)
				""")
	#fp.close()


if __name__=="__main__":
	GenerateCase(".")