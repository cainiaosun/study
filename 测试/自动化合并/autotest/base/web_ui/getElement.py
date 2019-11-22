import sys,os
from util.operate_excel import OperaExcel
from base.web_ui.get_config import MyConfig
'''
	从数据表中读取定位元素，并以字典的形式存储起来返回
'''
class getLocator(object):
	def __init__(self):
		pass

	def get(self,excel=MyConfig('project','element').value):
		#
		Locators={}
		exceldata=OperaExcel(excel)
		for i in range (1,exceldata.get_rows()):
			Locators[exceldata.get_value(i,1)]=(exceldata.get_value(i,2),exceldata.get_value(i,3))
		return Locators


if __name__=="__main__":
	print(getLocator().get("./case/page.xls"))
	print(getLocator().get()['用户名输入框'])
