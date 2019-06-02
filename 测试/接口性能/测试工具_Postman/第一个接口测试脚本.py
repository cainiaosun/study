import urllib.request as urllib2
import urllib.parse as urllib
url = "https://www.baidu.com/s"
data="wd=\%E6\%97\%B6\%E9\%97\%B4&rsv_spt=1&rsv_iqid=0xe4d28ae800033916&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=001"
#data=urllib.urlencode(data)
res=url+"?"+data
resq=urllib2.urlopen(res)
reponse=resq.read()
print(reponse)