#读取：元素-element 读取：操作-handle 读取：值-value
import sys
sys.path.append("..//04.util")
from opera_xlrd import OperaExcel
from write_user_command import WriteUserCommand
from log import Log
import server
sys.path.append("..//05.page")
import login_page as PageElement
import Function as MyDriverFuction#"..//04.util//Function.py"
sys.path.append("..//03.base")
from appium_init import BaseDriver


class RunMainUnit(object):
	def __init__(self,Case_ID):
		self.Case_ID=Case_ID
	def operate_action(self):
		action=OperaExcel().get_value(self.Case_ID,"操作")
		return action

	def operate_element(self):
		handle=OperaExcel().get_value(self.Case_ID,"操作元素")
		handle=eval("PageElement."+handle)
		return handle

	def operate_value(self):
		value=OperaExcel().get_value(self.Case_ID,"操作值")
		return value

	def expect_element(self):
		o_handle=OperaExcel().get_value(self.Case_ID,"预期元素")
		handle=eval("PageElement."+o_handle)
		return handle

	def expect_action(self):
		action=OperaExcel().get_value(self.Case_ID,"预期操作")
		return action


class RunMain(object):
	def run(self):
		Log().info("RunMain().run()运行")
		for i in range(1,OperaExcel().get_rows()):
			Case_ID=OperaExcel().get_cell(i,0)
			get=RunMainUnit(Case_ID)
			operate_action=get.operate_action()
			operate_element=get.operate_element()
			operate_value=get.operate_value()
			print(str(operate_action)+" ; "+str(operate_element)+" ; "+str(operate_value)+" .")
			#expect_action=get.expect_action()
			#expect_element=get.expect_element()
			if operate_action==None:
				pass
			else:
				if operate_element:
					Log().info("元素操作！")
					Log().info(str(operate_action)+' ; '+str(operate_element)+' ; '+str(operate_value)+' . ')
					MyDriverMethod=getattr(MyDriverFuction.Element(operate_element),operate_action)
				else:
					Log().info("非元素操作！")
					MyDriverMethod=getattr(MyDriverFuction,operate_action)
				if operate_value:
					MyDriverMethod(operate_value)
				else:
					MyDriverMethod()
					

if __name__ == '__main__':
	server.Server().main()
	MyDriverFuction.driver=BaseDriver().android_driver(0)
	RunMain().run()
	# for i in range(1,OperaExcel().get_rows()):
	# 	Case_ID=OperaExcel().get_cell(i,0)
	# 	get=RunMainUnit(Case_ID)
	# 	operate_action=get.operate_action()
	# 	operate_element=get.operate_element()
	# 	operate_value=get.operate_value()
	# 	print(str(operate_action)+" ; "+str(operate_element)+" ; "+str(operate_value)+" .")


# class Test(object):
# 	def __init__(self,a,b):
# 		self.a=a
# 		self.b=b

# 	def sum(self,c):
# 		print(self.a+self.b+c) 
# if __name__=="__main__":
# 	element=(1,2)
# 	print(element[0])
# 	print(element[1])
# 	handle="sum"
# 	value=4
# 	Test(element[0],element[1]).sum(3)
# 	getattr(Test(element[0],element[1]),handle)(value)

# 	print(Test(element[0],element[1]).a)
# 	print(str(element))
# 	print(eval("Test"+str(element)+".a"))
