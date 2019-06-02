from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time , datetime , re,os,sys
sys.path.append(".//")
sys.path.append(sys.path[0].split("ATQ项目")[0] + 'ATQ项目\\02.方法模块')
import Function_temp  as F



print(os.path.split(webdriver.__file__))