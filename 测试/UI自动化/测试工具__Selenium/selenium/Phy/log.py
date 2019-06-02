#coding=UTF-8
#可变参数的实现：*标识符，例如def func4(*var):
def func4(i,*var3):
    print "参数var1的值是：",i,"默认参数var2的值是",var3
func4(200,20,40,30)
