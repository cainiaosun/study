#coding=utf-8
"""
	执行dos命令
	Include List：
		DosCmd:dos命令类，包含两个方法：xcute_cmd_result()、excute_cmd()
"""

import os
class DosCmd:
	"""
	Method List:
		excute_cmd_result():执行命令，并返回dos返回结果
		excute_cmd():执行命令，不返回dos返回结果
	"""

	def excute_cmd_result(self,command):
		"""
		excute_cmd_result()执行命令，并返回dos返回结果
		参数：
			command：需要执行的命令
		Etc：
			DosCmd().excute_cmd_result('adb devices')
		"""
		result_list = []
		result = os.popen(command).readlines()
		for i in result:
			if i =='\n':
				continue
			result_list.append(i.strip('\n'))
		return result_list

	def excute_cmd(self,command):
		"""
		excute_cmd()执行命令，不返回dos返回结果
		参数：
			command：需要执行的命令
		Etc：
			DosCmd().excute_cmd('adb devices')
		"""
		os.system(command)

if __name__ == '__main__':
	dos = DosCmd()
	print(dos.excute_cmd_result('adb devices'))