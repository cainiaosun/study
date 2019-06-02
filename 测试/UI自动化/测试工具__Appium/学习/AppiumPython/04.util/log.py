
#python日志
# coding=utf-8
import logging
import time
import socket
import os
import traceback
import multiprocessing
# import setting
 
#rq = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
rq = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

setting = {
	'logpath': '../10.log/',
	'filename': 'fox_'+rq+'.log'
}
# localIP = socket.gethostbyname(socket.gethostname())
 
class Log(object):
	def __init__(self,logger="00000"):
		self.path = setting['logpath']
		self.filename = setting['filename']
		self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s')
		# self.logger = logging.getLogger(logging.basicConfig(level=logging.NOTSET))
		self.logger = logging.getLogger(logger)
		self.loggerName = logger
		self.name =socket.gethostbyname(socket.gethostname())#获取主机名称和IP
		###########################################################################
		self.logger = logging.getLogger(self.name)
		#self.logger = logging.getLogger("pid"+str(multiprocessing.current_process().pid))
		self.logger.setLevel(logging.DEBUG)
		# self.logger.setLevel(logging.basicConfig(level=logging.NOTSET))
		# self.fh = logging.FileHandler(self.path + self.filename)
		###########################################################################
		self.fh = logging.FileHandler(self.path + self.filename)
		# self.fh.setLevel(logging.DEBUG)
		self.fh.setFormatter(self.formatter)
		self.logger.addHandler(self.fh)
		self.pid=multiprocessing.current_process().pid
		###############
		# self.fh.setLevel(logging.DEBUG)
		# self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s')
		# self.fh.setFormatter(self.formatter)
		# self.logger.addHandler(self.fh)
 
	def close(self):
		if rq != self.fileHandlerName:
			################
			if self.fileHandler != None:
				self.logger.removeHandler(self.fileHandler)
			  ##################
				# self.logger.addHandler(self.fh)
				# self.logger.addHandler(fh)
				self.logger.removeHandler(fh)
 
##############################################################################################################
 
	def _fmtInfo(self, msg):
		if len(msg) == 0:
			msg = traceback.format_exc()
			return msg
		else:
			_tmp = [msg[0]]
			_tmp.append(traceback.format_exc())
			return '\n**********\n'.join(_tmp)
 
 
###################################################################################3###########################
 
 
 
 
	# def notset(self, msg):
	#	 self.logger.notset(msg)
 
	def debug(self, msg):
		self.msg="pid:"+str(self.pid)+" - "+str(msg)
		self.logger.debug(self.msg)
		self.logger.handlers.clear()
 
	def info(self, msg):
		self.msg="pid:"+str(self.pid)+" - "+str(msg)
		self.logger.info(self.msg)
		self.logger.handlers.clear()
 
	def warning(self, msg):
		self.msg="pid:"+str(self.pid)+" - "+str(msg)
		self.logger.warning(self.msg)
		self.logger.handlers.clear()
 
	def error(self, msg):
		self.msg="pid:"+str(self.pid)+" - "+str(msg)
		self.logger.error(self.msg)
		self.logger.handlers.clear()
 
	def critical(self,msg):
		self.msg="pid:"+str(self.pid)+" - "+str(msg)
		self.logger.critical(self.msg)
		self.logger.handlers.clear()
 
	# def close(self):
	#	 self.logger.addHandler(self.fh)
	#	 self.logger.removeHandler(self.fh)
 
# if __name__ == "__main__":
#	 logger = Log("info")



if __name__=="__main__":
	print("yes!")
	Log().info("信息!")
	Log().warning("警告！")
	Log().debug("调试！")
	Log().critical("致命！")
	# t_0=time.time()
	# for i in range(100):
	# 	writ_log(str(i))

	# print(time.time()-t_0)