from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time , datetime , re,os,openpyxl,sys
#警告窗口，遇见错误时提示错误信息
def warning(message="提示信息",name="错误提示！",errorname="错误信息："):
    import tkinter,sys
    #提交事件，点击提交按钮时调用，为参数赋值并关闭窗口，异常时终止运行
    def confirm():
        root.destroy() 
        sys.exit()
    def on_closing():
        from tkinter import messagebox
        if messagebox.askokcancel("Quit","Do you want to quit?"):
            root.destroy()
            sys.exit()
    root = tkinter.Tk()#窗口
    root.title(name)#窗口标题
    root.geometry("360x200")#设置窗口大小
    sapce1=tkinter.Label(root)
    sapce1.pack(side='top')
    message=errorname+"\n    "+message+"\n任意操作后终止执行！"
    l2 = tkinter.Label(sapce1,justify="left",text=message,width=50,height=8)
    l2.pack(side="bottom")
    sapce2=tkinter.Label(root)
    sapce2.pack(side='top')
    tkinter.Label(sapce2,width=32).pack(side="left")
    tkinter.Button(sapce2, text="取消", command=confirm,width=5).pack(side="left")
    tkinter.Label(sapce2,width=1).pack(side="left")
    tkinter.Button(sapce2, text="确定", command=confirm,width=5).pack(side="left")
    root.protocol("WM_DELETE_WINDOW",on_closing)
    root.mainloop()
# 弹出一个窗口并录入一些参数控制流程
def pop_up_box():
    import tkinter
    from tkinter import ttk
    from tkinter import filedialog
    import os,sys
    #建一个参数字典，所有字段默认值均设为空
    values={'username':None,'password':None,'case_path':None,'if_import':None,\
        'if_assign':None,'executor':None,'begin_num':None,'end_num':None}
    #提交事件，点击提交按钮时调用，为参数赋值并关闭窗口，异常时终止运行
    def submit():
        try:
            values['username']=Combobox1.get()
            values['password']=Entry1.get()
            values['case_path']=Entry2.get()
            values['if_import']=v1.get()
            values['if_assign']=v2.get()
            values['executor']=Combobox2.get()
            values['begin_num']=Combobox3.get()
            values['end_num']=Combobox4.get()
            values['display']=v3.get()
            root.destroy()
        except:#出现异常停止运行，暂时没有写一个好的提示
            print("error!")
            sys.exit()

    #取消事件，直接关闭窗口并终止执行
    def cancel():
        root.destroy()
        sys.exit()

    #选择文件，并赋值给绑定了case_path的组件
    def select_path():
        path_=filedialog.askopenfilename(initialdir=os.getcwd())
        case_path.set(path_)
        #print(case_path.get())

    #直接点击关闭窗口时的处理函数
    def on_closing():
        from tkinter import messagebox
        if messagebox.askokcancel("Quit","Do you want to quit?"):
            root.destroy() 
            sys.exit()

    root = tkinter.Tk()#窗口
    root.title("案例上传及分配")#窗口标题
    root.geometry("450x301")#设置窗口大小

    #把一个Label当做一个空间容纳用户名和密码
    sapce1=tkinter.Label(root)
    sapce1.pack(side='top')
    l1 = tkinter.Label(sapce1,justify="left",text="用户名：",width=6,height=2)
    l1.pack(side='left',expand=0)

    username = tkinter.StringVar(sapce1,value="sunhongbin")
    Combobox1 = ttk.Combobox(sapce1,width=14,textvariable=username)
    Combobox1["values"]=("sunhongbin","wangzhaoxia","yuanxiaoyun")
    Combobox1.pack(side="left")

    #空组件，占用4个长度单位形成空白区间
    tkinter.Label(sapce1,width=4,height=2).pack(side="left")
    #密码label
    tkinter.Label(sapce1,justify="left",text="密  码：",width=6,height=2).pack(side='left')

    password = tkinter.StringVar(sapce1,value="123456")
    Entry1 = tkinter.Entry(sapce1, textvariable=password,width=13)
    Entry1.pack(side='left')

    sapce2=tkinter.Label(root)
    sapce2.pack(side='top')

    l3 = tkinter.Label(sapce2,justify="left",text="案例路径：",width=8,height=2)
    l3.pack(side='left')
    case_path = tkinter.StringVar(sapce1,value="请录入或选择案例路径！")
    Entry2 = tkinter.Entry(sapce2, text="sunhongbin",textvariable=case_path,width=31)
    Entry2.pack(side='left')
    btn0 = tkinter.Button(sapce2, text="选择路径",command=select_path,width=7,height=1)
    btn0.pack(side='left')
 
    sapce3=tkinter.Label(root)
    sapce3.pack(side='top')
    l4 = tkinter.Label(sapce3,justify="left",text="是否上传：",width=8,height=2)
    l4.pack(side='left')
    v1=tkinter.IntVar()
    v1.set(0)
    for i in range(2):
        if i==0:text="是"
        elif i==1:text="否"
        Radiobutton = tkinter.Radiobutton(sapce3,text=text,value=i,variable=v1,width=2)
        Radiobutton.pack(side='left')
    #占格位，保证对齐
    l5 = tkinter.Label(sapce3,width=27)
    l5.pack(side='left')

    sapce4=tkinter.Label(root)
    sapce4.pack(side='top')
    l6 = tkinter.Label(sapce4,justify="left",text="是否分配：",height=2)
    l6.pack(side='left')
    v2=tkinter.IntVar()
    v2.set(0)
    for i in range(2):
        if i==0:text="是"
        elif i==1:text="否"
        Radiobutton = tkinter.Radiobutton(sapce4,text=text,value=i,variable=v2,width=2)
        Radiobutton.pack(side='left')
    l7 = tkinter.Label(sapce4,justify="left",text="执行人：")
    l7.pack(side='left')
    executor = tkinter.StringVar(sapce4,value="孙洪斌")
    Combobox2 = ttk.Combobox(sapce4,width=16,textvariable=executor)
    Combobox2["values"]=("孙洪斌","王朝霞","袁小云")
    Combobox2.pack(side="left")
    l5 = tkinter.Label(sapce4,width=0)
    l5.pack(side='right')

    sapce5=tkinter.Label(root)
    sapce5.pack(side='top')
    l7 = tkinter.Label(sapce5,justify="left",text="分配起止轮次：",height=2)
    l7.pack(side='left')
    begin = tkinter.StringVar(sapce4,value="1")
    Combobox3 = ttk.Combobox(sapce5,width=4,height=2,textvariable=begin)
    Combobox3["values"]=("1","2","3")
    Combobox3.pack(side='left')
    l8 = tkinter.Label(sapce5,justify="left",text="至")
    l8.pack(side='left')
    end = tkinter.StringVar(sapce4,value="3")
    Combobox4 = ttk.Combobox(sapce5,width=4,textvariable=end)
    Combobox4["values"]=("1","2","3")
    Combobox4.pack(side='left')
    l8 = tkinter.Label(sapce5,justify="left",text="轮")
    l8.pack(side='left')
    l9 = tkinter.Label(sapce5,width=16)
    l9.pack(side='left')

    sapce6=tkinter.Label(root)
    sapce6.pack(side='top')
    tkinter.Label(sapce6,justify="left",text="显示浏览器：",height=2).pack(side='left')
    v3=tkinter.IntVar()
    v3.set(1)
    for i in range(2):
        if i==0:text="是"
        elif i==1:text="否"
        Radiobutton = tkinter.Radiobutton(sapce6,text=text,value=i,variable=v3,width=2)
        Radiobutton.pack(side='left')
    tkinter.Label(sapce6,width=25).pack(side='left')

    var = tkinter.StringVar()
    var.set("")
    btn1 = tkinter.Button(root, text="取消", command=cancel,width=5)
    btn2 = tkinter.Button(root, text="提交", command=submit,width=5)
    l9 = tkinter.Label(root,width=4)
    l10 = tkinter.Label(root,width=2)
    l9.pack(side='right')
    btn2.pack(side='right')
    l10.pack(side='right')
    btn1.pack(side='right')
    root.protocol("WM_DELETE_WINDOW",on_closing)
    root.mainloop()
    return values
#取得参数集values
values=pop_up_box()
print(values)

class ATQtest(unittest.TestCase):
    #driver全局变量
    if values['display']==0:
        dr = webdriver.Firefox()
    elif values['display']==1:
        option =webdriver.FirefoxOptions()
        option.set_headless()
        dr = webdriver.Firefox(firefox_options=option)#设置对象
    #导入案例的路径
    case_path=values['case_path']
    #案例文档去掉后缀的名称
    if case_path.find("/"):
        filename=case_path.split("/")[len(case_path.split("/"))-1].split(".")[0].split("_")[0]
    else:
        filename=case_path.split("\\")[len(case_path.split("\\"))-1].split(".")[0].split("_")[0]
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
    def setUp(self,driver = dr,demand = demand,rows = rows):
        self.driver =driver#设置对象
        self.base_url = "http://11.8.127.248:8080/atq/frame.jsp"#网址
        self.demand=demand#需求名称，构成是：日期+需求名
        self.rows=rows#导入案例的案例数
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True
        print("")

    def test_01_login(self):
        driver = self.driver
        self.driver.get(self.base_url)
        print("登录ATQ！")
        driver.find_element_by_name('loginId').clear()
        driver.find_element_by_name('loginId').send_keys(values['username'])
        driver.find_element_by_name('password').send_keys(values['password'])
        driver.find_element_by_link_text('登录').click()
        #等待
        time.sleep(5)

    def test_02_case_import(self):
        print("进入案例管理页面！")
        driver = self.driver
        aa=driver.find_element_by_xpath("//a/span")
        aa.find_element_by_xpath("//span[contains(text(),'案例管理')]").click()
        time.sleep(2)
        print("导入案例！")
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
        case_path=values['case_path']
        case_path=case_path.replace("/","\\\\")
        upload.send_keys(case_path)
        value=upload.get_attribute('value')
        if value!="":
            print("文件上传成功！")
        driver.find_element_by_xpath("//span[text()='确定']").click()
        time.sleep(2)
        #判断页面的元素检查是否正在导入，默认先等30s
        if len(driver.find_elements_by_xpath("//div[contains(text(),'导入中，请稍候')]"))>0:
            print("导入中，请耐心等候...")
            time.sleep(10)
        #30s后通过判断导入结束的弹出窗口判断是否导入完毕，如果没有找到窗口则等待继续寻找窗口，直至寻找成功
        #回到主frame页
        driver.switch_to.default_content()
        for i in range(0,300):
            try:
                text=""
                text=driver.find_element_by_xpath("/html/body/div[10]/div[2]").text
            except:
                if i==299:
                    values["if_assign"]==1
                    warning("导入出错，请检查文件格式及环境！")
            if text=="操作成功!":
                print("导入案例完成！")
                break
            elif text=="":time.sleep(0.01)    
            else:
                global if_assign
                if_assign==1
                warning("导入出错，请检查文件格式及环境！")       
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
        ex=openpyxl.load_workbook(values['case_path'])
        sh=ex[ex.sheetnames[0]]
        print("案例目录检查...")
        if self.isElementExist("by.xpath","//span[text()='"+sh['C2'].value+"']/../../../following-sibling::tr[1]//span[text()='"+sh['D2'].value+"']"):
            print("案例目录检查完毕，案例目录存在，案例导入成功！")
        else:print("案例目录检查完毕，未发现案例目录，案例导入失败！")
        #回到主frame页
        driver.switch_to.default_content()
        time.sleep(5)


    def test_03_case_assign(self):
        #if values["if_assign"]==1:
            #sys.exit()
        print("创建目录并分配案例！")
        driver = self.driver
        print("")
        de=self.demand
        executor=values['executor']
        number=self.rows
        for iLoop in range(int(values['begin_num'])-1,int(values['end_num'])):
            if iLoop==0:
                demand=de+"（第一轮）"
                case_num=number
            elif iLoop==1:
                demand=de+"（第二轮）"
                case_num=int(number*0.65)+1
            elif iLoop==2:
                demand=de+"（回归测试）"
                case_num=int(number*0.45)+1
            else:
                break
            #重新访问一下地址，如果重新进页面有一些元素的属性有变化不便于定位操作，重进一次页面可以避免这种问题
            driver.get(self.base_url)
            print("进入执行管理页面！")
            driver.find_element_by_xpath("//span[contains(text(),'执行管理')]").click()
            #切换iframe页面
            xf=driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
            driver.switch_to.frame(xf)
            time.sleep(2)
            print("等待【执行管理_案例目录】页面加载...")
            for i in range(0,10):
                refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                if len(refresh)>0:
                    time.sleep(2)
                else:
                    print("【执行管理_案例目录】页面加载完成！")
                    break
            if len(driver.find_elements_by_xpath("//span[text()='"+demand+"']"))==0:
                #增加轮次轮次
                driver.find_element_by_xpath("//span[text()='增加轮次']").click()
                #输入轮次名称，并点击保存
                driver.find_element_by_id("turnName").send_keys(demand)
                driver.find_element_by_xpath("//span[text()='保存']").click()
                time.sleep(0.2)
                #等待Loading元素消失，判断保存是否完成
                for i in range(0,20):
                    refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
                    if len(refresh)>0:
                        if i==0:
                            print("新增轮次保存中...")
                        time.sleep(1)
                    else:
                        print("保存完成！")
                        time.sleep(3)
                        break
            time.sleep(1)
            item = driver.find_element_by_xpath("//span[text()='"+demand+"']")
            print("案例执行目录："+item.text)
            #如果待分配案例数>200，每次分配200条，剩余不足200条的一次分配，然后退出循环，10次循环最大支持2000条
            case_sum=0
            page_num=0
            for jLoop in range(0,10):
                if case_num>200:
                    page_num=page_num+1
                    t_case_num=200
                    case_num=case_num-200
                    case_sum=case_sum+t_case_num
                elif case_num>0:
                    page_num=page_num+1
                    t_case_num=case_num
                    case_num=0
                    case_sum=case_sum+t_case_num
                elif case_num==0:
                    break
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
                    /../../../following-sibling::tr[1]//span[text()='"+values['executor']+"']")
                #移动滚动条到元素显示范围
                driver.execute_script("arguments[0].scrollIntoView();",exme)
                ActionChains(driver).move_to_element(exme).context_click().perform()
                driver.find_element_by_xpath("//div[contains(text(),'分配案例')]").click()
                #demand临时数据使用完毕，恢复原值
                if tempdemand!="":
                    demand=tempdemand
                    tempdemand=""
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
                time.sleep(45)
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
                time.sleep(60)
                print("勾选案例...")
                for i in range(0,t_case_num):
                    driver.find_element_by_xpath("//tr[@id='datagrid-row-r"+str(page_num)+"-2-"+str(i)+"']/td/div/input").click()
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
                item = driver.find_element_by_xpath("//span[text()='"+demand+"']")
                if len(item.text)>28:
                    #临时修改demand
                    tempdemand=demand
                    demand="独特性命名（处理名称过长，点击被遮挡）"
                    driver.execute_script("arguments[0].innerText='"+demand+"';",item)
                    driver.find_element_by_xpath("//span[text()='"+demand+"']").click()
                else:
                    item.click()
                time.sleep(0.5)
                text=driver.find_element_by_xpath("//span[contains(text(),'"+demand+"')]/../../../following-sibling::tr[1]\
                     //span[text()='"+executor+"']/../../following-sibling::td[1]/div").get_attribute("textContent")
                if tempdemand!="":
                    demand=tempdemand
                    tempdemand=""
                if text=="":
                    print("案例分配失败！")
                elif int(text)==case_sum:
                    print("案例分配成功，已分配案例数："+text)
                else:
                    print("案例分配失败！")
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
    suite = unittest.TestSuite()
    suite.addTest(ATQtest('test_01_login'))
    if values['if_import']==0:
        suite.addTest(ATQtest('test_02_case_import'))
    if values['if_assign']==0:
        suite.addTest(ATQtest('test_03_case_assign'))
    runner=unittest.TextTestRunner()
    runner.run(suite)