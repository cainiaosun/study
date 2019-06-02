from selenium import webdriver
import json
driver=webdriver.Firefox(executable_path="F:/GIT文件/Study/测试/UI自动化/Selenium/driver/firefox/geckodriver-v0.24.0-win64/geckodriver.exe")
print("begin")
with open("test.txt","w") as fp:
	fp.write(driver)

print("yes")

