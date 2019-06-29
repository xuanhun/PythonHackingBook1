# -*- coding: UTF-8 -*-
import pywifi

def bies():
  wifi=pywifi.PyWiFi()#创建一个无限对象
  ifaces=wifi.interfaces()[0]#取一个无线网卡
  ifaces.scan()#扫描
  bessis=ifaces.scan_results()
  for i in range(len(bessis)):
    print(bessis[i].ssid, bessis[i].signal)


bies()