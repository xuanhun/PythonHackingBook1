# -*- coding: UTF-8 -*-

import socket
import sys
import re
import os

class Client:
    def __init__(self,serverIp,serverPort):
        self.serverIp=serverIp #待连接的远程主机的域名
        self.serverPort = serverPort
        self.bufferSize = 10240

    def connet(self): #连接方法
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print("Failed to create socket. Error: %s"%e)
            
        try:
            s.connect((self.serverIp,self.serverPort))
            while True:
                message = input('> ')#接收用户输入
                if not message:
                    break
                s.send(bytes(message, 'utf-8'))#发送命令
                data = s.recv(self.bufferSize)#接收数据
                if not data:
                    break
                if re.search("^0001",data.decode('utf-8','ignore')):#判断数据类型
                    print(data.decode('utf-8')[4:])
                else:#文件内容处理
                    s.send("File size received".encode())#通知服务端可以发送文件了
                    file_total_size = int(data.decode())#总大小
                    received_size = 0
                    f = open("new" +os.path.split(message)[-1], "wb")#创建文件
                    while received_size < file_total_size:
                        data = s.recv(self.bufferSize)
                        f.write(data)#写文件
                        received_size += len(data)#累加接收长度
                        print("已接收:", received_size)
                    f.close()#关闭文件
                    print("receive done", file_total_size, " ", received_size)
        except socket.error:
            s.close()
            raise #退出进程
        finally:
            s.close()


if __name__ == '__main__':
    cl = Client('127.0.0.1',8800)
    cl.connet()
    sys.exit() #退出进程

