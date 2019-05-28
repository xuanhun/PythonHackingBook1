# -*- coding: UTF-8 -*-

import argparse
from scapy.all import *

bannerText="""
██╗  ██╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗██╗   ██╗███╗   ██╗
╚██╗██╔╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██║   ██║████╗  ██║
 ╚███╔╝ ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║██╔██╗ ██║
 ██╔██╗ ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║██║╚██╗██║
██╔╝ ██╗╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                                 

端口扫描器 by 玄魂工作室
微信订阅号 : xuanhun521
Github  : https://github.com/xuanhun                                                                                     
    """


#答疑端口状态
def print_ports(port, state):
	print("%s | %s" % (port, state))

def tcpScan(target,ports):
    print("tcp全连接扫描 %s with ports %s" % (target, ports))
    for port in ports:
        send=sr1(IP(dst=target)/TCP(dport=port,flags="S"),timeout=2,verbose=0)
        if (send is None):
            print_ports(port,"closed")
        elif send.haslayer("TCP"):
            print(send["TCP"].flags)
            if send["TCP"].flags == "SA":
                send_1 = sr1(IP(dst=target) / TCP(dport=port, flags="AR"), timeout=2, verbose=0)
                print_ports(port,"opend")
            elif send["TCP"].flags == "RA":
                print_ports(port,"closed")

    
def synScan(target,ports):
    print("tcp SYN扫描 %s with ports %s" % (target, ports))
    for port in ports:
        send=sr1(IP(dst=target)/TCP(dport=port,flags="S"),timeout=2,verbose=0)
        if (send is None):
            print_ports(port,"closed")
        elif send.haslayer("TCP"):
            print(send["TCP"].flags)
            if send["TCP"].flags == "SA":
                send_1 = sr1(IP(dst=target) / TCP(dport=port, flags="R"), timeout=2, verbose=0)#只修改这里
                print_ports(port,"opend")
            elif send["TCP"].flags == "RA":
                print_ports(port,"closed")
    
def ackScan(target,ports):
    print("tcp ack扫描 %s with ports %s" % (target, ports))
    for port in ports:
        ack_flag_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags="A"),timeout=5)
        print(str(type(ack_flag_scan_resp)))
        if (str(type(ack_flag_scan_resp))=="<class 'NoneType'>"):
            print_ports(port,"filtered")
        elif(ack_flag_scan_resp.haslayer(TCP)):
            if(ack_flag_scan_resp.getlayer(TCP).flags == "R"):
                print_ports(port,"unfiltered")
        elif(ack_flag_scan_resp.haslayer(ICMP)):
            if(int(ack_flag_scan_resp.getlayer(ICMP).type)==3 and int(ack_flag_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print_ports(port,"filtered")
        else:
            print_ports(port,"filtered")  


def windowScan(target,ports):
    print("tcp window扫描 %s with ports %s" % (target, ports))
    for port in ports:
        window_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags="A"),timeout=5)
        print(str(type(window_scan_resp)))
        if (str(type(window_scan_resp))=="<class 'NoneType'>"):
            print_ports(port,"close")
        elif(window_scan_resp.haslayer(TCP)):
            if(window_scan_resp.getlayer(TCP).window == 0):
                print_ports(port,"close")
            elif(window_scan_resp.getlayer(TCP).window > 0):
                print_ports(port,"open")
        else:
            print_ports(port,"close") 

def nullScan(target,ports):
    print("tcp NULL 扫描 %s with ports %s" % (target, ports))
    for port in ports:
        null_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags=""),timeout=5)
        if (str(type(null_scan_resp))=="<class 'NoneType'>"):
            print_ports(port,"Open|Filtered") 
        elif(null_scan_resp.haslayer(TCP)):
            if(null_scan_resp.getlayer(TCP).flags == "R" or null_scan_resp.getlayer(TCP).flags == "A"):
                print_ports( port,"Closed")
        elif(null_scan_resp.haslayer(ICMP)):
            if(int(null_scan_resp.getlayer(ICMP).type)==3 and int(null_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print_ports(port, "Filtered")

 
def finScan(target,ports):
    print("tcp FIN 扫描 %s with ports %s" % (target, ports))
    for port in ports:
        fin_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags="F"),timeout=5)
        if (str(type(fin_scan_resp))=="<class 'NoneType'>"):
            print_ports(port, "Open|Filtered")
        elif(fin_scan_resp.haslayer(TCP)):
            if(fin_scan_resp.getlayer(TCP).flags == 0x14):
                print_ports(port, "Closed")
        elif(fin_scan_resp.haslayer(ICMP)):
            if(int(fin_scan_resp.getlayer(ICMP).type)==3 and int(fin_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print_ports(port, "Filtered")


def xmaxScan(target,ports):
    print("tcp xmax 扫描 %s with ports %s" % (target, ports))
    for port in ports:
        fin_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags="FPU"),timeout=5)
        if (str(type(fin_scan_resp))=="<class 'NoneType'>"):
            print_ports(port, "Open|Filtered")
        elif(fin_scan_resp.haslayer(TCP)):
            if(fin_scan_resp.getlayer(TCP).flags == "R"):
                print_ports(port, "Closed")
        elif(fin_scan_resp.haslayer(ICMP)):
            if(int(fin_scan_resp.getlayer(ICMP).type)==3 and int(fin_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print_ports(port, "Filtered")

def udpScan(target,ports):
    print("UDP 扫描 %s with ports %s" % (target, ports))
    for port in ports:
        udp_scan_resp = sr1(IP(dst=target)/UDP(dport=port),timeout=5)
        if (str(type(udp_scan_resp))=="<class 'NoneType'>"):
            print_ports(port, "Open|Filtered")
        elif(udp_scan_resp.haslayer(UDP)):
            if(udp_scan_resp.getlayer(TCP).flags == "R"):
                print_ports(port, "Open")
        elif(udp_scan_resp.haslayer(ICMP)):
            if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print_ports(port, "Filtered")


if __name__ == '__main__':

    print(bannerText)

    parser = argparse.ArgumentParser("")
    parser.add_argument("-t", "--target", help="目标IP", required=True)
    parser.add_argument("-p", "--ports", type=int, nargs="+", help="指定端口列表 (21 23 80 ...)")
    parser.add_argument("-s", "--scantype", help="""
    "T":全连接扫描
    "S":syn扫描
    "A":ack扫描
    "W":TCPwindow扫描
    "N":NULL扫描
    "F":FIN扫描
    "X":Xmas扫描
    "U":UDP扫描
    """, required=True)
    args = parser.parse_args()
    print(args)
    target = args.target
    scantype = args.scantype
    if args.ports:
	    ports = args.ports
    else:
	    ports = range(1, 65535)

    # 扫码方式
    if scantype == "T":#全连接扫描
	    tcpScan(target,ports)
    elif scantype == "S":#syn扫描
	    synScan(target,ports)
    elif scantype == "A":#ack扫描
	    ackScan(target,ports)
    elif scantype == "W":#TCPwindow扫描
	    windowScan(target,ports)
    elif scantype == "N":#NULL扫描
	    nullScan(target,ports)
    elif scantype == "F":#FIN扫描
	    finScan(target,ports)
    elif scantype == "X":#Xmas扫描
	    xmaxScan(target,ports)
    elif scantype == "U":#UDP扫描
	    udpScan(target,ports)
    else:
	    print("不支持当前模式")

