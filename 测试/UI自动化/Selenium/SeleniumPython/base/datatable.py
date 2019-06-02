#coding=utf-8
import sys,os,shutil,multiprocessing
sys.path.append("..")
from base.get_config import MyConfig as myconfig
from base.environment import Environment
from util.operate_excel import OperaExcel


debug=False#debug参数，调试时修改为真,使用默认调试数据(需要把environment模块的debug值也改成True)


class DataTable(OperaExcel):	
	def __init__(self,column=None,sheet=0,path=None):
		"""
		构造函数
		参数：
			--column：列，可以是列名或列index序列
			--sheet：使用的sheet页，可以是sheet名称，页可以是index序列
		"""		
		if debug:#调试时，debug参数设置为真，就使用默认的调试参数
			data_path="../temp/runningdata/data_debug"
		else:
			pid=multiprocessing.current_process().pid
			data_path=myconfig("running",str(pid)).value
		self.data_path=data_path
		self.runnning_case=data_path+"/runningcase.xls"#运行中的案例
		self.sheet_id=Environment("sheet_id").value#配置文件中读取指定sheet页
		self.row=Environment("row").value#配置文件中读取指定row行
		self.column=column
		self.DataOperaExcel=OperaExcel(file_path=self.runnning_case,i=self.sheet_id)

	@staticmethod
	def load(casefile,running_path=None):
		if debug:#调试时，debug参数设置为真，就使用默认的调试参数
			data_path="../temp/runningdata/data_debug"
		else:
			pid=multiprocessing.current_process().pid
			data_path=myconfig("running",str(pid)).value
		shutil.copyfile(casefile,data_path+"/runningcase.xls")#复制案例到运行数据路径
		Environment().add("running_path",data_path)#修改变量参数：运行数据路径（无用参数）
		Environment().add("case_path",data_path+"/runningcase.xls")#修改变量参数：运行中的案例
		Environment().add("sheet_id",0)#修改变量参数：操作的sheet表，默认为0，即第一张
		Environment().add("row",2)#修改变量参数：当前操作的数据的所在行
		return True


	def open(self):
		return self.DataOperaExcel.get_excel()

	def get_sheet(self):
		sheet=self.DataOperaExcel.get_sheet()
		return sheet

	def rows(self):
		rows=sheet=self.DataOperaExcel.get_rows()
		return rows

	def cols(self):
		cols=self.DataOperaExcel.get_cols()
		return cols

	def set(self,value):
		row=Environment("row").value
		column=self.column
		#column=OperaExcel().get_column(column)
		return self.DataOperaExcel.write_value(self.row,column,value)

	def value(self):
		return self.DataOperaExcel.get_cell(self.row,self.column)

	def case_list(self,Case_ID="Case_ID"):
		#return set(self.get_col_values(i))
		i=self.DataOperaExcel.get_column(Case_ID)
		case_list=self.DataOperaExcel.get_col_values(i)#获取第i行的值，读案例这里填写案例编号(Case_ID)所在的列数
		case_list=list({}.fromkeys(case_list).keys())#去除重复单元格，读案例这里的目的是去除合并单元格读到值
		del case_list[0]#去除第一个值，读案例这里是去除读到的列名的值，即案例编号(Case_ID)
		if "" in case_list:
			case_list.remove("")#去除空值，原则上不会出现空值
		return case_list#返回所有的案例编号列表

	def col_values(self,Case_ID="Case_ID"):
		i=self.DataOperaExcel.get_column(Case_ID)
		return self.DataOperaExcel.get_col_values(i)

	def exist(self):
		row_list=self.DataOperaExcel.get_row_values(0)
		if self.column in row_list:
			return True
		else:
			return False



if __name__ == "__main__":
	print("加载数据表，写运行配置！")
	DataTable.load("../case/testcase.xls")
	print("加载数据表：",DataTable().open())
	print("获取sheet页：",DataTable().get_sheet())
	print("获取行数：",DataTable().rows())
	print("获取列数：",DataTable().cols())
	print("修改配置文件下row行，9列:",DataTable(8).set("操作"))
	print("修改配置文件下row行，\"预期结果\":",DataTable("预期结果").set("预期结果值"))
	print("修改配置文件下row行，\"实际结果\":",DataTable("实际结果").set("实际结果值"))
	print("读取配置文件下row行，\"实际结果\":",DataTable("实际结果").value())
	print("获取案例列表:",DataTable().case_list())
	print("获取案例列的值：",DataTable().col_values())
	print("判断\"实际结果\"列是否存在:",DataTable("实际结果").exist())
	print("判断\"实际结果1\"列是否存在:",DataTable("实际结果1").exist())



	

