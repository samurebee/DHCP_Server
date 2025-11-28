from socket import *
import helper_func


#references https://avocado89.medium.com/dhcp-packet-analysis-c84827e162f0

def gen_ip():

    ip = random.randint(0, 255)

    

#DHCP OFFER, yiaddr = offered ip, siaddr = server ip, chaddr = clients mac addy

def dhcp_offer(xid, yiaddr, siaddr = socket.inet_aton(192.168.0.1), chaddr, broadcast_flag, ciaddr):

    packet = b''

    op = struct.pack('!B',2)
    htype = struct.pack('!B',1)
    hlen = struct.pack('!B',6)
    hops = struct.pack('!B',1)
    xid = struct.pack('!I',helper_func.get_xid())
    sec = struct.pack('!H',60)

    flags = struct.pack('!H',helper_func.is_unicast()) #FIX

    ciaddr = socket.inet_aton(helper_func.get_ciaddr()) #client has no ip initially thus 0.0.0.0

    yiaddr = "192.168.0.2"    #gen_ip() #FINISH, 192.168.0.0/24 HARD CODED COME BACK

    #siaddr is assigned above 

    giaddr = socket.inet_aton(helper_func.get_giaddr()) #https://www.rfc-editor.org/rfc/rfc2131.html#section-4.1 pg22, we set this to 0 since server and client are on the same subnet

    chaddr = socket.inet_aton(chaddr) #client hardware address, or client mac addy

    sname = b'\x00' * 64 #not relevant come back to this 


    file = b'\x00' * 128 #not relevant come back to this 

    magic_cookie = 

    options 





    
