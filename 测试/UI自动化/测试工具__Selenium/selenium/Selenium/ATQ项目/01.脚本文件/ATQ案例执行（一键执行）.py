from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time , datetime , re,os,sys
sys.path.append(".//")
sys.path.append("sys.path[0].split("项目构成")[0] + '项目构成/02.方法模块'")
import Function as F,ATQ案例执行页面 as P

class ATQtest(unittest.TestCase):
    dr = webdriver.Firefox()#定义一个类的全局变量
    F.driver=dr
    def setUp(self,driver = dr):#将全局变量dr赋值到setUp方法中，
        self.driver =driver#设置对象
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.base_url = "http://11.8.127.248:8080/atq/frame.jsp"#网址
        self.username='sunhongbin'#登录用户名
        self.executor="孙洪斌"#执行人名称

    def test_00_access_url(self):
        driver = self.driver
        self.driver.get(self.base_url)

    def test_01_login(self):
        driver=self.driver
        username = self.username
        F.find_element(P.用户名输入框).clear()
        F.find_element(P.用户名输入框).send_keys(username)
        F.find_element(P.密码输入框).send_keys("123456")
        F.find_element(P.登录按钮).click()
        #等待
        time.sleep(5)

    def test_02_openpage(self):
        driver = self.driver
        F.find_element(P.执行管理菜单).click()

    def test_03_caseexcute(self):
        demand=self.demand
        executor = self.executor
        driver = self.driver
        time.sleep(5)
        xf=F.find_element(P.iframe)
        driver.switch_to.frame(xf)
        try:
            F.find_element(P.案例执行菜单集(demand))
        except:
            print("没有找到待执行的需求目录，请检查目录是否存在，目录命名规则：XXXX年X月X日，且当前日期后当月最近一次上线日期")
        item = F.find_elements(P.案例执行菜单集(demand))
        print(len(item))
        for i in range(0,len(item)):
            print(i)
            demand=self.demand   
            item = F.find_elements(P.案例执行菜单集(demand))
            print(item[i].text)
            if len(item[i].text)>28:
                demand="独特性命名（处理名称过长，点击被遮挡）"
                driver.execute_script("arguments[0].innerText='"+demand+"';",item[i])
                F.find_element(P.案例执行菜单(demand)).click()
            else:
                item[i].click()
            time.sleep(1)
            F.find_element(P.执行人子菜单(demand,executor)).click()
            time.sleep(1)
            s1=Select(F.find_element(P.案例状态选项))
            s1.select_by_index(1)
            F.find_element(P.查询按钮).click()
            time.sleep(5)
            for j in range(1, 1000):
                if F.is_element_present(P.待执行案例)==False:break
                F.find_element(P.待执行案例勾选框).send_keys(Keys.SPACE)
                F.find_element(P.执行分配案例按钮).click()
                time.sleep(4)
                driver.switch_to.default_content()
                for i in range(1,20):
                    time.sleep(0.5)
                    if F.is_element_present(P.步骤)==True:break
                s2=Select(F.find_element(P.案例执行选项))
                s2.select_by_index(1)
                time.sleep(1)
                F.find_element(P.保存按钮).click()
                time.sleep(2)
                driver.switch_to.frame(xf)
            F.find_element(P.刷新按钮).click()
            time.sleep(3)

    def tearDown(self):
        #self.driver.quit()#这里有多个test需要用到driver，所以tearDown中，不要关闭浏览器
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()