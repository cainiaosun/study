from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time , datetime , re,os,openpyxl

class ATQtest(unittest.TestCase):
    dr = webdriver.Firefox()#定义一个类的全局变量
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
        self.username='wangzhaoxia'#登录用户名
        self.demand=datestr#需求名称，这里只取上线日期，用作匹配最近一次日期上线所有的目录
        self.executor="王朝霞"#执行人名称

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
        time.sleep(2)

    def test_03_caseassign(self):
        driver = self.driver
        print("")
        de=self.demand
        executor=self.executor
        for iLoop in range(0,3):
            if iLoop==0:
                demand=de+""
            elif iLoop==1:
                damand=de+""
            else:
                demand=de+""
            #切换iframe页面
            xf=driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
            driver.switch_to.frame(xf)
            time.sleep(5)
            print("等待案例执行目录页面的加载...")
            for i in range(0,10):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    time.sleep(2)
                else:
                    print("案例执行目录页面加载完成！")
                    break
            #增加轮次轮次
            driver.find_element_by_xpath("//span[text()='增加轮次']").click()
            #输入轮次名称，并点击保存
            driver.find_element_by_id("turnName").send_keys(demand)
            driver.find_element_by_xpath("//span[text()='保存']").click()
            time.sleep(0.1)
            #等待Loading元素消失，判断保存是否完成
            for i in range(0,20):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    if i==0:
                        print("新增轮次保存中...")
                    time.sleep(1)
                else:
                    print("保存完成！")
                    time.sleep(1)
                    break
            item = driver.find_element_by_xpath("//span[text()='"+demand+"']")
            print("创建的目录："+item.text)
            #点击新创建的案例执行目录
            if len(item.text)>28:
                #临时修改demand
                tempdemand=demand
                demand="独特性命名（处理名称过长，点击被遮挡）"
                driver.execute_script("arguments[0].innerText='"+demand+"';",item)
                driver.find_element_by_xpath("//span[text()='"+demand+"']").click()
            else:
                item.click()
            #聚焦到执行人元素上，点击鼠标右键，然后点击分配案例
            exme=driver.find_element_by_xpath("//span[contains(text(),'"+demand+"')]\
                /../../../following-sibling::tr[1]//span[text()='"+executor+"']")
            #demand临时数据使用完毕，恢复原值
            demand=tempdemand
            ActionChains(driver).move_to_element(exme).context_click().perform()
            driver.find_element_by_xpath("//div[contains(text(),'分配案例')]").click()
            #回到主frame页
            driver.switch_to.default_content()
            #检查页面加载是否完成
            for i in range(0,60):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    if i==0:
                        print("案例页面加载中...")
                    time.sleep(1)
                else:
                    print("案例页面加载完成！")
                    time.sleep(1)
                    break
            #选择案例执行数量
            print("选择案例执行数...")
            seno=driver.find_elements_by_xpath("//select")
            Select(seno[1]).select_by_index(2)
            #检查页面加载是否完成
            for i in range(0,60):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    if i==0:
                        print("案例页面加载中...")
                    time.sleep(1)
                else:
                    print("案例页面加载完成！")
                    time.sleep(1)
                    break
            #循环勾选案例，并在勾选完成后点击确认,弹出窗口后点击"确定"
            print("勾选案例...")
            for i in range(0,1):
                driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-"+str(i)+"']/td/div/input").click()
            time.sleep(1)
            print("勾选完成！")
            driver.find_element_by_xpath("//span[text()='确认']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//span[text()='确定']").click()
            #判断确定后点击确定后，勾选页面是否跳出
            for i in range(0,100):
                confirm=driver.find_elements_by_xpath("//span[text()='确认']")
                if len(confirm)==0:
                    break
                else:
                    time.sleep(2)
            #切换iframe页面  
            driver.switch_to.frame(xf)
            #等待页面跳转后，页面的加载
            print("等待页面加载...")
            for i in range(0,10):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    time.sleep(2)
                else:
                    print("页面加载完成！")
                    break
            #刷新一下案例执行目录页面
            driver.find_element_by_link_text("刷新").click()
                    #等待页面跳转后，页面的加载
            print("等待页面加载...")
            for i in range(0,10):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    time.sleep(0.5)
                else:
                    print("页面加载完成！")
                    break
            #点击进入目录树,并获取分配案例的数量
            driver.find_element_by_xpath("//span[text()='"+demand+"']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//span[contains(text(),'"+demand+"')]/../../../following-sibling::tr[1]\
                 //span[text()='"+executor+"']/../../following-sibling::td[1]/div").get_attribute("textContent")
            if text!="":
                print("案例分配成功，分配数量："+text)
            #回到主frame页
            driver.switch_to.default_content()
        
        

        
       

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

