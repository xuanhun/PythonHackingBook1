# -*- coding: UTF-8 -*-
from scapy.all import *

scapy.config.conf.sniff_promisc=True #设置混杂模式

def packetHandler(pkt):
    dport = pkt[IP][TCP].dport
    if dport==80 and pkt[IP][TCP].payload:
        print('捕获http请求：',pkt[IP][TCP].payload)
if __name__ == '__main__':
    sniff(filter='tcp and port 80',prn=packetHandler,iface='en0')
    