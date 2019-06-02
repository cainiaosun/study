#coding=utf-8
import shutil,xlrd,os,sys
from xlutils.copy import copy
sys.path.append("..")
from util.write_environment import Environment
#xlwd

"""
	只支持.xls文件
"""


class OperaExcel:
	def __init__(self,file_path=None,i=None):
		#print(Environment("sheet").value)
		if file_path == None:
			self.file_path = Environment("case_path").value #'..\\config\\testcase.xls'
		else:
			self.file_path = file_path	
		if i == None:
			i=0
		self.excel = self.get_excel()
		i=Environment("sheet").value
		self.data = self.get_sheet(i)
			
	def get_excel(self):
		'''
		打开并获取，excel对象
		'''
		# file_path_end='..\\config\\testcase_tem.xls'
		# shutil.copyfile(self.file_path,file_path_end)
		excel = xlrd.open_workbook(self.file_path,formatting_info=True)
		return excel

	def get_sheet(self,i):
		'''
		获取一个i键(或index)对应的sheet页对象
		参数：
			--i：sheet页名或者sheet的键值
		'''
		if isinstance(i,int):
			tables = self.excel.sheets()[i]
		elif isinstance(i,str):
			tables = self.excel.get_sheet_by_name(i)
		return tables

	def get_rows(self):
		'''
		获取sheet页的行数
		'''
		rows = self.data.nrows
		return rows

	def get_cols(self):
		'''
		获取sheet页的行数
		'''
		cols = self.data.ncols
		return cols

	def get_cell(self,row,column):
		'''
		获取sheet页单元格的值
		参数：
			--row：所在行
			--column：所在列
		'''
		if isinstance(column,int)==False:
			column=self.get_column(column)
		data = self.data.cell(row,column).value
		return data

	def get_column(self,column_name):
		read_value = self.excel
		sheet=read_value.sheets()[0]
		for i in range(sheet.ncols):
			if sheet.cell(0,i).value==column_name:
				column=i
				break
		return column

	def get_row(self,row_name):
		read_value = self.excel
		sheet=read_value.sheets()[0]
		for i in range(sheet.nrows):
			if sheet.cell(0,i).value==row_name:
				row=i
				break
		return row

	def write_value(self,row,column="实际结果",value=""):
		'''
		向sheet页单元格写入
		参数：
			--row_name：行名，即一行的第一个单元格的值
				根据案例模板是Case_ID列的值，通过该值获取对应Case_ID所在的行数
			--column_name：列名，即一列的第一个单元格的值
				通过该值获取对应的列数,结合row_name获得的行数，修改对应单元格的值
				根据案例模板多为：实际结果、是否执行、是否通过
		Etc：
			修改案例 "test_04" 的 执行状态 为 "pass"
			OperaExcel().write_value("test_04","执行状态","通过")
		'''
		read_value = self.excel
		sheet=read_value.sheets()[0]
		# for i in range(sheet.nrows):
		# 	if sheet.cell(i,0).value==row_name:
		# 		row=i
		# 		break
		if isinstance(row,int)==False:
			row=self.get_row(row)
		if isinstance(column,int)==False:
			column=self.get_column(column)
		write_data = copy(read_value)
		write_save = write_data.get_sheet(0)
		write_save.write(row,column,value)
		write_data.save(self.file_path)

	def get_value(self,row_name="",column_name="实际结果",value=""):
		'''
		向sheet页单元格写入
		参数：
			--row_name：行名，即一行的第一个单元格的值
				根据案例模板是Case_ID列的值，通过该值获取对应Case_ID所在的行数
			--column_name：列名，即一列的第一个单元格的值
				通过该值获取对应的列数,结合row_name获得的行数，修改对应单元格的值
				根据案例模板多为：实际结果、是否执行、是否通过
		Etc：
			修改案例 "test_04" 的 执行状态 为 "pass"
			OperaExcel().write_value("test_04","执行状态","通过")
		'''
		read_value = self.excel
		sheet=read_value.sheets()[0]
		row=get_row=self.get_row(row_name)
		column=self.get_column(column_name)
		return sheet.cell(row,column).value

	def merge_cell(self,sheet):
		sheet = self.data
		#print(sheet.cell(0,0))
		rt = {}
		#print("this is mer:")
		#print(sheet.merged_cells)
		if sheet.merged_cells:
			# exists merged cell
			for item in sheet.merged_cells:
				for row in range(item[0], item[1]):
					for col in range(item[2], item[3]):
						rt.update({(row, col): (item[0], item[2])})
		return rt

	def get_col_values(self,i):
		sheet = self.data
		merged = self.merge_cell(sheet)
		data = sheet.col_values(i)
		for index,content in enumerate(data):
			if merged.get((index, i)):
				# 这是合并后的单元格，需要重新取一次数据
				data[index] = sheet.cell_value(*merged.get((index, i)))
		return data

	def get_case_list(self,i):
		#return set(self.get_col_values(i))
		case_list=self.get_col_values(i)#获取第i行的值，读案例这里填写案例编号(Case_ID)所在的列数
		case_list=list({}.fromkeys(case_list).keys())#去除重复单元格，读案例这里的目的是去除合并单元格读到值
		del case_list[0]#去除第一个值，读案例这里是去除读到的列名的值，即案例编号(Case_ID)
		if "" in case_list:
			case_list.remove("")#去除空值，原则上不会出现空值
		return case_list#返回所有的案例编号列表



if __name__ == '__main__':
	#print(OperaExcel().get_sheet(0).col_values(0))
	#print(OperaExcel().get_sheet(0).merged_cells)
	#print(OperaExcel().merge_cell(OperaExcel().get_sheet(0)))	
	#print(OperaExcel().get_col_values(0))
	#print(OperaExcel().get_case_list(0))
	col_values=OperaExcel().get_col_values(0)
	case_list=OperaExcel().get_case_list(0)
	print(col_values)
	print(case_list)
	
	count=len(case_list)
	for case in case_list:
		#case=case_list[i]
		case_step_count=col_values.count(case)
		start=col_values.index(case)
		print(case,case_step_count,start)
	# read_value = OperaExcel().get_excel()
	# sheet = read_value.sheets()[0]
	# help(sheet)
	# opera = OperaExcel()
	# print(opera.get_rows())
	# print(opera.write_value(6,'pass'))
	# print(type(1))
	# help(isinstance)
	# print(isinstance(0,int))


	# read_value =OperaExcel().get_excel()
	# write_data = copy(read_value)
	# print(type(write_data))
	# write_save = write_data.get_sheet(0)
	# print(type(write_save))
	# help(write_save)
	# print(type(write_save.cell))
	OperaExcel().write_value("test_01","实际结果","通过")
	#OperaExcel().my_write("test_01","操作","haha")




