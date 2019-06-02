from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest


class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie()
        self.base_url = 'http://11.8.121.150:7001/GDNY_CZ/logon.html'
        self.name='000678'

    def test_login_as_admin(self):
        self.driver.get(self.base_url)
        ui=self.by_name('UserID')
        self.highlight(ui)
        ui.clear()
        ui.send_keys(self.name)
        self.by_id('button_submit').click()
        time.sleep(5)
        customer=self.by_xpath("//a/span[text()='客户管理']")
        self.highlight(customer)
        time.sleep(5)
        ActionChains(self.driver).move_to_element(customer).perform()
        intcustomer=self.by_xpath("//span[text()='个人客户管理']")
        self.highlight(intcustomer)
        time.sleep(5)
        intcustomer.click()
        self.driver.switch_to.frame("right")
        button1=self.driver.find_element_by_xpath("//td[text()='新增']")
        self.highlight(button1)
        time.sleep(4)
        button1.click()
        hs=self.driver.window_handles
        print(hs)
        hs = self.driver.window_handles
        print("开始")
        print(hs)
        self.driver.switch_to.window(hs[1])
        self.driver.find_element_by_name("CertID").send_keys("511423198805150019")
        self.driver.find_element_by_name("CertID1").send_keys("511423198805150019")
        self.driver.find_element_by_name("CustomerName").send_keys("测试十")
        self.driver.find_element_by_name("next").click()
        self.driver.switch_to.window(hs[0])
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        print(self.driver.current_window_handle)
        ppx=self.driver.window_handles
        print("结束")
        print(ppx)
        self.driver.switch_to.window(ppx[1])
        es=self.driver.find_elements_by_xpath("//iframe")
        len(es)
        for i in range (0,len(es)):
            print(es[i].get_attribute("name"))
        print("第二次")
        es=self.driver.find_elements_by_xpath("//iframe")
        len(es)
        for i in range (0,len(es)):
            print(es[i].get_attribute("name"))
            self.driver.switch_to.frame(es[i].get_attribute("name"))
            print(self.driver.page_source)


        #self.driver.find_element_by_xpath("//input[text()='确认']").click()

        time.sleep(3)
        #self.driver.quit()


    def by_id(self, id):
        return self.driver.find_element_by_id(id)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    def highlight(self,element):
        self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,"background:green;border:2px so lid red")


if __name__ == '__main__':
    unittest.main()