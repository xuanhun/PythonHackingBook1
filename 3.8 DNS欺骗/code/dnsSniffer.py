# -*- coding: UTF-8 -*-
from scapy.all import *

scapy.config.conf.sniff_promisc=True #设置混杂模式

def packetHandler(pkt):
    print(pkt.summary())
    udp = pkt.getlayer(UDP)
    print(udp.show())
if __name__ == '__main__':
    dev = "en0"
    filter = "udp port 53"
    sniff(filter=filter,prn=packetHandler,iface=dev)
   
