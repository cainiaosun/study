from selenium.webdriver.common.by import By
#[By.ID,By.CLASS_NAME,By.XPATH,By.NAME,By.TAG_NAME,By.CSS_SELECTOR,By.LINK_TEXT,By.ANDROID_UIAUTOMATOR]
#['id', 'class name', 'xpath', 'name', 'tag name', 'css selector', 'link text','-android uiautomator']
class By(By):
	ANDROID_UIAUTOMATOR='-android uiautomator'

#账号元素
account=(By.ANDROID_UIAUTOMATOR,'new UiSelector().text("账号")')
#点击登录元素
login_click=(By.ANDROID_UIAUTOMATOR,'new UiSelector().text("点击登录")')
#用户名输入框元素
username=(By.ID,"cn.com.open.mooc:id/accountEdit")
#密码输入框元素
password=(By.ID,"cn.com.open.mooc:id/passwordEdit")
#登录按钮元素
login=(By.ANDROID_UIAUTOMATOR,'new UiSelector().text("登录")')