from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import subprocess

capabilities={
  "platformName": "Android",
  #"deviceName": "RJC5T17A25001992",
  "deviceName": "RJC5T17A25001992",
  #"app": "C:\\Users\\孙洪斌\\Downloads\\逍遥安卓下载\\mukewang_7090.apk",
  "appPackage":"cn.com.open.mooc",
  "appActivity":"com.imooc.component.imoocmain.splash.MCSplashActivity",
  "newCommandTimeout":600,
  "noReset": "true",
  "unicodeKeyboard":"False",
  "resetKeyboard":"False"
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)


"""
	--swipe():滑动屏幕
	--get_window_size():获取屏幕大小（长宽）
	--hide_keyboard():隐藏密码键盘

"""


def swipe(start_x,start_y,end_x,end_y,duration=200):
	"""
	说明：swipe()从一个点滑动到另一个点，并停留一段时间
	参数：
		--start_x：滑动起始x坐标
		--start_y：滑动起始y坐标
		--end_x：滑动终点x坐标
		--end_y：滑动终点y坐标
		--duration:完成整个滑动用时，单位：ms，默认：200
	Etc：
		swipe(500,400,50,400)
	"""
	driver.swipe(start_x,start_y,end_x,end_y,duration)

def get_window_size(which=None):
	"""
	说明：get_window_size(which)获取设备的大小（长、宽）
	参数：
		--which：获取值类型，默认为空
			which选项值：
				"height"：长
			    "width"：宽
			    None:长和宽{'width':width,'height':height}
	Etc：
		height=get_window_size("height")#获取高
	"""
	if which==None:
		return driver.get_window_size()
	elif which in ["height","width"]:
		return driver.get_window_size()[which]
	else:
		print("抛出一个错误！")

def swipe_on(direction,duration=200):
	"""
	说明：wipe_left()向指定方向整屏滑动一次
	参数：
		--direction：方向
		--duration:完成整个滑动用时，单位：ms，默认：200
	Etc：
		wipe_left()
	"""
	width=get_window_size("width")
	height=get_window_size("height")
	if direction=="left":
		rate_x1=0.9
		rate_y1=0.5
		rate_x2=0.1
		rate_y2=0.5
	elif direction=="right":
		rate_x1=0.1
		rate_y1=0.5
		rate_x2=0.9
		rate_y2=0.5
	elif direction=="up":
		rate_x1=0.5
		rate_y1=0.9
		rate_x2=0.5
		rate_y2=0.1
	elif direction=="down":
		rate_x1=0.5
		rate_y1=0.1
		rate_x2=0.5
		rate_y2=0.9
	else:
		print("这里做一个异常！")
	start_x=int(width*rate_x1)
	start_y=int(height*rate_y1)
	end_x=int(width*rate_x2)
	end_y=int(height*rate_y2)
	swipe(start_x,start_y,end_x,end_y,duration)

def hide_keyboard():
	"""
	说明：hide_keyboard()隐藏密码键盘
	参数：None
	Etc：
		hide_keyboard()
	"""
	driver.hide_keyboard()

class switch_to():
	@staticmethod
	def context(page)
		driver.switch_to.context(page)

class Element():
	"""
	说明：Element()元素定位和操作的类
	方法：
		--find_element()：定位元素并返回一个元素
		--click()：点击操作，单击左键
		--send_keys()：向元素输入一个值，输入前会先清空
	"""

	def __init__(self,locator="",driver=driver):
		self.locator=locator


	def find_element(self):
		"""
		说明：find_element()定位元素并返回一个元素
		参数：None
		Etc：
			Element((By.ID,"cn.com.open.mooc:id/accountEdit"))
			Element((By.ANDROID_UIAUTOMATOR,'new UiSelector().text("登录")'))
		"""
		locator=self.locator
		if locator[0] in [By.ID,By.CLASS_NAME,By.XPATH,By.NAME,By.TAG_NAME,By.CSS_SELECTOR,By.LINK_TEXT,\
		By.ANDROID_UIAUTOMATOR]:
			return driver.find_element(locator[0],locator[1])
		else:
			print(locator[0]+"：暂不支持的定位类型！")


	def click(self):
		"""
		说明：click()点击操作，单击左键
		参数：None
		Etc：
			Element((By.ANDROID_UIAUTOMATOR,'new UiSelector().text("登录")')).click()
		"""
		element=self.find_element()
		element.click()


	def send_keys(self,value):
		"""
		说明：send_keys()向元素输入一个值，输入前会先清空
		参数：
			--value:向元素输入的值
		Etc：
			Element((By.ID,"cn.com.open.mooc:id/accountEdit")).send_keys("18771723322")
		"""
		self.find_element().send_keys(value)





if __name__=="__main__":
	#swipe(500,400,50,400)
	#sleep(5)
	#swipe_on("left")
	#swipe_on("left")
	#swipe_on("right")
	#swipe_on("left")
	#size=get_window_size()
	#sleep(5)
	#driver.tap([(size['width']/2,size['height']/2)],1000)
	help(driver.switch_to_content)
	Element((By.ANDROID_UIAUTOMATOR,'new UiSelector().text("账号")')).click()
	Element((By.ANDROID_UIAUTOMATOR,'new UiSelector().text("点击登录")')).click()
	Element((By.ANDROID_UIAUTOMATOR,'new UiSelector().text("登录")')).click()
	Element((By.ID,"cn.com.open.mooc:id/accountEdit")).send_keys("18771723322")
	Element((By.ID,"cn.com.open.mooc:id/passwordEdit")).send_keys("shb5146955102")
	#driver.hide_keyboard()
	Element((By.ANDROID_UIAUTOMATOR,'new UiSelector().text("登录")')).click()
	sleep(5)
	#Element(("uiautomator","new UiSelector().text('点击登录')")).click()
