#PuqiWebServer-HttpWebServerModule By PuqiAR#
#Coding:Utf-8
#Py3.*
#anthor:PuqiAR
#  Hello Puqi Web Server !
import socket
import os
import threading
r = os.path.dirname(__file__ ) + '/'
#运行目录
class PuqiWebServer():
    class tools():
        def r_file_rb(file):
            try:
                with open(file,'rb') as f:
                    data = f.read()
                    return data
            except Exception as e:
                return e
    class HttpWebServer():
        def HttpWebServer_Machine(n_socket,Client_Data,ServerName,Index_Info):
            Client_Data_Contect = Client_Data.decode('utf-8')
            Request_Data = Client_Data_Contect.split(" ",maxsplit=2)
            Request_Path = Request_Data[1]
            #print('From:',ServerName,'Request_Path:',Request_Path)
            if (Request_Path == '/'):
                Request_Path = '/' + Index_Info #请求目录
            try:
                with open(r + '/wwwroot/'+ServerName + Request_Path,'rb') as f:
                    file_Data = f.read() #读取访问文件
            except Exception as e:
                #404-File Not Found
                Reponse_Line = "HTTP/1.1 404 Not Found\r\n".encode('utf-8')
                Reponse_Header = "Server: PWS1.0\r\n".encode('utf-8')
                with open(r + '/Static/Error/404/404.html','rb') as f:
                    file_Data = f.read()
                Reponse_Body = file_Data
                Reponse_Data = (Reponse_Line + Reponse_Header + "\r\n".encode('utf-8')+Reponse_Body)
                n_socket.send(Reponse_Data) #发送数据
            else:
                #HTTP/1.1 200 OK
                Reponse_Line = "HTTP/1.1 200 OK\r\n".encode('utf-8')
                Reponse_Header = "Server: PWS1.0\r\n".encode('utf-8')
                Reponse_Body = file_Data
                Reponse_Data = (Reponse_Line + Reponse_Header + "\r\n".encode('utf-8') + Reponse_Body)
                n_socket.send(Reponse_Data) #发送数据
            finally:
                #关闭new_Socket
                n_socket.close()
        def HttpWebServer_Start_Reponse_Client(ServerName,Bind_Ip,Bind_Port,Index_Info):
            Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            try:
                #绑定
                Server.bind((str(Bind_Ip),int(Bind_Port)))
            except OSError as e:
                #绑定错误
                print("StartServerErr!Err",e,"Try to change IP/Port!")
                Server.close()
            finally:
                #监听
                Server.listen(128) #监听数量128
            while (True):
                if (Index_Info == ''): #未设置主页，主页为/index.html
                    Index_Info = '/index.html'
                n_socket,Ip_Port = Server.accept() #接受连接
                #print('Server:',ServerName,'From:',Ip_Port,'Request received')
                Client_Data = n_socket.recv(4096)#接收数据
                if (len(Client_Data) == 0):
                    print('Server:',ServerName,'From:',Ip_Port,'Closed!')
                    n_socket.close()
                    return 'close' #浏览器关闭
                #创建子线程处理客户端请求
                Th = threading.Thread(target=PuqiWebServer.HttpWebServer.HttpWebServer_Machine,args=(n_socket,Client_Data,ServerName,Index_Info))
                #n_socket,Client_Data,ServerName,Index_Info
                Th.setDaemon(True)
                Th.start() #启动
                

        def HttpWebServer_Start(Server_Name,ServerIp,ServerPort,Index_Info,exit):
            print('StartServer:',Server_Name,'on',ServerIp,':',ServerPort)
            PuqiWebServer.HttpWebServer.HttpWebServer_Start_Reponse_Client(Server_Name,ServerIp,ServerPort,Index_Info)
                    
                