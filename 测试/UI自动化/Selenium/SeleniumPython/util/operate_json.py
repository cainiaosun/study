#coding:utf-8
import json
class OperateJson:
	def read_data(self):
		with open(filename,"r",encoding="utf-8") as fp:
			data=json.load(fp)
		return data

	def get_data(self,key):
		return self.read_data()[key]


if __name__=="__main__":
	OperateJson()
