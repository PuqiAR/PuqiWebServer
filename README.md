# PuqiWebServer
 A Python WebServer
<p style="font-size:30px;color:blue">PuqiWebServer</p>
<img src="https://img.shields.io/badge/-WebServer-ff69b4">
PuqiWebServer-基于Python的Web服务器
Usage：Python 3.* Lib:socket,os,sys,threading

Hello PuqiWebServer!
默认有一个网站:HelloPuqiWebServer
命令行启动输入:StartServer并输入网站名称启动网站

添加网站 & 删除:
在/ServerInfo文件夹里添加修改ServerList,在末尾加入要添加的网站名,在Bind-Ip末尾添加:[网站名]:[绑定IP] <去掉方括号>
Bind_Port末尾添加:[网站名]:[绑定端口] <去掉方括号> 在wwwroot里添加和网站名相同的文件夹,放入网站文件.
删除: 直接在ServerInfo里删掉对应的信息就行，wwwroot里删除文件夹

Hello PuqiWebServer!