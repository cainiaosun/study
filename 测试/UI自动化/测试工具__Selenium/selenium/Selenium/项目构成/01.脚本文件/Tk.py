# 弹出一个窗口并根据点击按钮返回一个值，我们只应用于next_step()函数中，共同处理异常后续操作
def pop_up_box(pop_text):
    import tkinter
    from tkinter import ttk
    import os
    values={'username':None,'password':None,'case_path':None,'if_import':None,\
        'if_assign':None,'excutor':None,'begin_num':None,'end_num':None}
    def submit():
        try:
            values['username']=Combobox1.get()
            values['password']=Entry1.get()
            values['case_path']=Entry2.get()
            values['if_import']=v1.get()
            values['if_assign']=v2.get()
            values['excutor']=Combobox2.get()
            values['begin_num']=Combobox3.get()
            values['end_num']=Combobox4.get()
            root.destroy()
        except:print("error!")

    def cancel():
        root.destroy()

    def select_path():
        from tkinter import filedialog
        path_=filedialog.askopenfilename(initialdir=os.getcwd())
        #tkinter.path_.set(path_)
        case_path.set(path_)
        print(case_path.get())

    def on_closing():
        from tkinter import messagebox
        if messagebox.askokcancel("Quit","Do you want to quit?"):
            root.destroy()
            
    root = tkinter.Tk()#窗口
    root.title("案例上传及分配")#窗口标题
    root.geometry("430x270")#设置窗口大小

    #把一个Label当做一个空间容纳用户名和密码
    sapce1=tkinter.Label(root)
    sapce1.pack(side='top')
    l1 = tkinter.Label(sapce1,justify="left",text="用户名：",width=6,height=2)
    l1.pack(side='left',expand=0)

    username = tkinter.StringVar(sapce1,value="sunhongbin")
    Combobox1 = ttk.Combobox(sapce1,width=16,textvariable=username)
    Combobox1["values"]=("sunhongbin","wangzhaoxia","yuanxiaoyun")
    Combobox1.pack(side="left")


    l2 = tkinter.Label(sapce1,justify="left",text="密  码：",width=6,height=2)
    l2.pack(side='left')

    password = tkinter.StringVar(sapce1,value="123456")
    Entry1 = tkinter.Entry(sapce1, textvariable=password,width=15)
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
    excutor = tkinter.StringVar(sapce4,value="孙洪斌")
    Combobox2 = ttk.Combobox(sapce4,width=16,textvariable=excutor)
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
#print(pop_up_box("你妹"))
#警告窗口，遇见错误时提示错误信息
def warning(message="提示信息",name="错误提示！"):
    import tkinter
    #提交事件，点击提交按钮时调用，为参数赋值并关闭窗口，异常时终止运行
    def confirm():
        root.destroy()
        quit()
    def on_closing():
        from tkinter import messagebox
        if messagebox.askokcancel("Quit","Do you want to quit?"):
            root.destroy()
    root = tkinter.Tk()#窗口
    root.title(name)#窗口标题
    root.geometry("360x200")#设置窗口大小
    sapce1=tkinter.Label(root)
    sapce1.pack(side='top')
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

warning()
