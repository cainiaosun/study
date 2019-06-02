import os,sys
import configparser

current_file=os.path.abspath(__file__)
current_path=os.path.dirname(current_file)
config_file=os.path.abspath(current_path+"/../config/config.ini")

class MyConfig:
	def __init__(self,nodename=None,key=None):
		self.config=configparser.ConfigParser()
		self.config_file=config_file
		self.nodename=nodename
		self.key=key
		if nodename!=None and key!=None:
			self.value=self.read_config()

	def read_ini(self,file=None):
		file=self.config_file
		self.config.read(file,encoding="utf-8")
		return self.config

	def read_config(self,nodename=None,key=None):
		if nodename==None and key==None:
			nodename=self.nodename
			key=self.key
		self.read_ini()
		return self.config.get(nodename,key)


if __name__=="__main__":
	#config().read_ini()

	config=configparser.ConfigParser()
	config.read(config_file,encoding="utf-8")
	print(config["project"]["project_path"])
	print(config.sections())
	with open(config_file,"r",encoding="utf-8") as fp:
		print(fp.read())
	myconfig=MyConfig
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


