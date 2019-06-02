class hanoi(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
s=1
def hanoi(n, x, y, z):
	global s
	#print(s)
	if n == 1:
		print(s,x, '-->' , z) # 把唯一的一个盘从x移动到z就完事了
		s=s+1
	else:
		hanoi(n-1, x, z, y) # 把除最下以外的所有盘当作一个整体，移动到y
		print(s,x, '-->' , z) # 把最底下的那个盘移动到z
		s=s+1
		hanoi(n-1, y, x, z) # 再把放在y上的所有盘放到已经放了最下面一个盘的z上


n =5#int(input('汉诺塔层数是：'))
hanoi(n, 'X', 'Y', 'Z')
