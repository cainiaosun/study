import sys,json
sys.path.append("..")
from base.method import RunMethod
from base.datatable import DataTable
from base.environment import Environment
from base.operate_data import GetData,ModifyData
from util.send_mail import SendEmail
from util.write_log import Log
from jsonpath_rw import jsonpath,parse


class RunMain:
	def __init__(self):
		pass

	def run_test(self,testcase):
		request_data=GetData().get_request_data(testcase)#获取案例及依赖案例的所有请求数据
		for i in range(0, len(request_data)):#从最底层依赖处理请求数据，直到执行当前案例，即最后一个循环时
			data = request_data[i]
			response_data = RunMethod().request(method=data["method"], url=data["url"], data=data["data"], headers=None)
			if i == len(request_data) - 1:
				ModifyData().write_result(testcase,response_data)
				Log().info("案例执行完成 > 案例编号"+data["Case_ID"])
				return response_data
			else:
				data_next = request_data[i + 1]
				depend_para = data_next["depend_para"]
				para_value=GetData().json_field(data_next["depend_data"],response_data)
				if para_value:
					para_value = para_value[0]
					data_next["data"][depend_para] = para_value
				else:
					para_value = None
					Log().warning(data_next["Case_ID"]+"所依赖的字段"+data_next["depend_data"]+"在依赖案例"+
								  data_next["depend_case"]+"的返回值中不存在！")


	def main(self):
		Log().info("执行案例集 > 案例集")
		DataTable.load("../case/testcase.xls")
		count=DataTable().rows()-1#案例总数
		pass_num=0
		fail_num=0
		skip_num=0
		for i in range(1,DataTable().rows()):
			Environment("row").set(i)
			value=Environment("row").value
			Log().info("案例依次执行序号："+str(value)+" > 案例编号："+DataTable("Case_ID").value())
			if DataTable("是否执行").value()=="是":
				self.run_test(i)
				if DataTable("是否执行").value()=="通过":
					pass_num=pass_num+1
				elif DataTable("是否执行").value()=="失败":
					fail_num=fail_num+1
			else:
				skip_num=skip_num+1
				Log().info("案例已跳过 > 案例编号" + DataTable("Case_ID").value())
				DataTable("执行状态").set("跳过")
		Log().info("案例执行完成 > 执行总数为" + str(count))
		user_list = ["1396677105@qq.com"]
		title = "接口测试报告"
		content = "案例总数："+str(count)+"；通过数："+str(pass_num)+"；失败数："+str(fail_num)+"；跳过数："+str(skip_num)+"。"
		SendEmail().send_email(user_list, title, content)



if __name__=="__main__":
	RunMain().main()











