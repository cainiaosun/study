#coding=utf-8
import time,sys
from appium import webdriver
sys.path.append("..//04.util")
from write_user_command import WriteUserCommand
from log import Log
import server
class BaseDriver:
	def android_driver(self,i):
		print("this is android_driver:",i)
		#devices_name adb devices
		#port
		write_file = WriteUserCommand()
		devices = write_file.get_value('user_info_'+str(i),'deviceName')
		port = write_file.get_value('user_info_'+str(i),'port')
		capabilities = {
		  "platformName": "Android",
		  #"automationName":"UiAutomator2",
		  "deviceName": devices,
		  #"app": "C:\\Users\\孙洪斌\\Downloads\\逍遥安卓下载\\mukewang_7090.apk",
		  "appPackage":"cn.com.open.mooc",
		  "appActivity":"com.imooc.component.imoocmain.splash.MCSplashActivity",
		  #"noReset":"true",
		  "platforVersion":"4.4.4",
		  "appPackage":"cn.com.open.mooc"
		  #"newCommandTimeout":'180'
		}
		Log().info("设备通讯，通讯信息:{\"deviceName\":"+str(devices)+",\"port\":"+str(port)+"}")
		driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub",capabilities)
		time.sleep(10)
		return driver

if __name__=="__main__":
	server.Server().main()
	time.sleep(10)
	BaseDriver().android_driver(0)



