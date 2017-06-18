# shell 脚本学习笔记
---
## 命令
### history
* history 查看终端历史命令
* history 与 ！号关联:
```     
!!     #为调用上一条指令，与 UP 键相似  
!21    #为调用历史命令中的第21条指令
```
### grep
* 基础部分
```
grep 'string' file #查找file中string   
grep -r 'string' #查找出当前目录下包含string的文件
grep -n 'string' file #查找file中string,并显示行号
grep -v 'string' file #file中不包含string的内容
grep -c 'string' file #统计string在file中有多少行出现过  
grep -o 'string' file | wc -l #统计string在file中出现多少次
```
* 进阶部分
```
grep '^str' file #查找file中以str开头的行
grep 'str$' file #查找file中以str结尾的行
grep -n '^$' file ＃查找file中空行的行号  
grep -A2 '^$' file #查找file中空行的行，以及该空行的下面２行 
grep -B3 '^$' file #查找file中空行的行，以及该空行的上面３行
```
