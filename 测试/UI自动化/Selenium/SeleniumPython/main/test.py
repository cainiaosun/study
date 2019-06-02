from selenium.webdriver import Firefox
# driver=Firefox()
# driver.get("https://www.baidu.com")
for i in range(2,5):
	driver=Firefox(executable_path="F:/GIT文件/Study/测试/UI自动化/Selenium/driver/firefox/geckodriver-v0.2"+str(i)+".0-win64/geckodriver.exe")
	driver.get("https://www.baidu.com")
# help(Firefox)