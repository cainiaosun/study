import os
import time
souce=['F:\\souce','F:\\souce1']
target_dir='F:\\backup\\'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command='E:&&cd InstallSoftWare\\WinRAR&&rar a %s  %s'%(target,' '.join(souce))
print zip_command
if os.system(zip_command)==0:
    print 'Sucessful backup to',target
else:
    print 'Backup Failed'
time.sleep(10)
