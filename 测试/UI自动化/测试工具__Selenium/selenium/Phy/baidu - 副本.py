from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest


class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://11.8.121.150:7001/GDNY_CZ/logon.html'

    def test_login_as_admin(self):
        username = '000678'
        self.driver.get(self.base_url)
        self.by_name('UserID').send_keys(username)
        self.by_id('button_submit').click()
        customer=self.by_xpath("/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[2]/ul/li[1]/a/span[2]")
        ActionChains(self.driver).move_to_element(customer).perform()
        self.by_xpath("/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[2]/ul/li[1]/ul/li[3]/a/span[2]").click()
        time.sleep(10)
        self.driver.quit()


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

