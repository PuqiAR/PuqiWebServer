import os
import HttpWebServer
import time as t
import sys
Server_List = []
Server_Bind_Ip = {
    'HelloPuqiWebServer':'127.0.0.1'
}
Server_Bind_Port = {
    'HelloPuqiWebServer':8900
}
Server_Index_Info = {
    'HelloPuqiWebServer':'index.html'
}
r = os.path.dirname(__file__ ) + '/'
print(r)
file = open(r + '/ServerInfo/Server_list/Server.txt')
for l in file:
    kv = l.strip()
    Server_List.append(l)
file.close()

file = open(r + '/ServerInfo/Bind_Ip/Server.txt')
for l in file:
    kv = l.strip().split(':')
    Server_Bind_Ip[kv[0]] = kv[1]
file.close()

file = open(r + '/ServerInfo/Bind_Port/Server.txt')
for l in file:
    kv = l.strip().split(':')
    Server_Bind_Port[kv[0]] = kv[1]
file.close()
Site_Contect = ''

file = open(r + '/ServerInfo/Index_Info/Server.txt')
for l in file:
    kv = l.strip().split(':')
    Server_Index_Info[kv[0]] = kv[1]
file.close()
#Start
#判断是否有Args
if (len(sys.argv)==1):
    pass #无参数
else:
    if(len(sys.argv)==2):
        StartServerName = sys.argv[1] #PuqiWebServer.py [ServerName]
        if(StartServerName in Server_List):
            HttpWebServer.PuqiWebServer.HttpWebServer.HttpWebServer_Start(StartServerName, Server_Bind_Ip[StartServerName], Server_Bind_Port[StartServerName], Server_Index_Info[StartServerName], False)
        else:
            print("Can not find server",StartServerName)
print('Load Done......')
print('Data:',Server_List,Server_Bind_Ip,Server_Bind_Port)  
while (True):
    Command = str(input('''
    Input Command(StartServer)
    '''))
    if (Command == 'exit'):
        exit
    if (Command == 'StartServer'):
        Command = str(input('InputServerName:'))
        print('Loading HttpWebServer...')
        t.sleep(0.8)
        print('Done......\nStartServer......')
        if (Command in Server_List):
            HttpWebServer.PuqiWebServer.HttpWebServer.HttpWebServer_Start(Command,Server_Bind_Ip[Command],Server_Bind_Port[Command],Server_Index_Info[Command],False)
        else:
            print('Can not find Server:',Command,'in ServerList!')
