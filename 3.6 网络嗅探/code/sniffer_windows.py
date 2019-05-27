# -*- coding: UTF-8 -*-
import  os
import  socket
import  ctypes

class PromiscuousSocket (object): 
  def __init__(self):
      HOST = socket.gethostbyname(socket.gethostname())
      s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
      s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
      s.bind((HOST, 0))
      s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

      self.s = s
  
  def __enter__(self):
      return self.s

  def __exit__(self, *args, **kwargs):
      self.s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

def sniffer(count, bufferSize=65565):
    with PromiscuousSocket() as s:
        for i in range(count):
          package = s.recvfrom(bufferSize)
          print(package)



if __name__ == '__main__':
    sniffer(count=10) 