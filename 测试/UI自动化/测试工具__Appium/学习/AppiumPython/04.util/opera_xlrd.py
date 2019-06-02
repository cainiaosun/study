#coding=utf-8
import shutil,xlrd,os
from xlutils.copy import copy
#xlwd

"""
	只支持.xls文件
"""


class OperaExcel:
	def __init__(self,file_path=None,i=None):
		if file_path == None:
			self.file_path = 'F:\\GIT文件\\mystudy\\学习资料\\编程与测试\\测试工具__Appium\\学习\\AppiumPython\\02.config\\testcase.xls'
		else:
			self.file_path = file_path	
		if i == None:
			i=0
		self.excel = self.get_excel()
		self.data = self.get_sheet(i)
			
	def get_excel(self):
		'''
		打开并获取，excel对象
		'''
		file_path_end="../02.config/testcase_temp.xlsx"
		shutil.copyfile(self.file_path,file_path_end)
		excel = xlrd.open_workbook(self.file_path)
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
			table = excel.get_sheet_by_name(i)
		return tables

	def get_rows(self):
		'''
		获取sheet页的行数
		'''
		rows = self.data.nrows
		return rows

	def get_columns(self):
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
		data = self.data.cell(row,column).value
		return data

	def write_value(self,row_name="",column_name="实际结果",value=""):
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
		for i in range(sheet.nrows):
			if sheet.cell(i,0).value==row_name:
				row=i
				break
		for i in range(sheet.ncols):
			if sheet.cell(0,i).value==column_name:
				column=i
				break
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
		for i in range(sheet.nrows):
			if sheet.cell(i,0).value==row_name:
				row=i
				break
		for i in range(sheet.ncols):
			if sheet.cell(0,i).value==column_name:
				column=i
				break
		return sheet.cell(row,column).value


if __name__ == '__main__':
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
	#OperaExcel().write_value("test_03","实际结果","猪猪网看电影！")
	#OperaExcel().my_write("test_01","操作","haha")




