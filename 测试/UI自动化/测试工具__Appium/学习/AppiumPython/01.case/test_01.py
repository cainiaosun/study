#coding=utf-8
from __init import *

F.driver=F.get_driver()
F.Element(login_page.account).click()
F.Element(login_page.login_click).click()
F.Element(login_page.login).click()
F.Element(login_page.username).send_keys("18771723322")
F.Element(login_page.password).send_keys("shb5146955102")
#driver.hide_keyboard()
F.Element(login_page.login).click()


