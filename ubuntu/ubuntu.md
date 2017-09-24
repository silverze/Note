# Ubuntu 学习使用笔记

## 工具

### 画图工具 kolourpaint
该图片编辑工具还是比较大的，类似于windows下的画图软件  
安装命令：`sudo apt-get install kolourpaint4`

### atom手动安装插件
```
cd ~/.atom/packages
# 比如：git clone https://atom.io/packages/emmet
git clone <你想安装的 Package 的仓库链接>
cd <Package 路径> # cd emmet-atom
npm install

```

### 快捷键
```
终端清屏　ctrl+l
移到当前命令开头　ctrl+a
移到当前命令结尾　ctrl+e
将光标前的命令清楚 ctrl+u
```
### 硬链接＆软链接
- 文件可以创建硬链接与软链接，文件夹只能创建软链接
- 默认使用ln命令创建的是硬链接，硬链接一般用来保存重要文件，防止意外删除  

使用ln 命令创建一个文件夹的软链接，类似于windows中的快捷方式，ln -s src dist,
注意使用全路径,例如：需要在/home/user/目录下创建一个mstar软链接指向/mnt/hgfs/Mstar/：    
` ln -s /mnt/hgfs/Mstar/ /home/user/mstar `

## 解压缩
1. 对于.tar.gz压缩文件使用命令　`tar -zxvf filename.tar.gz`  
2. 对于.zip压缩文件使用命令　`unzip filename.zip`
