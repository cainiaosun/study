import unittest,sys
sys.path.append(".//")
sys.path.append(sys.path[0].split("项目构成")[0] + '项目构成\\02.方法模块')
from HTMLTestRunner import *

class classtest(unittest.TestCase):
    def setUp(self):#将全局变量dr赋值到setUp方法中，
        pass

    def test_01(self):
        self.assertEqual(1,1,msg="值不相等")

    def test_01(self):
        self.assertEqual(1,1,msg="值不相等")

    def tearDown(self):
        pass

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()#获取套件
    suite.addTest(classtest('test_01'))#添加案例
    runner=unittest.TextTestRunner()#


    filename = "..\\03.测试报告\\result.html"
    with open(filename, 'wb') as fp:        
        # 定义测试报告        
        runner = HTMLTestRunner(stream=fp, title='CSDN login 测试报告', description='用例执行情况：')        
        # 运行测试用例        
        runner.run(suite)#执行套件       
        # 关闭测试报告        
        # fp.close()