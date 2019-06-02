from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class ATQtest(unittest.TestCase):
    dr = webdriver.Firefox()#定义一个类的全局变量
    examenumber=0
    def setUp(self,driver = dr):#将全局变量dr赋值到setUp方法中，
        self.driver =driver#设置对象
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.base_url = "http://11.8.127.248:8080/atq/frame.jsp"#网址
        self.username='wangzhaoxia'#登录用户名
        self.demand='2018年8月23日'#需求名称，最好是带日期，以免需求名称重复
        self.executor="王朝霞"#执行人名称
        self.a=0#如果self.a=0,那么不匹配轮次，只执行一轮，如果是其他值，则匹配轮次，执行三轮

    def test_00_access_url(self):
        driver = self.driver
        self.driver.get(self.base_url)

    def test_01_login(self):
        driver=self.driver
        username = self.username
        driver.find_element_by_name('loginId').clear()
        driver.find_element_by_name('loginId').send_keys(username)
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_link_text('登录').click()
        #等待
        time.sleep(2)

    def test_02_openpage(self):
        driver = self.driver
        aa=driver.find_element_by_xpath("//a/span")
        aa.find_element_by_xpath("//span[contains(text(),'执行管理')]").click()

    def test_03_caseexcute(self):
        driver = self.driver
        #切换iframe页面
        xf=self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
        driver.switch_to.frame(xf)
        #s = self.pop_up_box()#手工输入获取需求名称，不带日期也可以，但是最好还是带日期，以免存在重复的需求名称
        excutor=self.executor
        s = self.demand
        for i in range(1,4):
            #print(self.a)
            #print(i)
            #通过拼接字符串是实现find_element的变量输入，contains()和text()方法
            if i==1:
                ss=s+"（第一轮）"
            elif i==2:
                ss = s+"（第二轮）"
            else:
                ss = s+"（回归测试）"
            #如果self.a=0,那么只循环一次后退出循环，不匹配轮次
            if self.a==0 and  i==1:
                #print("判断1")
                ss=s
            elif self.a==0 and i==2:
                #print("判断2")
                break
            driver.find_element_by_xpath("//span[contains(text(),'"+ss+"')]").click()
            #查找父元素..,查找弟弟元素following-sibling::tr[1]，[1]里面的1表示最近的一个（第一个）弟弟元素，\在行指代换行
            driver.find_element_by_xpath("//span[contains(text(),'"+ss+"')]\
            /../../../following-sibling::tr[1]//span[text()='"+excutor+"']").click()
            #实例化Select并选择
            s1=Select(driver.find_element_by_id("stat"))
            s1.select_by_index(1)
            driver.find_element_by_xpath("//a[@id='']/span/span[text()='查询']").click()
            time.sleep(5)

            for j in range(1, 500):
                #Keys类模拟键盘发送空格键
                if self.isElementExist("by_xpath","/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/div/table/\
                tbody/tr[1]/td[2]/div/input")==False:
                    break
                driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/div/table/\
                tbody/tr[1]/td[2]/div/input").send_keys(Keys.SPACE)
                driver.find_element_by_xpath("//span[text()='执行分配案例']").click()
                time.sleep(4)
                #回到主frame页
                driver.switch_to.default_content()
                s2=Select(driver.find_element_by_id("allstat"))
                s2.select_by_index(1)
                time.sleep(1)
                driver.find_element_by_xpath("//span[text()='保存']").click()
                time.sleep(2)
                driver.switch_to.frame(xf)
        print("运行正常，执行结束！")
        ATQtest.examenumber = 1#此处校验值，用于后面校验是否完全执行完毕


    # 弹出一个窗口并返回输入的值
    def pop_up_box(self):
        import tkinter
        def input():
            try:
                root.destroy()
            except:
                num = "异常处理！"

        def inputclear():
            var.set('')

        root = tkinter.Tk()
        root.title("输入框")
        root.geometry("250x130")

        l1 = tkinter.Label(root, text='请输入需求名称')
        l1.pack()
        var = tkinter.StringVar()
        var.set("")
        entry1 = tkinter.Entry(root, textvariable=var)
        entry1.pack()
        btn1 = tkinter.Button(root, text="提交", command=input)
        btn2 = tkinter.Button(root, text="清空", command=inputclear)
        btn2.pack(side='right')
        btn1.pack(side='right')
        root.mainloop()
        return var.get()

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
        #self.driver.quit()#这里有多个test需要用到driver，所以tearDown中，不要关闭浏览器
        self.assertEqual([], self.verificationErrors)

for i in range(1,100):
    if i>1:
        print("第"+str(i-1)+"次错误循环执行！")
    if __name__:
        suite = unittest.TestSuite()#获取套件
        suite.addTest(ATQtest('test_00_access_url'))#添加案例，访问网址
        if i==1:
            suite.addTest(ATQtest('test_01_login'))#添加案例，如果出现错误循环，执行'test_00_access_url'仍处于登录状态，不需要执行此步骤
        suite.addTest(ATQtest('test_02_openpage'))#添加案例，打开案例执行页面
        suite.addTest(ATQtest('test_03_caseexcute'))#添加案例，打开对应的未执行案例，并执行，执行完全结束后，赋值ATQtest.examenumber=1
        runner=unittest.TextTestRunner()#
        runner.run(suite)#执行套件
        print("校验数字是："+str(ATQtest.examenumber))
        if ATQtest.examenumber==1:#如果校验数字是1，即完全执行成功，那么退出循环，否则循环继续执行
            break
