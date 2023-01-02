# import scapy.all as scapy
# request = scapy.ARP()
# print(request.show())
from scapy .all import *
# ip =IP()
#
# print(ip)
# print(ip.show())


from scapy.all import *
# my_frame = ether() /tcp()
# print(my_frame)
# print(my_frame.show())

# from scapy.all import *
# s = IP(dst="google.com")/ICMP()
# print(s.show())







# from scapy.all import *
# a =IP(ttl=10)
# print(a)
# print(a.src)
#
# a.dst="192.168.1.1"
# print(a)
# print(a.src)
#
# del(a.ttl)
# print(a.show())
#
# b=IP()
# print (b.show())

# c=IP()/TCP()
# print(c.show())
#
# d = Ether()/IP()/TCP()
# print(d.show())
#
# e = IP()/TCP()/"GET /HTTP/1.0\r\n\r\n"
# print(e.show())
# j = a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET/index/html HTTP/1.0\n\n"
# print(hexdump(j))


import pexpect
print(pexpect.run('echo hello'))
