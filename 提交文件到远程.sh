echo 提交文件
rm -f .git/index.lock
ping -n 5 127.1>H:/可删除临时文件
git add *
git commit -m *
git push -u origin master
echo 文件提交完成
ping -n 30 127.1>H:/可删除临时文件