echo 提交文件
rm -f .git/index.lock #删除锁
ping -n 5 127.1>H:/可删除临时文件 #等待5s
git pull #更新本地库文件
git add -A #添加所有的文件
git commit -m -a #提交所有的文件%
git push -u origin master #提交文件到远程
echo 文件提交完成
ping -n 30 127.1>H:/可删除临时文件