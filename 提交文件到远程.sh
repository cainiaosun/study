echo 提交文件
%删除锁%
rm -f .git/index.lock
%等待5s%
ping -n 5 127.1>H:/可删除临时文件
%更新本地库文件%
git pull 
%添加所有的文件%
git add -A
%提交所有的文件% 
git commit -m -a 
%提交文件到远程%
git push -u origin master 
echo 文件提交完成
ping -n 30 127.1>H:/可删除临时文件