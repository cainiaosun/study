from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time , datetime , re,os

class ATQtest(unittest.TestCase):
    option =webdriver.FirefoxOptions()
    option.set_headless()
    dr = webdriver.Firefox(firefox_options=option)#设置对象
    #dr1 = webdriver.Firefox()#定义一个类的全局变量
    examenumber=0
    #以下是为了获取一个字符串 datestr 以用作匹配对象使用，可以简化为按月匹配，也可以用其他方式
    ##--------------------------------------------------------------
    ##--------------------------------------------------------------
    #获取当前的时间树
    datenow=time.localtime(time.time())
    #取得当前时间的年、月份、日数
    y=datenow[0]
    m=datenow[1]
    d=datenow[2]
    #获取当前月份第一天的星期数
    weekday=datetime.date(y,m,1).weekday()+1
    #判断当月第一天在周四后还是周四前，处理取得月份的第二周的周四
    if weekday>4:
        tday = 1 + (7 - weekday) + 4 + 7
        tdate = datetime.date(y, m, tday)
    else:
        tday = 1 + (4 - weekday) + 7
        tdate = datetime.date(y, m, tday)
    #判断tdate与当前日期的大小，如果tdate小于当前时间，我们重新取一个tday的值
    if (tdate-datetime.date(y,m,d)).days<0:
        tday=tday+14
    #打印我们需要获取的一个字符串，当月大于当前时间的双数周四的字符串格式日期
    datestr = str(y)+"年"+str(m)+"月"+str(tday)+"日"
    ##--------------------------------------------------------------
    ##--------------------------------------------------------------
    def setUp(self,driver = dr,datestr = datestr):#将全局变量dr赋值到setUp方法中，
        self.driver =driver#设置对象
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.base_url = "http://11.8.127.248:8080/atq/frame.jsp"#网址
        self.username='sunhongbin'#登录用户名
        self.demand=datestr#需求名称，这里只取上线日期，用作匹配最近一次日期上线所有的目录
        self.executor="孙洪斌"#执行人名称

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
        time.sleep(5)

    def test_02_openpage(self):
        driver = self.driver
        aa=driver.find_element_by_xpath("//a/span")
        aa.find_element_by_xpath("//span[contains(text(),'执行管理')]").click()

    def test_03_caseexcute(self):
        #使用到几个参数
        demand=self.demand
        executor = self.executor
        driver = self.driver
        #这里要加一个页面加载的判断
        time.sleep(5)
        #切换iframe页面
        xf=driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
        driver.switch_to.frame(xf)
        try:
            driver.find_elements_by_xpath("//span[contains(text(),'"+demand+"')]")
        except:
            print("没有找到待执行的需求目录，请检查目录是否存在，目录命名规则：XXXX年X月X日，且当前日期后当月最近一次上线日期")
        item = driver.find_elements_by_xpath("//span[contains(text(),'"+demand+"')]")
        print(len(item))
        for i in range(0,len(item)):
            print(i)
            demand=self.demand   
            item = driver.find_elements_by_xpath("//span[contains(text(),'"+demand+"')]")
            print(item[i].text)
            #名称过长，元素中心会被遮挡，点击失败，我们重新命名然后取元素
            if len(item[i].text)>28:
                demand="独特性命名（处理名称过长，点击被遮挡）"
                driver.execute_script("arguments[0].innerText='"+demand+"';",item[i])
                driver.find_element_by_xpath("//span[contains(text(),'"+demand+"')]").click()
            else:
                item[i].click()
            #这里加一个页面加载判断
            time.sleep(1)
            #查找父元素..,查找弟弟元素following-sibling::tr[1]，[1]里面的1表示最近的一个（第一个）弟弟元素，\在行尾指代换行
            #本用例刷新后，点击需求菜单展开，这里是唯一的元素，但是如果不刷新，这里可能不是唯一的
            driver.find_element_by_xpath("//span[contains(text(),'"+demand+"')]\
            /../../../following-sibling::tr[1]//span[text()='"+executor+"']").click()
            #这里可以选择性的加一下菜单是否展开的判断
            time.sleep(1)
            #实例化Select并选择
            s1=Select(driver.find_element_by_id("stat"))
            s1.select_by_index(1)
            driver.find_element_by_xpath("//a[@id='']/span/span[text()='查询']").click()
            #这里要加一个页面加载的判断
            time.sleep(5)
            for j in range(1, 1000):
                #Keys类模拟键盘发送空格键
                if self.isElementExist("by_xpath","/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/div/table/\
                tbody/tr[1]/td[2]/div/input")==False:
                    break
                driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/div/table/\
                tbody/tr[1]/td[2]/div/input").send_keys(Keys.SPACE)
                driver.find_element_by_xpath("//span[text()='执行分配案例']").click()
                #这里主要是等执行是否能被点
                time.sleep(4)
                #回到主frame页，案例执行过程
                driver.switch_to.default_content()
                for i in range(1,40):
                    time.sleep(0.5)
                    if self.is_element_present(By.ID,"allstat")==True:break
                s2=Select(driver.find_element_by_id("allstat"))
                s2.select_by_index(1)
                time.sleep(1)
                driver.find_element_by_xpath("//span[text()='保存']").click()
                time.sleep(2)
                driver.switch_to.frame(xf)
            driver.find_element_by_link_text("刷新").click()
            time.sleep(3)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True  

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

for i in range(1,2):
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
