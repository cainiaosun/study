import requests
import json
from mock import mock



class RunMethod:
	def __init__(self):
		pass
	def get(self,url,data=None,headers=None):
		res = requests.get(url=url,data=data,headers=headers)
		response_code=res.status_code
		try:
			res = res.json()
			res["response_code"]=response_code
		except:
			res={}
			res["response_code"] = response_code
		res = json.dumps(res, indent=2, sort_keys=True)
		return res


	def post(self,url,data=None,headers=None):
		res = requests.post(url=url,data=data,headers=headers)
		response_code = res.status_code
		try:
			res = res.json()
			res["response_code"]=response_code
		except:
			res={"response_code":response_code}
		res = json.dumps(res, indent=2, sort_keys=True)
		return res

	def put(self,url,data=None,headers=None):
		res = requests.put(url=url,data=data,headers=headers,verity=False)
		response_code = res.status_code
		try:
			res = res.json()
			res["response_code"] = response_code
		except:
			res = {"response_code": response_code}
		res = json.dumps(res, indent=2, sort_keys=True)
		return res

	def delete(self,url,data=None,headers=None):
		res = requests.delete(url=url,data=data,headers=headers,verity=False)
		response_code = res.status_code
		try:
			res = res.json()
			res["response_code"] = response_code
		except:
			res = {"response_code": response_code}
		res = json.dumps(res, indent=2, sort_keys=True)
		return res


	def request(self,method,url,data=None,headers=None):
		# print(method,url,data)
		if method=="post":
			#print("000")
			res=self.post(url,data,headers)
		elif method=="get":
			res=self.get(url,data,headers)
		else:
			res=None
		return res


if __name__ == '__main__':
	url="http://127.0.0.1:8000/login/"
	data={
		"username":"sunhongbin",
		"password":"shb427190"
	}
	headers={
		#"Content-Type":"application/x-www-form-urlencoded"
		}
	print(RunMethod().get(url,data))
	print(RunMethod().post(url,data,headers))
	print(RunMethod().request("post",url,data))
	print(requests.post(url,headers=headers,data=data).json())

	get=mock.Mock(return_value=json.dumps(data,indent=2,sort_keys=True))
	mock.Mock()

	print("mock",get(url,data))


