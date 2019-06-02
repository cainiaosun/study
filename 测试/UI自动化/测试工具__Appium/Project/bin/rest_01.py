# with open("../test_write.txt","a") as fp:
# 	print(fp.readlines())
# 	fp.write("12312312312")
# 	fp.closed


fp=open("../lll3.txt",'r')   
#print(fp.readlines())
print(fp.readlines())
#fp.save
#print(fp.readlines())

with open("./text_write.py","w") as fp:
	fp.write("""
import do
class son(do.parent):
	def add(self,a,b,c):
		return a+b+c
		""")
	fp.close()

import text_write
print(text_write.son().sum(1,2))
print(text_write.son().add(1,2,3))
