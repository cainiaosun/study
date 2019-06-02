from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time , datetime , re,os,sys
sys.path.append(".//")
sys.path.append(sys.path[0].split("项目构成")[0] + '项目构成\\02.方法模块')
t=time.time()
import Function_temp as F,ATQ案例执行页面 as P,鼠标键盘事件 as M

class ATQtest(unittest.TestCase):
    dr = webdriver.Firefox()#定义一个类的全局变量
    #dr = webdriver.Ie()#定义一个类的全局变量
    F.driver=dr
    F.relay=1
    def setUp(self,driver = dr):#将全局变量dr赋值到setUp方法中，
        self.driver =driver#设置对象
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.base_url = "http://11.8.127.248:8080/atq/frame.jsp"#网址
        self.username='sunhongbin'#登录用户名
        self.executor="孙洪斌"#执行人名称
        self.driver.get(self.base_url)
        

    def test_01_size(self):
        element1=F.find_element(P.语言选择框).element()
        #测试左键点击方法带参数
        print(element1.size)
        print(element1.location)


        '''
        F.find_element(P.语言选择框).left_click()
        time.sleep(30)
        print(F.find_element(P.用户名输入框).exists(10))
        F.find_element(P.用户名输入框).clear()
        F.find_element(P.用户名输入框).send_keys(username)
        F.find_element(P.密码输入框).send_keys("123456")
        F.find_element(P.登录按钮).send_keys("123456")
        '''
        #u=driver.command_executor._url
        #s=driver.session_id
        #print(driver.command_executor._url)
        #print(driver.session_id)
        #等待
        #time.sleep(8)
        #driver2=webdriver.Remote(command_executor=u,desired_capabilities={})
        #driver2.session_id=s
        #pirnt(driver2.current_url)

    def tearDown(self):
        #self.driver.quit()#这里有多个test需要用到driver，所以tearDown中，不要关闭浏览器
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()#获取套件
    suite.addTest(ATQtest('test_01_size'))#添加案例，访问网址
    runner=unittest.TextTestRunner()#
    runner.run(suite)#执行套件