import sys,time
from selenium.webdriver.common.by import By
sys.path.append("..//04.util")
import Function as F#"..//04.util//Function.py"
sys.path.append("..//05.page")
import login_page

def to_login_page():
	#F.driver=F.get_driver()
	F.Element(login_page.account).click()
	F.Element(login_page.login_click).click()
	F.Element(login_page.login).click()
	result=F.Elements(login_page.username).count()
	return result

def login_sucess():
	F.Element(login_page.username).send_keys("18771723322")
	F.Element(login_page.password).send_keys("shb5146955102")
	#driver.hide_keyboard()
	F.Element(login_page.login).click()
	result=F.Elements(login_page.username).count()
	return result