import HTMLTestRunner
print("123")
with open(filename, 'wb') as fp:        
	# 定义测试报告        
	runner = HTMLTestRunner(stream=fp, title='CSDN login 测试报告', description='用例执行情况：')        
	# 运行测试用例        
	runner.run(testunit)        
	# 关闭测试报告        
	# fp.close()
--------------------- 
作者：关进小黑屋 
来源：CSDN 
原文：https://blog.csdn.net/yihongyuantufei/article/details/81289492 
版权声明：本文为博主原创文章，转载请附上博文链接！