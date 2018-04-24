# Day18.4.24
git常用命令以及遇到的问题和解决办法
=======
Hi Meimei!

I am tringing to make a summary about the common comand of git.Also a chance for me to practice the command.
In thr furture i will use git to keep everything i learn here.Hope will have a good time to use it! 
>>>>>>>
1.克隆代码
git clone ip

ctrl+insert 复制
shift_insert 粘贴


2.创建分支
git checkout -b meimei

3.查看状态
git status

4.切换分支
git checkout meimie

5.通过vim进入命令界面进行编辑（i,插入;wq!保存并退出）
vim README.md

6.添加修改数据到缓存区
git add .               （全部文件）
git add 修改的文件名  （具体某一个文件）

7.提交修改到本地分支
git commit -m '注释'

8.查看状态
git status

9提交本地分支到远程分支
git push origin 分支名

PS:设置全局变量
git config --global user.email "sss@qq.com"
git config --global user.name 'gg'



其它
1.合并add和commit操作
git commit -am '****'

2.创建秘钥
ssh-keygen -t rsa -C 账号

3.比较分支之间的不同
git diff 分支1 分支2

4.合并
git merge 分支

5.打tag标签
git tag -a 版本号 -m 注释

6.推送版本
git push origin 版本号

7.删除远程分支
git push origin --delete 分支

8.查看版本号
 git tag 

9.删除版本号
 git tag -d 版本号


10.删除远程版本号
 push origin --delete tag 版本号

11.缓存修改的代码
 git stash

遇到的问题和解决办法：
1.运行 $ git remote add origin git@github.com:yourName/yourRepo.git命令时提示下面的错误。
fatal: Not a git repository (or any of the parent directories): .git

提示说没有.git这样一个目录，解决办法如下：运行git init就可以了！

2.Git使用之(pathspec master did not match any file(s) known to git)
解决办法：进入到仓库而不是上一级目录

3.执行git push origin 分支名，提示 Pulling is not possible because you have unmerged files.
解决办法：重新执行git add .命令和git commit -m '注释',然后再执行git push origin 分支名
