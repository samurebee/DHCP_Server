import struct 
import socket import *

#DHCP OFFER, yiaddr = offered ip, siaddr = server ip, chaddr = clients mac addy

#references https://avocado89.medium.com/dhcp-packet-analysis-c84827e162f0
def dhcp_offer(xid, yiaddr, siaddr, chaddr):

    packet = b''

    op = struct.pack('!B',2)
    htype = struct.pack('!B',1)
    hlen = struct.pack('!B',6)
    hops = struct.pack('!B',1)
    xid = struct.pack('!I',xid)
    sec = struct.pack('!H',60)
    flags = struct.pack('',)



    
