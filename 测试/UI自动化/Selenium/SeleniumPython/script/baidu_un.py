from selenium import webdriver
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("www.baidu.com")
driver.find_element_by_id().text