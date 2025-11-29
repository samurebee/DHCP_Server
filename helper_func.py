
import struct 
import time
import ipaddress
from socket import *


#IP Pool 
leases = {}
pending_offers = {}

def get_pool():
    net = ipaddress.ip_network("192.168.0.0/24")

    pool = [
        str(ip)
        for ip in net.hosts()
        if str(ip) != "192.168.0.1"
    ]
    return pool

# def assign_ip(chaddr):

#     if leases[chaddr] in leases and leases[mac][expires_at] :
        


#     ip = ipaddress.ip_network("192.168.0.0/24")

#     leases[chaddr] = {"ip": ip, "expires_at": None}

#     return None 

   


#GET FUNCTIONS

def get_htype(msg):
    return msg[1:2]

def get_hlen(msg): #gets mac address length 
    return msg[2:3]

def get_hops(msg):
    return msg[3:4]

def get_xid(msg):
    xid = msg[4:8] #bytes 4-7

    return xid

def get_sec(msg):
    sec = msg[8:10]

    return sec

def get_flag(msg):
    flag = msg[10:12]  

    return flag
    
def get_ciaddr(msg): #Should be 0.0.0.0
    ciaddr = msg[12:16]

    return inet_ntoa(ciaddr)

def get_siaddr(): 
    return "192.168.0.1"

def get_giaddr():
    return "0.0.0.0" #on LAN, change later to work with relay agent 


def get_chaddr_raw(msg): 
    hlen = get_hlen(msg)
    hlen = struct.unpack('!B', hlen)[0]
    mac = msg[28:28+hlen]

    return mac

def get_chaddr(msg): 
    hlen = get_hlen(msg)

    hlen = struct.unpack('!B', hlen)[0]

    mac_bytes = msg[28:28+hlen]

    mac = ':'.join('%02x' % b for b in mac_bytes)

    return mac



def is_unicast(msg): #READ ABOUT
    return None

def get_leasetime():
    return 60

#PRINT FUNCTIONS FINISH

def print_chaddr(msg):
    print("Client's MAC Address is {}".format(get_chaddr(msg)))

def print_xid(msg):
    print("Client's transaction id is {}".format(hex(struct.unpack("!I",get_xid(msg))[0])))

# def print_flag(msg):
#     print("Clients flag bit is set to {}".format(hex(get_flag(msg))))

# def print_ciaddr(msg):
#     ciaddr = get_ciaddr(msg)

#     print("Clients IP Adress is {}".format(inet_ntoa(ciaddr)))

# def print_giaddr():
#     print("Gateway IP Adress is {}".format(inet_ntoa(get_giaddr()))) #raw bytes -> string


#BUILD OPTIONS 
#https://www.rfc-editor.org/rfc/rfc2132

def build_options(msg):
    options = b''

    magic_cookie = b'\x63\x82\x53\x63' # "99.130.83.99", pg3 of rfc 2132

    options += magic_cookie

    options += struct.pack("!BBB", 53, 1, 2) # TLV, type | length(of value) | value, 53 = DHCP message type  

    options += struct.pack("!BB", 54,4) + inet_aton(get_siaddr()) # code | len | ipv4, 54 = server identifier 

    options += struct.pack("!BBI",51,4,60) #lease time

    options += struct.pack("!BB",1,4) + inet_aton("255.255.255.0") #subnet mask 

    #FINISH: ADD OP 3

    #FINISH: ADD OP 6

    options += struct.pack("!B",255) #END 

    return options 


def decode_message_type(msg):
    opts = msg[240:]
    i = 0
    while i < len(opts):
        if opts[i] == 53:  #DHCP Message Type
            return opts[i+2]  #value at index after length
        if opts[i] == 255:  #END option
            break
        i += 2 + opts[i+1]
    return None

    


    
    





    

    


