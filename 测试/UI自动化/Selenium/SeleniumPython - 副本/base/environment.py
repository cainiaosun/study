#coding=utf-8
"""
一个进程(生成运行测试数据目录现在只有一个进程)中测试集合的环境变量值操作，可以增、删、查、改运行的环境变量值，以yaml文件的形式管理，yaml文件
格式{section：{name1：value1,name2：value2}},如果后面想改成{name1：value1,name2：value2}格式，
可以做适当修改，yaml文件没有限定死格式

The simplest way to use this is to invoke its main method. E.g.

    from write_environment import Environment

    ... define your tests ...

    if __name__ == '__main__':
        Environment(path="./environment.yaml").add("case_path","../temp/runningcase.xls")
        case_path=Environment("case_path").value

"""

import yaml,os,sys,multiprocessing,chardet
sys.path.append("..")
from base.get_config import MyConfig as myconfig


class Environment:
	"""
	
	"""
	path=myconfig("project","project_path").value+myconfig("project","data_path").value
	if os.path.exists(path)==False:
		path="../temp/testsuite_tempdata/testsuite_debug"
	def __init__(self,para=None,path=path):
		self.para=para#环境变量名称
		self.path=path+"/environment.yaml"#环境变量配置文件,默认值path+"/environment.yaml"

	def section_exist(self,section="Environment"):
		"""
		判断环境变量组是否存在
		参数：
			--section：yaml文件中的分组，默认"Environment"，目前只会用到这一组
		Etc：
			result=Environment().section_exist()
		"""
		path=self.path
		data=self.read_data()
		result=False
		if data:
			sections=[]
			for section,content in data.items():
				sections.append(section)
			if "Environment" in sections:
				result=True
		return result

	def exist(self):
		para=self.para
		data=self.read_data()
		section="Environment"
		result=False
		if self.section_exist(section):
			keys=[]
			for key,value in data[section].items():
				keys.append(key)
			if para in keys:
				result=True
		return result

	@property
	def value(self,para=None,section="Environment"):
		"""
		获取一个环境变量的值
		参数：
			--para：环境变量名称
			--section：yaml文件中的分组，默认"Environment"，不做修改
		Etc：
		"""
		return self.get_value(para,section)
	
	def get_value(self,para=None,section="Environment"):
		"""同value()方法"""
		para=self.para
		data=self.read_data()
		if self.exist():
			value=data[section][para]
		else:
			value=None
		return value

	def read_data(self,path=None):
		'''
		读取yaml数据
		参数：
			--path：yaml文件
		Etc：
			Environment().read_data("../temp/environment.yaml")
		'''
		if path==None:
			path=self.path
		if os.path.exists(path):
			with open(path,"r") as fr:
				data = yaml.safe_load(fr)
		else:
			with open(path,"w") as fr:
				data = None
		return data

	def clear(self,path=None):
		'''
		清空yaml文件
		参数：
			--path：yaml文件
		Etc：
			Environment().clear("../temp/environment.yaml")
		'''
		if path==None:
			path=self.path
		with open(path,"w") as fr:
			fr.truncate()
		fr.close()

	def add(self,para,value,path=None):
		'''
		添加环境变量(同时也可以修改变量值)
		参数：
			--para：环境变量名称
			--value：环境变量值
			--path：yaml文件
		Etc：
			Environment(path="../temp/environment.yaml").read_data("case_path","../../case.xls")
		'''
		if path==None:
			path=self.path
		data=self.read_data()
		if self.section_exist("Environment")==False:
			data={"Environment":{}}
		data["Environment"][para]=value
		with open(path,"w",encoding="utf-8") as fr:
			yaml.dump(data,fr)

	def set(self,value,para=None,path=None):
		"""同add()"""
		if para==None:
			para=self.para
		if path==None:
			path=self.path
		self.add(para,value,path)


	def remove(self,para=None,path=None):
		'''
		添加环境变量(同时也可以修改变量值)
		参数：
			--para：环境变量名称
			--path：yaml文件
		Etc：
			Environment(path="../temp/environment.yaml").remove("case_path")
		'''
		if path==None:
			path=self.path
		para=self.para
		data=self.read_data()
		if self.exist():
			del data["Environment"][para]
			with open(path,"w") as fr:
				yaml.dump(data,fr)




if __name__ == '__main__':
	#help(yaml)
	# Environment().add("testpath",".//")
	# Environment().add("key1","aaa")
	# Environment().add("key2","sss")
	# si=os.path.abspath("../")
	# print(os.path.abspath("../"))
	# Environment().add("key5",si)
	# si=os.path.abspath("../")
	# print(type(si))
	# Environment().add("key3",si)
	# Environment().add("key4","rrrrr")
	# print(Environment("testpath").get_value())
	print(Environment().read_data().get("Environment").get("testpath"))
	print(Environment("case_path").value)
	# with open("../temp/testsuite_tempdata/testsuite_debug/environment.yaml","rb") as fp:
	# 	line=fp.read()
	# 	print(line)
	# 	types=chardet.detect(line)
	# 	line.decode("utf-8")
	# 	print(types)
	# print(line)
	# # Environment("environment").remove()
	# # Environment().clear()

