# smb 网络映射本次磁盘

## 安装smb: 
 'sudo apt-get install samba'

## smb服务添加用户，并设置密码：    
'sudo smbpasswd -a (your_username)'

## 安装完成后，修改配置文件，在/etc/samba/smb.conf文件最后添加：  
```shell
#share setting 
[silver]
path = /home/silver
available = yes
browseable = yes
public = yes
writable = yes
valid users = silver

read only = no
```

## 配置完成后source一下：  
`sudo source /etc/samba/smb.conf`

## 重启smb服务  
`sudo service smbd restart`