#coding=utf-8
import yaml
class WriteUserCommand:
	def read_data(self):
		'''
		加载yaml数据
		'''
		with open("../config/userconfig.yaml") as fr:
			data = yaml.load(fr)
		return data

	def get_value(self,key,port):
		'''
		获取value
		'''

		data = self.read_data()
		print(data)
		value = data[key][port]
		return value

	def write_data(self,i,device,bp,port):
		'''
		写入数据
		'''
		data = self.join_data(i,device,bp,port)
		with open("../config/userconfig.yaml","a") as fr:
			yaml.dump(data,fr)


	def join_data(self,i,device,bp,port):
		data = {
		"user_info_"+str(i):{
		"deviceName":device,
		"bp":bp,
		"port":port
		}
		}
		return data

	def join_table(self,path):
		data = {
		"case_path":{
		"path":path,
		}
		}
		return data

	def clear_data(self,yamlfile="../config/userconfig.yaml"):
		with open("../config/userconfig.yaml","w") as fr:
			fr.truncate()
		fr.close()

	def get_file_lines(self):
		data = self.read_data()
		return len(data)

	def write_case_path(self,path):
		'''
		写入数据
		'''
		self.clear_data(path)
		data = self.join_case_path(path)
		with open(path,"a") as fr:
			yaml.dump(data,fr)

	def join_case_path(self,path):
		data = {
		"case_path":{
		"path":path,
		}
		}
		return data


if __name__ == '__main__':
	write_file = WriteUserCommand()
	write_file.clear_data()
	# write_file.write_date(123123)
	# print(write_file.get_file_lines())
	# print(write_file.get_value('user_info_1','bp'))
	write_file.write_case_path(88888)
	write_file.write_case_path(12310000023)

