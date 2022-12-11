import os
Command = ''
print('PuqiWebServerManager v1.2.10\n')
while True:
    Command = str(input('root@PuqiWebServer $'))
    if (Command == 'exit'):
        exit()
    if (Command == 'add'):
        ServerName = str(input('InputServerName:'))
        Server_Bind_Ip = str(input('InputServer_Bind_Ip:'))
        Server_Port = str(input('InputServer_Port:'))
        Server_Index_Info = str(input('InputIndex_File_Info(Default:index.html):'))
        if (ServerName == '' or Server_Bind_Ip == '' or Server_Port == ''):
            print('Error:ServerName or IP or Port Can not be '' !')
            break
        else:
            if Server_Index_Info == '\n':
                Server_Index_Info = 'index.html'
            file = open('../ServerInfo/Server_list/Server.txt','a')
            file.write('\n' + ServerName + '\n')
            file = open('../ServerInfo/Bind_Ip/Server.txt','a')
            file.write('\n' + ServerName + ':' + Server_Bind_Ip)
            file = open('../ServerInfo/Bind_Port/Server.txt','a')
            file.write('\n' + ServerName + ':' + Server_Port)
            file = open('../ServerInfo/Index_Info/Server.txt','a')
            file.write('\n' + ServerName + ':' + Server_Index_Info)
            os.mkdir('../wwwroot/' + ServerName)
            print('Server Create !')
os.system("pause")