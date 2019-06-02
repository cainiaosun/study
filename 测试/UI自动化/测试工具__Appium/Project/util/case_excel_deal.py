#coding=utf-8
import sys,os,shutil,multiprocessing
sys.path.append("..")
from util.opera_xlrd import OperaExcel
from util.write_environment import Environment

class DataTable(OperaExcel):	
	def __init__(self,colunm=None,sheet=0,path=None):
		"""
		构造函数
		参数：
			--colunm：列，可以是列名或列index序列
			--sheet：使用的sheet页，可以是sheet名称，页可以是index序列
		"""
		debugpath="../temp/testsuite_tempdata/testsuite_debug"
		if path==None:
			self.path=Environment("case_path").value
		else:
			self.path=path
		self.colunm=colunm
		self.row=Environment("row").value

	@staticmethod
	def load(casefile,running_path=None):
		shutil.copyfile(casefile,running_path+"/runningcase.xls")
		Environment().add("case_path",running_path+"/runningcase.xls")
		return True


	# def load(self,casefile,running_path=None):
	# 	if running_path==None:
	# 		running_path=self.path
	# 	shutil.copyfile(casefile,running_path+"/runningcase.xls")
	# 	Environment().add("case_path",running_path+"/runningcase.xls")
	# 	return True

	def open(self):
		return OperaExcel().get_excel()

	def get_sheet(self,sheet=None):
		sheet=OperaExcel().get_sheet(Environment("sheet").value)
		return sheet

	def rows(self):
		rows=sheet=OperaExcel().get_rows()
		return rows

	def cols(self):
		cols=OperaExcel().get_cols()
		return cols

	def set(self,value,colunmname=None,row=None):
		colunm=self.colunm
		#colunm=OperaExcel().get_column(colunm)
		OperaExcel().write_value(self.row,colunm,value)

	def value(self):
		return OperaExcel().get_cell(self.row,self.colunm)

	def case_list(self,Case_ID="Case_ID"):
		#return set(self.get_col_values(i))
		i=OperaExcel().get_column(Case_ID)
		case_list=OperaExcel().get_col_values(i)#获取第i行的值，读案例这里填写案例编号(Case_ID)所在的列数
		case_list=list({}.fromkeys(case_list).keys())#去除重复单元格，读案例这里的目的是去除合并单元格读到值
		del case_list[0]#去除第一个值，读案例这里是去除读到的列名的值，即案例编号(Case_ID)
		if "" in case_list:
			case_list.remove("")#去除空值，原则上不会出现空值
		return case_list#返回所有的案例编号列表

	def col_values(self,Case_ID="Case_ID"):
		i=OperaExcel().get_column(Case_ID)
		return OperaExcel().get_col_values(i)

	def exist(self):
		return OperaExcel().exist()



if __name__ == "__main__":
	print("001")
	Environment().add("case_path","../temp/testsuite_tempdata/testsuite_debug/runningcase.xls")
	Environment().add("sheet",0)
	Environment().add("row",3)
	print(Environment("case_path").value)
	print(Environment("case_path").exist())
	print(Environment("case_path").section_exist())
	print(Environment("sheet").exist())
	print(Environment("sheet").value)
	print(Environment("row").value)
	Environment().add("key5","rrrrr")
	#DataTable().load("../config/testcase.xls")
	print(DataTable(0).value())
	print(DataTable().open())
	print(DataTable().get_sheet())
	print(DataTable().rows())
	print(DataTable().cols())
	print(DataTable().case_list())
	print(DataTable().col_values())
	print(DataTable("所属模块").set("ttt00"))
	print(DataTable(1).set("ttt0033"))
	print(DataTable("所属模块").value())
	print(DataTable(1).value())



	

