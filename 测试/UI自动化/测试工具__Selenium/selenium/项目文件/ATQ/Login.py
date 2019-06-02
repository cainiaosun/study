from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest


class login(unittest.TestCase):

    def setUp(self):
        self.driver =webdriver.Firefox()
        self.base_url = 'http://11.8.127.248:8080/atq'

    def test_login_as_admin(self):
        username = 'sunhongbin'
        self.driver.get(self.base_url)
        self.by_name('loginId').clear()
        self.by_name('loginId').send_keys(username)
        self.by_name('password').send_keys('123456')
        self.driver.find_element_by_link_text('登录').click()

        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/ul/li[3]/a/span/span").click()
        self.driver.find_element_by_xpath("//ul[@id='nav']/li[3]/a/span/span").click()
        driver.find_element_by_xpath("//ul[@id='nav']/li[3]/a/span/span").click()

 #       time.sleep(3)
 #       self.driver.quit()




    def by_id(self, id):
        return self.driver.find_element_by_id(id)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

if __name__ == '__main__':
    unittest.main()