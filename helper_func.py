
import struct 
from socket import *

#GET FUNCTIONS

def get_flag(msg):

    flag = struct.unpack('!H',msg[10:12])[0]    

    return flag
    
def get_ciaddr(msg): #Should be 0.0.0.0

    ciaddr = msg[12:16]

    return inet_ntoa(ciaddr)

def get_hlen(msg): #gets mac address length 
    return msg[2]

def get_chaddr(msg): #finish 
    hlen = get_hlen(msg)

    mac_bytes = msg[28:28+hlen]

    mac = ':'.join('%02x' % b for b in mac_bytes)

    return mac


def get_xid(msg):
    xid = msg[4:8] #bytes 4-7

    return struct.unpack("!I",xid)[0]

def get_giaddr():
    return inet_ntoa("0.0.0.0") 

def is_unicast(msg):

    # if get_giaddr() == "0.0.0.0" and get_flag(msg) == 0 and get_ciaddr(msg) == "0.0.0.0": #FINISH, only handles 1 case 
    #     return 1

    return 0

def get_siaddr(): #FIX: hard coded 
    return "192.168.0.1"

def get_leasetime():
    return 60

#PRINT FUNCTIONS

def print_chaddr(msg):

    print("Client's MAC Address is {}".format(get_chaddr(msg)))

def print_xid(msg):

    print("Client's transaction id is {}".format(hex(get_xid(msg))))

def print_flag(msg):

    print("Clients flag bit is set to {}".format(hex(get_flag(msg))))

def print_ciaddr(msg):

    ciaddr = get_ciaddr(msg)

    print("Clients IP Adress is {}".format(inet_ntoa(ciaddr)))

def print_giaddr():

    print("Gateway IP Adress is {}".format(inet_ntoa(get_giaddr()))) #raw bytes -> string


#BUILD OPTIONS 
#https://www.rfc-editor.org/rfc/rfc2132

def build_options(msg):

    options = b''

    magic_cookie = b'\x63\x82\x53\x63' # "99.130.83.99" #pg3 of rfc 2132

    options += struct.pack("!BBB", 53, 1, 2) # TLV, type | length(of value) | value, 53 = DHCP message type  

    options += struct.pack("!BB", 54,4,) + inet_aton(get_siaddr()) # code | len | ipv4, 54 = server identifier 

    option += struct.pack("!BB",51,4,get_leasetime())



    

    


