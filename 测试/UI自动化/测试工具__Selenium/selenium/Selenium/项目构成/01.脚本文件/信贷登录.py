from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time , datetime , re,os,sys
sys.path.append(".//")
sys.path.append(sys.path[0].split("项目构成")[0] + '项目构成/02.方法模块')
import Function_temp as F

#help(F.find_element())
help(webdriver.Firefox)

#F.driver=webdriver.Ie()

#help(F.driver)
"""
F.driver.get(r"http://11.8.121.150:7001/GDNY_CZ")
用户名=(By.NAME,"UserID")
密码=(By.NAME,"Password")
登录=(By.ID,"button_submit")
用户名.clear()
用户名.send_keys("孙洪斌")




F.find_element(用户名).clear()
F.find_element(用户名).send_keys("000678")
#F.find_element(密码).send_keys("als000???")
F.find_element(登录).click()
"""


