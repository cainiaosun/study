from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time , datetime , re,os,openpyxl

class ATQtest(unittest.TestCase):
    #driver全局变量
    dr = webdriver.Firefox()
    #导入案例的路径
    case_path=r"D:\SVN专用文件夹\信贷项目\01.测试任务\2018年\9月份\02.组员\孙洪斌\模板\02.测试案例\test.xlsx"
    #案例文档名称
    filename=case_path.split("\\")[len(case_path.split("\\"))-1].split(".")[0]
    #创建案例文档的对象
    ex=openpyxl.load_workbook(case_path)
    #第一个sheet页
    sheet1=ex[ex.sheetnames[0]]
    #取得表格的总行数-1，用作分配案例的时候判断案例分配数
    rows=sheet1.max_row-1
    #C2单元格取得上线日期
    date_go_live=sheet1['C2'].value.split("日")[0]+"日"
    #拼装执行目录的名称
    demand=date_go_live+filename
    def setUp(self,driver = dr,case_path = case_path,demand = demand,rows = rows):
        self.driver =driver#设置对象
        self.base_url = "http://11.8.127.248:8080/atq/frame.jsp"#网址
        self.username='wangzhaoxia'#登录用户名
        self.demand=demand#需求名称，构成是：日期+需求名
        self.executor="王朝霞"#执行人名称
        self.case_path=case_path#导入案例的路径
        self.rows=rows#导入案例的案例数
        self.driver.implicitly_wait(1)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_01_access_url(self):
        driver = self.driver
        self.driver.get(self.base_url)

    def test_02_login(self):
        driver=self.driver
        username = self.username
        driver.find_element_by_name('loginId').clear()
        driver.find_element_by_name('loginId').send_keys(username)
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_link_text('登录').click()
        #等待
        time.sleep(5)

    def test_03_page_open(self):
        driver = self.driver
        aa=driver.find_element_by_xpath("//a/span")
        aa.find_element_by_xpath("//span[contains(text(),'案例管理')]").click()
        time.sleep(2)

    def test_04_case_import(self):
        driver = self.driver
        case_path=self.case_path
        print("")
        #切换iframe页面
        xf=driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
        driver.switch_to.frame(xf)
        WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath("//div[contains(text(),'Loading')]"))
        time.sleep(5)
        self.Loading()
   

    def Loading(self):
        self.driver.implicitly_wait(0.0001)
        driver = self.driver
        print("等待页面加载...")
        for iLoading in range(0,3000):
            try:
                if iLoading==0:
                    WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath("//div[contains(text(),'Loading')]"))
                else:
                    driver.find_element_by_xpath("//div[contains(text(),'Loading')]")
                if iLoading/100==int(iLoading/100):
                    print("加载中...")
                time.sleep(0.1)
            except:
                print("页面加载完成！")
                break
        self.driver.implicitly_wait(5)


    def isElementExist(self,by_type,element):
        flag=True
        driver=self.driver
        try:
            if by_type=="by_xpath":
                driver.find_element_by_xpath(element)
            elif by_type=="by_id":
                driver.find_element_by_id(element)
            elif by_type=="by_name":
                driver.find_element_by_name(element)
            elif by_type=="by_css":
                driver.find_element_by_css_selector(element)
            return flag
        except:
            flag=False
            return flag

    def tearDown(self):
        #self.driver.quit()#这里有多个test需要用到driver，所以tearDown中，不要关闭浏览器
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
