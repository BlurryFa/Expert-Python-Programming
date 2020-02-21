# 一、Python's venv
## 1、创建虚拟环境
> python3.7 -m venv ENV         （ENV should be replaced by the desired name for the new environment）
## 2、Python环境下有三个文件夹
_**bin/**_ :    This is where the new Python executable and scripts/executables provided by other packages are stored.(Windows中改为 **_Scripts/_** )

_**lib/ and include/**_ :     These directories contain the supporting library files for new Python inside the virtual environment. The new packages will be installed in ENV/lib/pythonX.Y/site-packages/ .
## 3、激活虚拟环境
> source ENV/bin/activate   （UNIX）
# 二、 系统环境隔离-Vagrant
## create a new file named  Vagrantfile in the current working directory
> vagrant init
## vagrantfile is ready, run your virtual machine using the following command
> vagrant up
## connect to it through SSH using the following shorthand
> vagrant ssh
# 三、Docker
略略略
