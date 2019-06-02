import configparser,os

class OperateIni:
	def __init__(self):
		self.config=configparser.ConfigParser()

	def add_node(self,nodename):
		self.config.add_section(nodename)

	def add_alter(self,nodename,key,value):
		self.config.set(nodename,key,value)

	def read_ini(self,file):
		return self.config.readfp(open(file,"r",encoding="utf-8"))

	def read_value(self,nodename,key):
		self.config.get(nodename,key)

	def test(self):
		print("test") 

if __name__=="__main__":
	path="../config/LocalElement.ini"
	# config=configparser.ConfigParser()
	# print(config)
	#config["default"]=open(path,"r",encoding="utf-8").read()
	# config.read(path)
	# print(config.defaults())
	# print(config.get("LocalElement","account"))
	# print("cofing is:"+str(config.read(path)))
	# print("path is:"+os.path.abspath(path))
	# print("read_ini is:"+str(OperateIni().read_ini(path)))
	with open(path,"r",encoding="utf-8") as fp:
		line=fp.read()
	print(line)
	OperateIni().read_ini(path)
	OperateIni().add_node("Login_element")
	print(OperateIni().read_value("Login_element","account"))
	# with open("./test.ini","w") as fp:
	# 	configparser.ConfigParser().write("file")
	


