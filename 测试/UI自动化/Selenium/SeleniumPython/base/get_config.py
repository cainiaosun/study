import os,sys
import configparser

current_file=os.path.abspath(__file__)
current_path=os.path.dirname(current_file)
config_file=os.path.abspath(current_path+"/../config/config.ini")

class MyConfig:
	def __init__(self,section=None,option=None):
		self.config=configparser.ConfigParser()
		self.config_file=config_file
		self.section=section
		self.option=option
		if section!=None and option!=None:
			self.value=self.read_config()

	def read_ini(self,file=None):
		file=self.config_file
		self.config.read(file,encoding="utf-8")
		return self.config

	def read_config(self,section=None,option=None):
		if section==None and option==None:
			section=self.section
			option=self.option
		self.read_ini()
		return self.config.get(section,option)

	#外部尽量不要调用
	def write(self):
		with open(config_file,"w",encoding="utf-8") as fp:
			self.config.write(fp)

	def add_section(self,section):
		self.read_ini()
		if self.config.has_section(section)==False:
			self.config.add_section(section)
			self.write()

	def remove_section(self,section):
		self.read_ini()
		if self.config.has_section(section):
			self.config.remove_section(section)
			self.write()

	def sections(self):
		self.read_ini()
		return self.config.sections()

	def set(self,section,option,value):
		if self.config.has_section(section)==False:
			self.add_section(section)
		self.config.set(section,option,value)
		self.write()

if __name__=="__main__":
	#config().read_ini()
	
	config=configparser.ConfigParser()
	config.read(config_file,encoding="utf-8")
	print(config["project"]["project_path"])
	print(config.sections())
	with open(config_file,"r",encoding="utf-8") as fp:
		print(fp.read())
	myconfig=MyConfig
	# myconfig().add_section("if")
	myconfig().remove_section("if")
	myconfig().set("my","key1","value")
	myconfig().remove_section("my")
	print("sections is:",myconfig().sections())	
	project_path=myconfig().read_config("project","project_path")
	project_path=myconfig("project","project_path").value
	report_path=myconfig().read_config("project","report_path")
	log_path=myconfig().read_config("project","log_path")
	data_path=myconfig().read_config("project","data_path")
	report_path=project_path+report_path
	log_path=project_path+log_path
	data_path=project_path+data_path
	print("报告路径："+report_path)
	print("日志路径："+log_path)
	print("运行数据路径："+data_path)


