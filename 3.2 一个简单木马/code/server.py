# -*- coding: UTF-8 -*-

import socket
import sys
import os


class server:
    def __init__(self, ip, port):
        self.port = port
        self.ip = ip
        self.bufferSize = 10240

    def start(self):  # 启动监听，接收数据
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.ip, self.port))  # 绑定
            s.listen(10)  # 监听
            print('等待客户端连接')
            while True:  # 一直等待新的连接
                try:
                    conn, addr = s.accept()  # 接收连接
                    print('客户端连接 ' + addr[0] + ':' + str(addr[1]))
                    while True:  # 不知道客户端发送数据大小，循环接收
                        data = conn.recv(self.bufferSize)
                        if not data:
                            break
                        else:
                            self.executeCommand(conn,data)
                    conn.close()
                except socket.error as e:
                    print(e)
                    conn.close()  # 关闭连接
        finally:
            s.close()  # 关闭服务端

    def executeCommand(self, tcpCliSock, data):  # 解析并执行命令
        try:#
            message = data.decode("utf-8")
            if os.path.isfile(message):#判断是否是文件
                filesize = str(os.path.getsize(message))#获取文件大小
                print("文件大小为：",filesize)
                tcpCliSock.send(filesize.encode())#发送文件大小
                data = tcpCliSock.recv(self.bufferSize)  
                print("开始发送")
                f = open(message, "rb")#打开文件
                for line in f:
                    tcpCliSock.send(line)#发送文件内容
            else:
                tcpCliSock.send(('0001'+os.popen(message).read()).encode('utf-8'))
        except:
            raise



if __name__ == '__main__':
    s = server('', 8800)
    s.start()
