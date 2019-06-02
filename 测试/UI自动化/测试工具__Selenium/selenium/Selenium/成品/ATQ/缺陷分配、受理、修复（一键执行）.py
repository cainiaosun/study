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
    #dr = webdriver.Firefox()#设置对象
    def setUp(self,driver=dr):
        #获取参数
        self.driver = driver
        #隐式等待
        self.driver.implicitly_wait(8)
        #需要访问的网址
        self.base_url = "http://11.8.127.248:8080/atq/frame.jsp"
        #测试人员
        self.excutor=("孙洪斌","王朝霞","袁小云")
        #开发人员（吴龙飞、李云鹏、吴豪波、朱文军、朱俊杰、杨瞻、莫厅川、刘勇、钟启明）
        self.developer=("朱俊杰","钟启明","钟启明")
        self.verificationErrors = []
        self.accept_next_alert = True
        
    #登录案例
    def test_01_login(self):
        #简写self.driver
        driver=self.driver
        #项目经理王华洲姓名
        username = 'wanghuazhou'
        #访问
        driver.get(self.base_url)
        #清空用户名
        driver.find_element_by_name('loginId').clear()
        #输入用户名
        driver.find_element_by_name('loginId').send_keys(username)
        #清空密码
        driver.find_element_by_name('password').clear()
        #输入密码
        driver.find_element_by_name('password').send_keys('123456')
        #点击登录
        driver.find_element_by_link_text('登录').click()
        #等待2s，以待登录成功
        time.sleep(3)

    #进入缺陷菜单页面案例
    def test_02_topage(self):
        #简写self.driver
        driver=self.driver
        #点击测试管理菜单，然后点击缺陷管理菜单
        driver.find_element_by_xpath("//div[text()='测试管理']").click()
        aa=driver.find_element_by_xpath("//a/span")
        aa.find_element_by_xpath("//span[contains(text(),'缺陷管理')]").click()
            
    #处理新提出待分配缺陷的案例
    def test_03_new(self):
        #简写self.driver
        driver=self.driver
        #切换iframe页面
        xf=self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
        driver.switch_to.frame(xf)
        #点击选择缺陷状态
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr/td/"
                                             "span[5]/input[1]").click()
        self.driver.find_element_by_xpath("/html/body/div[9]/div/div[contains(text(),'提出')]").click()
        for i in range(0,3):
            print("测试人:"+self.excutor[i]+"；开发人:"+self.developer[i]+".")
            #查询条件选项选择第 1 个，即：测试人
            Select(self.driver.find_element_by_id("key")).select_by_index(1)
            #清空内容，输入测试人名称
            self.driver.find_element_by_name("data").clear()
            self.driver.find_element_by_name("data").send_keys(self.excutor[i])
            #等待3s加载后，点击查询
            time.sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr/td/a[1]/span/span").click()
            time.sleep(5)
            #循环选择分配缺陷
            for j in range(1,50):
                #判断是否有可处理的缺陷，如果没有那么终止循环
                if self.is_element_present(By.XPATH, "//tr[@id='datagrid-row-r2-1-0']/td[@field='bugTitle']") == False:
                    break
                #选择待处理缺陷的第一条处理
                self.driver.find_element_by_xpath("//tr[@id='datagrid-row-r2-1-0']/td[@field='bugTitle']").click()
                #切换回主frame页
                driver.switch_to.default_content()
                #点击选择缺陷状态为：关闭
                driver.find_element_by_xpath("//div[@id='djDiag']/div/div/div/div/div/span/span/span").click()
                driver.find_element_by_xpath("//div[@id='djDiag']/../following-sibling::div[4]/div/div[1]").click()
                #点击选择开发人员
                driver.find_element_by_xpath("//span[@id='fp']/span/span/span").click()
                time.sleep(1)
                #因为这里定位到的缺陷分配人是多个，而且元素数量、次序、xpath等都不固定，但是只有需要的哪个元素一个是没有被遮住可以点击的，
                #所以我们在这里循环点击元素集所有的元素，判断异常，直到点击成功以后退出循环
                de=driver.find_elements_by_xpath("//div[text()='"+self.developer[i]+"']")
                for k in range(0,len(de)):
                    try:
                        de[k].click()
                        break#如果点击成功不报错的话，就中止循环
                    except:
                        "不做任何事情，只有在最后一次循环仍异常的情况下提示选项问题"
                        if k==len(de)-1:
                            print("开发人员不在可选项中！")
                #点击确定
                driver.find_element_by_xpath("//div[@id='djDiag']/div/div/div/div/div/a/span/span").click()
                #切回xf页面，以供后需求操作
                driver.switch_to.frame(xf)
                time.sleep(3)

    #处理已分配需受理缺陷的案例
    def test_04_assigned(self):
        #简写self.driver
        driver=self.driver
        #切换回主frame页
        driver.switch_to.default_content()
        #切换iframe页面
        xf=self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
        driver.switch_to.frame(xf)
        #点击选择缺陷装填
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr/td/"
                                             "span[5]/input[1]").click()
        self.driver.find_element_by_xpath("/html/body/div[9]/div/div[contains(text(),'分配')]").click()
        #清空测试人
        self.driver.find_element_by_name("data").clear()
        time.sleep(2)
        #点击查询
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr/td/a[1]/span/span").click()
        time.sleep(5)
        #循环受理缺陷
        for i in range(1,50):
            #判断没有缺陷可处理时，退出循环
            if self.is_element_present(By.XPATH, "//tr[@id='datagrid-row-r2-1-0']/td[@field='bugTitle']") == False:
                break
            #选择待处理缺陷的第一条处理
            self.driver.find_element_by_xpath("//tr[@id='datagrid-row-r2-1-0']/td[@field='bugTitle']").click()
            #切换回主frame页
            driver.switch_to.default_content()
            #因为已默认选择了受理，这里直接点击确认
            driver.find_element_by_xpath("//div[@id='djDiag']/div/div/div/div/div/a/span/span").click()
            driver.switch_to.frame(xf)
            time.sleep(3)

    #处理已分配打开的缺陷案例
    def test_05_open(self):
        #简写self.driver
        driver=self.driver
        #切换回主frame页
        driver.switch_to.default_content()
        #切换iframe页面
        xf=self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
        driver.switch_to.frame(xf)
        #点击选择缺陷状态
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr/td/"
                                             "span[5]/input[1]").click()
        self.driver.find_element_by_xpath("/html/body/div[9]/div/div[contains(text(),'受理')]").click()
        #清空测试人
        self.driver.find_element_by_name("data").clear()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a/span/span[text()='查询']").click()
        time.sleep(5)
        #循环处理缺陷
        for i in range(1,50):
            if self.is_element_present(By.XPATH, "//tr[@id='datagrid-row-r2-1-0']/td[@field='bugTitle']") == False:
                break
            #选择待处理缺陷的第一条处理
            self.driver.find_element_by_xpath("//tr[@id='datagrid-row-r2-1-0']/td[@field='bugTitle']").click()
            #切换回主frame页
            driver.switch_to.default_content()
            #点击选择缺陷状态为：关闭
            driver.find_element_by_xpath("//div[@id='djDiag']/div/div/div/div/div/span/span/span").click()
            driver.find_element_by_xpath("//div[@id='djDiag']/../following-sibling::div[4]/div/div[2]").click()
            #点击确定关闭提示对话框
            driver.find_element_by_xpath("//div[text()='请确认缺陷起源!']/../div/a").click()
            #点击选择处理状态
            driver.find_element_by_xpath("//span[@id='dyz']/span/span/span").click()
            time.sleep(0.2)
            driver.find_element_by_xpath("//div[text()='已解决']").click()
            #点击弹出框确定
            driver.find_element_by_xpath("//div[@id='djDiag']/div/div/div/div/div/a/span/span").click()
            #填写解决说明并点击确定
            driver.find_element_by_id("dlgNote").send_keys("已解决")
            driver.find_element_by_xpath("//div[@id='dd']/div[2]/a").click()
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

    def close_alert_and_get_its_text(selSf):
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
