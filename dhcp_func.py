from helper_func import *


#references https://avocado89.medium.com/dhcp-packet-analysis-c84827e162f0 (errors in the article)


#DHCP OFFER, yiaddr = offered ip, siaddr = server ip, chaddr = clients mac addy
#https://www.rfc-editor.org/rfc/rfc2131.html#section-4.1 

def dhcp_offer(discover_pkt):
    offer_pkt = b''

    op = struct.pack('!B',2) 

    htype = get_htype(discover_pkt)

    hlen = get_hlen(discover_pkt)

    hops = get_hops(discover_pkt)

    xid = get_xid(discover_pkt)
    
    sec = get_sec(discover_pkt)

    flags = get_flag(discover_pkt) #FINISH use isUnicast()

    ciaddr = inet_aton("0.0.0.0") #client has no ip thus 0.0.0.0

    yiaddr = inet_aton("192.168.0.10") #ip were offering

    siaddr = inet_aton(get_siaddr()) #our/server ip, change to global value later

    giaddr = inet_aton(get_giaddr())

    chaddr = get_chaddr_raw(discover_pkt) #client mac address

    sname = b'\x00' * 64 #not used

    file = b'\x00' * 128 #not used 

    options = build_options(discover_pkt)

   
    offer_pkt =  op + htype + hlen + hops + xid + sec + flags + ciaddr + yiaddr + siaddr + giaddr + chaddr + sname + file + options

    return offer_pkt

def dhcp_ack(msg):
    return None








    
