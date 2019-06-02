from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
        self.driver.implicitly_wait(5)
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
        time.sleep(5)
        print("等待【案例管理_案例列表】页面加载...")
        for i in range(0,10):
            refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
            if len(refresh)<2:
                print("【案例管理_案例列表】页面加载完成！")
                driver.find_element_by_xpath("//span[text()='导入案例']").click()
                break
            else:
                time.sleep(3)
        time.sleep(2)
        #上传按钮
        upload=driver.find_element_by_id("upload")
        upload.send_keys(case_path)
        value=upload.get_attribute('value')
        if value!="":
            print("文件上传成功！")
        driver.find_element_by_xpath("//span[text()='确定']").click()
        time.sleep(2)
        #判断页面的元素检查是否正在导入，默认先等30s
        if len(driver.find_elements_by_xpath("//div[contains(text(),'导入中，请稍候')]"))>0:
            print("导入中，请耐心等候...")
            time.sleep(30)
        #30s后通过判断导入结束的弹出窗口判断是否导入完毕，如果没有找到窗口则等待继续寻找窗口，直至寻找成功
        #回到主frame页
        driver.switch_to.default_content()
        for i in range(0,100):
            try:
                text=driver.find_element_by_xpath("/html/body/div[10]/div[2]").text
                print("案例导入完毕！")
                break
            except:
                time.sleep(0.01)
        time.sleep(5)
        #通过判断Loading元素，目录树页面是否加载成功，如果未加载成功则等待2s，反复循环
        self.driver.switch_to.frame(xf)
        print("等待【案例管理_案例目录】页面加载...")
        for i in range(0,100):
            refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
            if len(refresh)>0:
                time.sleep(2)
            else:
                print("【案例管理_案例目录】页面加载完成！")
                break
        #创建excel对象并取excel中的数据去判断目录树对应的目录是否已经存在，以此判断案例是否导入成功
        ex=openpyxl.load_workbook(case_path)
        sh=ex[ex.sheetnames[0]]
        print("案例目录检查...")
        if self.isElementExist("by.xpath","//span[text()='"+sh['C2'].value+"']/../../../following-sibling::tr[1]//span[text()='"+sh['D2'].value+"']"):
            print("案例目录检查完毕，案例目录存在，案例导入成功！")
        else:print("案例目录检查完毕，未发现案例目录，案例导入失败！")
        #回到主frame页
        driver.switch_to.default_content()
        time.sleep(5)

    def test_05_access_url(self):
        driver = self.driver
        self.driver.get(self.base_url)

    def test_06_page_open(self):
        driver = self.driver
        aa=driver.find_element_by_xpath("//a/span")
        aa.find_element_by_xpath("//span[contains(text(),'执行管理')]").click()
        time.sleep(2)

    def test_07_case_assign(self):
        driver = self.driver
        print("")
        de=self.demand
        executor=self.executor
        number=self.rows
        for iLoop in range(0,3):
            if iLoop==0:
                demand=de+"（第一轮）"
                case_num=number
            elif iLoop==1:
                demand=de+"（第二轮）"
                case_num=int(number*0.65)+1
            else:
                demand=de+"（回归测试）"
                case_num=int(number*0.45)+1
            #切换iframe页面
            xf=driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
            driver.switch_to.frame(xf)
            time.sleep(5)
            print("等待【执行管理_案例目录】页面加载...")
            for i in range(0,10):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    time.sleep(2)
                else:
                    print("【执行管理_案例目录】页面加载完成！")
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
            tempdemand=""
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
            #移动滚动条到元素显示范围
            driver.execute_script("arguments[0].scrollIntoView();",exme)
            ActionChains(driver).move_to_element(exme).context_click().perform()
            driver.find_element_by_xpath("//div[contains(text(),'分配案例')]").click()
            #demand临时数据使用完毕，恢复原值
            if tempdemand!="":
                demand=tempdemand
            #回到主frame页
            driver.switch_to.default_content()
            #检查页面加载是否完成
            for i in range(0,60):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    if i==0:
                        print("【案例分配_案例列表】页面加载中...")
                    time.sleep(1)
                else:
                    print("【案例分配_案例列表】页面加载完成！")
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
                        print("【案例分配_案例列表】页面加载中...")
                    time.sleep(1)
                else:
                    print("【案例分配_案例列表】页面加载完成！")
                    time.sleep(1)
                    break
            #循环勾选案例，并在勾选完成后点击确认,弹出窗口后点击"确定"
            print("勾选案例...")
            for i in range(0,case_num):
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
            print("等待【执行管理_案例目录】页面加载...")
            for i in range(0,10):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    time.sleep(2)
                else:
                    print("【执行管理_案例目录】页面加载完成！")
                    break
            print("刷新【执行管理_案例目录】页面！")
            #刷新一下案例执行目录页面
            driver.find_element_by_link_text("刷新").click()
                    #等待页面跳转后，页面的加载
            print("等待【执行管理_案例目录】页面加载...")
            for i in range(0,10):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    time.sleep(0.5)
                else:
                    print("【执行管理_案例目录】页面加载完成！")
                    break
            #点击进入目录树,并获取分配案例的数量
            driver.find_element_by_xpath("//span[text()='"+demand+"']").click()
            time.sleep(0.5)
            text=driver.find_element_by_xpath("//span[contains(text(),'"+demand+"')]/../../../following-sibling::tr[1]\
                 //span[text()='"+executor+"']/../../following-sibling::td[1]/div").get_attribute("textContent")
            if text!="":
                print("案例分配成功，分配数量："+text)
            #刷新一下案例执行目录页面
            driver.find_element_by_link_text("刷新").click()
            #等待页面跳转后，页面的加载
            print("等待【执行管理_案例目录】页面加载...")
            for i in range(0,10):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    time.sleep(0.5)
                else:
                    print("【执行管理_案例目录】页面加载完成！")
                    break
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