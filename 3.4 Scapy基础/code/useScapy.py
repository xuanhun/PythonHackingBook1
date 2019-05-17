# -*- coding: UTF-8 -*-

import sys
from scapy.all import *

p=sr1(IP(dst='192.168.1.1')/ICMP())
if p:
    p.show()


