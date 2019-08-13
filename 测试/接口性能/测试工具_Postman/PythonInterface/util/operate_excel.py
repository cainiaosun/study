#coding=utf-8
import shutil,xlrd,os,sys,time
from xlutils.copy import copy
#xlwd

"""
	只支持.xls文件
"""


class OperaExcel:
	def __init__(self,file_path=None,i=0):
		#print(Environment("sheet").value)
		if file_path == None:
			self.file_path ='..\\case\\testcase.xls'
			# self.file_path=None
		else:
			self.file_path = file_path	
		self.i=i
		self.excel = self.get_excel()
		self.data = self.get_sheet(i)
			
	def get_excel(self):
		'''
		打开并获取，excel对象
		'''
		excel = xlrd.open_workbook(self.file_path,formatting_info=True)
		return excel

	def get_sheet(self,i=None):
		'''
		获取一个i键(或index)对应的sheet页对象
		参数：
			--i：sheet页名或者sheet的键值
		'''
		if i==None:
			i=self.i
		try:
			if isinstance(i,int):
				tables = self.excel.sheets()[i]
			elif isinstance(i,str):
				tables = self.excel.get_sheet_by_name(i)
		except:
			raise Exception("sheet页："+str(i)+"，sheet页不存在！")
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
		if isinstance(row,int)==False:
			row=self.get_row(row)
		if isinstance(column,int)==False:
			column=self.get_column(column)
		rows=self.get_rows()
		cols=self.get_cols()
		if row==None or row>rows or column==None or column>cols:
			raise Exception("对象单元格："+str(row)+","+str(column)+",不在sheet页单元格区间0-"+str(rows)+",0-"+str(cols)+"内.")
		else:
			data = self.data.cell(row,column).value
		return data

	def get_column(self,value,row=0):
		'''
		获取某一行中，一个值首次出现位置的列数
		参数返回：
			:param column_name: 需要查找的内容
			:param row: 查找的行数，整型,默认row=0
			:return: 返回列数column，若没有查询到返回None
		'''
		read_value = self.excel
		sheet=read_value.sheets()[self.i]
		ncols=sheet.ncols
		for i in range(ncols+1):
			if i==ncols:
				column = None
			elif sheet.cell(row,i).value==value:
				column=i
				break
		return column

	def get_row(self,value,clomn=0):
		'''
		获取某一列中，一个值首次出现位置的行数
		参数返回：
			:param row_name: 需要查找的内容
			:param clomn: 查找的列数，整型，默认clomn=0
		:return: 返回行数row，若没有查询到返回None
		'''
		read_value = self.excel
		sheet=read_value.sheets()[self.i]
		nrows=sheet.nrows
		for i in range(nrows+1):
			if i==nrows:
				row =None
			elif sheet.cell(i,clomn).value==value:
				row=i
				break
		return row

	def write_value(self,row,column,value=""):
		'''
		向sheet页单元格写入
		参数：
			--row：行名或行序号
			--column_name：列名，或列序号
		Etc：
			修改案例 "test_04" 的 执行状态 为 "pass"
			OperaExcel().write_value("test_04","执行状态","通过")
		'''
		read_value = self.get_excel()
		sheet=read_value.sheets()[self.i]
		row_name=row
		col_name=column
		if isinstance(row,int)==False:
			row=self.get_row(row)
		if isinstance(column,int)==False:
			column=self.get_column(column)
		if row==None or column==None:
			raise Exception("单元格("+str(row_name)+","+str(col_name)+")不存在!")
		write_data = copy(read_value)
		write_save = write_data.get_sheet(self.i)
		write_save.write(row,column,value)
		write_data.save(self.file_path)
		return self.get_value(row,column)

	def get_value(self,row,column):
		'''
		获取sheet页一个单元格的值
		参数：
			--row：行名或行序号
			--column_name：列名，或列序号
		'''
		value=self.get_cell(row,column)
		return value

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

	def get_row_values(self,i):
		sheet = self.data
		merged = self.merge_cell(sheet)
		data = sheet.row_values(i)
		for index,content in enumerate(data):
			if merged.get((i,index)):
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
	print("获得的excel：",OperaExcel().get_excel())
	print("获得的sheet：",OperaExcel().get_sheet(1))
	# help(sheet)
	opera = OperaExcel()
	print("行数：",opera.get_rows())
	print("列数：",opera.get_cols())
	print("获取2行3列的值：",opera.get_cell(2,3))
	print("\"test_01\"所在行：",opera.get_row("test_01"))
	print("\"实际结果\"所在列：",opera.get_column("实际结果"))
	t=time.time()
	""" 实例中，self.excel 和 self.data在构造函数中，实例化先处理，所以在数据表修改后，会出现无法获取新值得问题，需要重新
	实例化，或者修改数据后再调用self.open_workbook()函数重新加载数据表才行,如：opera.write_value()函数，如果函数内使用
	self.excel，每次copy的都是最原始的实例化的表，所以只有最后一个会生效"""
	print("修改\"test_01\"所在行，\"实际结果\"所在列列的值结果为：",opera.write_value("test_01","实际结果",'3333'))
	print("耗时：",time.time()-t)
	print("获取\"test_01\"所在行，\"实际结果\"所在列列的值结果为：",opera.get_value("test_01","实际结果"))
	print("修改第3行，第7列的值结果为：",opera.write_value(2,6,'111'))
	print("获取第3行，第7列的值结果为：",opera.get_value(2,6))
	col_values=OperaExcel().get_col_values(0)
	case_list=OperaExcel().get_case_list(0)
	print("第一列的值(已处理合并单元格)：",col_values)
	print("第一列去掉，重复、首行、空数据的值(Case_ID案例列表)：",case_list)	
	count=len(case_list)
	for case in case_list:
		#case=case_list[i]
		case_step_count=col_values.count(case)
		start=col_values.index(case)
		print("案例编号：",case,"案例步骤数：",case_step_count,"案例起始步骤所处行数：",start,"案例结束步骤所处行数：",start+case_step_count-1)
	print("第一行的值：",OperaExcel().get_row_values(0))