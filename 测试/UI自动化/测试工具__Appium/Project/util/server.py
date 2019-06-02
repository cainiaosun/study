#coding=utf-8
import sys,time,threading,multiprocessing
sys.path.append("..")
from util.dos_cmd import DosCmd
from util.port import Port
from util.write_log import Log
from util.write_user_command import WriteUserCommand

class Server:
	def __init__(self):
		self.dos = DosCmd()
		self.device_list = self.get_devices()
		self.write_file = WriteUserCommand()
	def get_devices(self):
		'''
		获取设备信息
		'''
		Log().info("获取设备信息！")
		devices_list = []
		result_list = self.dos.excute_cmd_result('adb devices')
		if len(result_list)>=2:
			for i in result_list:
				if 'List' in i:
					continue
				devices_info = i.split('\t')
				if devices_info[1] == 'device':
					devices_list.append(devices_info[0])
			Log().info("获取设备成功，设备数："+str(len(devices_list))+"；设备列表:"+str(devices_list))
			return devices_list
		else:
			Log().warning("获取设备失败，没有找到已连接设备！")
			return None

	def create_port_list(self,start_port):
		'''
		创建可用端口
		'''
		Log().info("生成可用端口！")
		port = Port()
		port_list = []
		port_list = port.create_port_list(start_port,self.device_list)
		Log().info("可用端口生成完成，可用端口列表："+str(port_list))
		return port_list

	def create_command_list(self,i):
		'''
		生成命令
		'''
		#appium -p 4700 -bp 4701 -U 127.0.0.1:21503
		Log().info("生成Appium服务启动dos命令！")
		command_list = []
		Log().info("生成port端口")
		appium_port_list = self.create_port_list(4700)
		Log().info("生成bp端口")
		bootstrap_port_list = self.create_port_list(4900)
		device_list = self.device_list
		command = "appium -p "+str(appium_port_list[i])+" -bp "+str(bootstrap_port_list[i])+" -U "+device_list[i]+" --no-reset --session-override --log ../log/detail/log.log"
		#appium -p 4723 -bp 4726 -U 127.0.0.1:62001 --no-reset --session-override --log E:/Teacher/Imooc/AppiumPython/log/test01.log
		command_list.append(command)
		self.write_file.write_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i]))
		Log().info("生成Appium服务启动dos命令完成，命令列表："+str(command_list))
		return command_list

	def start_server(self,i):
		'''
		启动服务
		'''
		Log().info("启动Appium服务")
		self.start_list = self.create_command_list(i)
		print(self.start_list)
		self.dos.excute_cmd(self.start_list[0])
		Log().info("启动Appium服务完成,服务已关闭结束！")

	def kill_server(self):
		Log().info("关闭已启动Appium服务")
		server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
		if len(server_list)>0:
			self.dos.excute_cmd('taskkill -F -PID node.exe')
			server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
		if len(server_list)==0:
			Log().info("Appium服务关闭完成")

		else:
			Log().warning("Appium服务未全部关闭！")

	def main(self):
		thread_list = []
		#Log().info("关闭已启动Appium服务")
		self.kill_server()
		#Log().info("关清空数据")
		self.write_file.clear_data()
		#Log().info("启动所有Appium服务，设备对应")
		for i in range(len(self.device_list)):
			appium_start = threading.Thread(target=self.start_server,args=(i,))
			thread_list.append(appium_start)
		for j in thread_list:
			j.start()
		time.sleep(20)#等待启动完成



if __name__ == '__main__':
	#help(DosCmd)
	server = Server()
	#server.create_command_list
	#print(server.get_devices())
	print(server.main())
	