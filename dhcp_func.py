from helper_func import *


#references https://avocado89.medium.com/dhcp-packet-analysis-c84827e162f0 (errors in the article)

def gen_ip():

    ip = random.randint(0, 255)

    

#DHCP OFFER, yiaddr = offered ip, siaddr = server ip, chaddr = clients mac addy
#https://www.rfc-editor.org/rfc/rfc2131.html#section-4.1 

def dhcp_offer(msg):
    packet = b''

    op = struct.pack('!B',2) 

    htype = struct.pack('!B',get_htype(msg))

    hlen = struct.pack('!B',get_hlen(msg))

    hops = struct.pack('!B',get_hops(msg))

    xid = struct.pack('!I',get_xid(msg))

    sec = struct.pack('!H',get_sec(msg))

    flags = struct.pack('!H',get_flag(msg)) #FINISH use isUnicast()

    ciaddr = socket.inet_aton(get_ciaddr()) #client has no ip thus 0.0.0.0

    yiaddr =    

    siaddr = socket.inet_aton(get_siaddr()) #192.168.0.1

    giaddr = socket.inet_aton(get_giaddr()) 

    chaddr = socket.inet_aton(chaddr) #client hardware address, or client mac addy

    sname = b'\x00' * 64 #not relevant come back to this 

    file = b'\x00' * 128 #not relevant come back to this 

    options = build_options(msg)







    
