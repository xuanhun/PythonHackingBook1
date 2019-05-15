# -*- coding: UTF-8 -*-

import socket
import sys
import selectors
import types

# 测试类


class Client:
    def __init__(self, host, port, numConn):
        self.host = host  # 待连接的远程主机的域名
        self.port = port
        self.message = [b'message 1 from client', b'message 2 from client']
        self.numConn = numConn
        self.selector = selectors.DefaultSelector()

    def connet(self):  # 连接方法
        server_addr = (self.host, self.port)
        for i in range(0, self.numConn):
            connid = i + 1
            print('开始连接', connid, '到', server_addr)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setblocking(False)
            sock.connect_ex(server_addr)#连接服务端
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
            data = types.SimpleNamespace(connid=connid,
                                     msg_total=sum(len(m) for m in self.message),
                                     recv_total=0,
                                     messages=list(self.message),
                                     outb=b'')
            self.selector.register(sock, events, data=data)

        try:
            while True:
                events = self.selector.select(timeout=1)
                if events:
                    for key, mask in events:
                        self.service_connection(key, mask)

        finally:
            self.selector.close()
        
    def service_connection(self,key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  
            if recv_data:
                print("收到", repr(recv_data), "来自连接", data.connid)
                data.recv_total += len(recv_data)
            if not recv_data or data.recv_total == data.msg_total:
                print("关闭连接：", data.connid)
                self.selector.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if not data.outb and data.messages:
                data.outb = data.messages.pop(0)
            if data.outb:
                print("发送", repr(data.outb), "到连接", data.connid)
                sent = sock.send(data.outb)  #发送数据
                data.outb = data.outb[sent:]#清空数据



if __name__ == '__main__':
    cl = Client('127.0.0.1', 8800, 5)
    cl.connet()
