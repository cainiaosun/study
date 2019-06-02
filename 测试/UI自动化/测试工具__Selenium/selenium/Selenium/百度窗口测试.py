from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
import time
import unittest


driver = webdriver.Ie()
driver.maximize_window()
base_url = 'http://www.baidu.com/'
driver.get(base_url)
t=time.time()
ui=driver.find_element_by_id('kw')
m=str(time.time()-t)
t=time.time()
print("定位元素用时："+m)
#driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",ui,"background:green;border:2px so lid red")
#m=str(time.time()-t)
#t=time.time()
#print("高亮元素用时："+m)
ui.clear()
m=str(time.time()-t)
t=time.time()
print("清空元素用时："+m)
ui.send_keys("测试记录")
m=str(time.time()-t)
t=time.time()
print("输入数据用时："+m)



