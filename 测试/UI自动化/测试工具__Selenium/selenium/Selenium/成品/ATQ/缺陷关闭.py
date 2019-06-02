from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class UntitledTestCase(unittest.TestCase):
    option =webdriver.FirefoxOptions()
    option.set_headless()
    dr = webdriver.Firefox(firefox_options=option)#设置对象
    #dr1 = webdriver.Firefox()#设置对象
    def setUp(self,driver=dr):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.base_url = "http://11.8.127.248:8080/atq/frame.jsp"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver=self.driver
        username = 'sunhongbin'
        driver.get(self.base_url)
        driver.find_element_by_name('loginId').clear()
        driver.find_element_by_name('loginId').send_keys(username)
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_link_text('登录').click()
        #等待
        time.sleep(2)
        aa=driver.find_element_by_xpath("//a/span")
        aa.find_element_by_xpath("//span[contains(text(),'缺陷管理')]").click()
        #切换iframe页面
        xf=self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
        driver.switch_to.frame(xf)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr/td/"
                                             "span[5]/input[1]").click()
        self.driver.find_element_by_xpath("/html/body/div[9]/div/div[contains(text(),'待验证')]").click()
        #查询条件选项选择第 1 个，即：测试人
        Select(self.driver.find_element_by_id("key")).select_by_index(1)
        #输入测试人名称
        self.driver.find_element_by_name("data").send_keys("孙洪斌")
        #等待3s加载后，点击查询
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr/td/a[1]/span/span").click()
        time.sleep(5)
        for i in range(1,50):
            #print(self.is_element_present(By.XPATH, "/html/body/div[1]/div[2]/form/table/tbody/tr/td/a[1]/span/span"))
            #print(self.is_element_present(By.XPATH, "//tr[@id='datagrid-row-r2-1-0']/td[@field='bugTitle']"))
            if self.is_element_present(By.XPATH, "//tr[@id='datagrid-row-r2-1-0']/td[@field='bugTitle']") == False:
                break
            #选择待处理缺陷的第一条处理
            self.driver.find_element_by_xpath("//tr[@id='datagrid-row-r2-1-0']/td[@field='bugTitle']").click()
            #切换回主frame页
            driver.switch_to.default_content()
            #点击选择缺陷状态为：关闭
            driver.find_element_by_xpath("//div[@id='djDiag']/div/div/div/div/div/span/span/span").click()
            driver.find_element_by_xpath("//div[@id='djDiag']/../following-sibling::div[4]/div/div[2]").click()
            #点击确定
            driver.find_element_by_xpath("//div[@id='djDiag']/div/div/div/div/div/a/span/span").click()
            #填写解决说明
            driver.find_element_by_id("dlgNote").send_keys("已解决")
            # 点击确定
            driver.find_element_by_xpath("//div[@id='dd']/div[2]/a/span").click()
            driver.switch_to.frame(xf)
            time.sleep(3)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
