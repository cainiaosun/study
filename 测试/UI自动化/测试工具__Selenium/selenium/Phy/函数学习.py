#coding=UTF-8

def func(name1,name2,age=18,*str,**dict):
    if 'job' in dict:
        pass
    print(name1,name2,age,str,dict)

func("sunhongbin","lihua","str1","str2",job="testing")


#定义函数用“def”关键字，如下func1
#形式参数：函数的传入变量，如number
def func1(number):
    print u"定义的函数名称是",func1.__name__,"形式参数number的值是：",number
func1(100)

#默认形式参数值：
#默认参数值可以被缺省,也可以传值
#定义函数时不能只在参数中间，定义默认参数，/例如：def func2(number1,number2="100",number3):
#调用函数的时候如果一个参数指定了名称，那么其它参数也要指定，错误示例：func2(number1=10,20,30),
#只指定了number1的值；但是对于最后一个参数是可以的，如“func2(10,20,number3=30)
def func2(number1,number2="100",number3="200"):
    print "number1的值是：",number1,"默认参数number2的值是：",number2,"默认参数number3的值是：",number3
func2(number1=10,number3=20)

#可变参数的实现，可以用元组或者列表做为参数
def func3(number):
    sum=0
    for i in number:
        sum=sum+i
    print "计算元组（列表）number内的各个值得和是：",sum
func3([1,2,3,4])

#可变参数的实现：*标识符，例如def func4(*var):
#当默认参数遇见可变参数时：默认参数只能在可变参数为空的情况下才能缺省func4(var1=200)，错误示例：func4(var1=100,100,899)
def func4(var1,var2=50,*var3):
    print "参数var1的值是：",var1,"默认参数var2的值是",var2,"可变参数var3的值是：",var3
func4(100,200,300,400)

#可变参数的实现：定义可变字典参数如：**dict，两个*号，调用需要指明键值
#
def func5(var,**dict):
    print "参数var的值是：",var,"字典的值是：",dict
func5("canshu",job="testing",name="sunhongbin")

'''
指定字典变量的变量名（字典只能输入这两个字段）：*，
但是目前在pyhon2我测试的是不能用的,后面再pyhon3中检查是否可用
'''
"""
def calc1(name,*,number1,number2):
    print(name,number)

calc1("sunhongbin",number1="1",number2="2")
"""

#如果是对全局变量进行操作，全局变量不能作为形式参数,如下x不能作为形式参数，调用的时候也不用输入全局变量
def func6():
    global x
    print "x=",x
    x=10
    print "local change x=",x
x=100
func6()


#函数递归
#以下是实现的一个阶乘的递归函数
def func7(n):
        if n==1:
            return 1
        return n * func7(n-1)
result=func7(100)
print "递归的结果是：",result


#尾递归，不带表达式的递归,知道有这个就可以了，我们不研究，有一个概念叫做栈溢出，也是知道就好

    















