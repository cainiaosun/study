#from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import subprocess

#不同元素写法示例
ID元素=(By.ID,"cn.com.open.mooc:id/accountEdit")
Class元素=(By.CLASS_NAME,"android.widget.TextView")
UiSelector元素=(By.ANDROID_UIAUTOMATOR,'new UiSelector().text("登录")')#text是属性可以是：resouce-id、text、class等等，"登录"是属性值
Xpath元素_01=(By.Xpath,'//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::android.widget.RelativeLayout')
Xpath元素_02=(By.Xpath,'//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::*[@index="2"]')
#//:根目录；android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]：类节点；/：下级；..:上级目录；
#preceding-sibling::：哥哥节点；android.widget.RelativeLayout：哥哥节点下的类节点；*[@index="2"]：哥哥节点下某一属性的节点


