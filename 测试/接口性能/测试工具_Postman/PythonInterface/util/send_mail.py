import smtplib
import email
from email.mime.text import MIMEText


class SendEmail(object):
	# """docstring for SendEmail"""
	# def __init__(self, arg):
	# 	super(SendEmail, self).__init__()
	# 	self.arg = arg

	def send_email(self,user_list,title,content):
		email_host="smtp.163.com"
		send_user="18771723322@163.com"
		password="shb5146955102"
		user="孙洪斌<"+send_user+">"
		message=MIMEText(content,_subtype="plain",_charset="utf-8")
		message["Subject"]=sub
		message["From"]=send_user
		message["To"]=";".join(user_list)
		server=smtplib.SMTP()
		server.connect(email_host)
		server.login(send_user,password)
		server.sendmail(user,user_list,message.as_string())
		server.close()


if __name__=="__main__": 
	user_list=["1396677105@qq.com"]
	sub="测试邮件标题"
	content="测试邮件内容"
	print(SendEmail().send_email(user_list,sub,content))
