from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
import time
import unittest


driver = webdriver.Ie()
driver.maximize_window()
base_url = 'http://11.8.121.150:7001/GDNY_CZ/logon.html'
name='000678'
driver.get(base_url)
t=time.time()
for i in range(1,100):
    time.sleep(3)
    ui=driver.find_element_by_name('UserID')
    m=str(time.time()-t)
    t=time.time()
    print("定位元素用户ID用时："+m)
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",ui,"background:green;border:2px so lid red")
    m=str(time.time()-t)
    t=time.time()
    print("高亮元素用户ID用时："+m)
    ui.clear()
    m=str(time.time()-t)
    t=time.time()
    print("清空元素用户ID用时："+m)
    ui.send_keys(name)
    m=str(time.time()-t)
    t=time.time()
    print("输入用户ID用时："+m)
    driver.find_element_by_id('button_submit').click()
    m=str(time.time()-t)
    t=time.time()
    print("定位并点击登录按钮用时："+m)
    driver.find_element_by_link_text('退出系统').click()
    m=str(time.time()-t)
    t=time.time()
    print("定位并点击退出系统按钮用时："+m)
    alert = driver.switch_to_alert()
    print(alert.text)
    alert.accept()



