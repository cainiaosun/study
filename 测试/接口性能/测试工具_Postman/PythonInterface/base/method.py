import requests
import json
from mock import mock



class RunMethod:
	def __init__(self):
		pass
	def get(self,url,data=None,headers=None):
		res = requests.get(url=url,params=data,headers=headers,verity=False)
		try:
			res = res.json()
			res=json.dumps(res,indent=2,sort_keys=True)
		except:
			res=res.text
		return res


	def post(self,url,data=None,headers=None):
		res = requests.post(url=url,params=data,headers=headers,verity=False)
		try:
			res = res.json()
			res=json.dumps(res,indent=2,sort_keys=True)
		except:
			res=res.text
		return res

	def put(self,url,data=None,headers=None):
		res = requests.put(url=url,params=data,headers=headers,verity=False)
		try:
			res = res.json()
			res=json.dumps(res,indent=2,sort_keys=True)
		except:
			res=res.text
		return res

	def delete(self,url,data=None,headers=None):
		res = requests.delete(url=url,params=data,headers=headers,verity=False)
		try:
			res = res.json()
			res=json.dumps(res,indent=2,sort_keys=True)
		except:
			res=res.text
		return res


	def request(self,method,url,params=None,headers=None):
		#print(method,url,params)
		if method=="post":
			res=self.post(url,params,headers)
		elif method=="get":
			res=self.get(url,params,headers)
		else:
			res=None
		return res

if __name__ == '__main__':
	url="http://127.0.0.1:8000/login/"
	data={
		"username":"sunhongbin",
		"password":"shb427190"
	}
	print(RunMethod().get(url,data))
	print(RunMethod().post(url,data))
	print(RunMethod().request("get",url,data))

	# get=mock.Mock(return_value=json.dumps(data,indent=2,sort_keys=True))

	# print(get(url,data))


