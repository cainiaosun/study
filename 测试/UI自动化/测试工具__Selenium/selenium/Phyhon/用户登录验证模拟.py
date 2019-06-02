#coding=utf-8
username=raw_input(u"请输入用户名：")
password=raw_input(u"请输入密码：")
pp=username.encode(utf-8)
qq=password.encode(utf-8)
print u"用户名：%s"%pp
print u"密码:%s"%qq
flag=1
while str(username)<>"孙":
    if flag>2:
        break
    print "用户名输入错误，请重新输入！"
    username=raw_input(u"请输入用户名：")
    password=raw_input(u"请输入密码：")
    flag=flag+1
    print "1"+str(flag)
else:
    while str(password)<>"123456":
        if flag>2:
            break
        print "密码输入错误，请重新输入！"
        username=raw_input(u"请输入用户名：")
        password=raw_input(u"请输入密码：")
        flag=flag+1
        print "2"+str(flag)
    else:
        print u"验证成功！"
        
        
