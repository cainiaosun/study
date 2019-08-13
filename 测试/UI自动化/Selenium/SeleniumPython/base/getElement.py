import sys,os
sys.path.append("..")
from util.operate_excel import OperaExcel
'''
	从数据表中读取定位元素，并以字典的形式存储起来返回
'''
class getElement(object):
	def __init__(self):
		pass

	def get(self,excel):
		#
		elements={}
		exceldata=OperaExcel(excel)
		for i in range (1,exceldata.get_rows()):
			elements[exceldata.get_value(i,1)]=(exceldata.get_value(i,2),exceldata.get_value(i,3))
		return elements


if __name__=="__main__":
	print(getElement().get("../case/page.xls"))