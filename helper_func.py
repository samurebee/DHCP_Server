
import struct 
from socket import *

#GET FUNCTIONS
def get_flag(msg):

    flag = struct.unpack('!H',msg[10:12])[0]    

    return flag
    
def get_ciaddr(msg):
    ciaddr = msg[12:16]

    return inet_ntoa(ciaddr)

def get_hlen(msg): #gets mac address length 
    return msg[2]

def get_chaddr(msg):
    hlen = get_hlen(msg)

    mac_address = msg[28:28+hlen]

    return mac_address


def get_xid(msg):
    xid = msg[4:8] #bytes 4-7

    return xid

def get_giaddr():
    return inet_ntoa("0.0.0.0") 

def is_unicast(msg):

    # if get_giaddr() == "0.0.0.0" and get_flag(msg) == 0 and get_ciaddr(msg) == "0.0.0.0": #FINISH, only handles 1 case 
    #     return 1

    return 0

#PRINT FUNCTIONS

def print_chaddr(msg):
    hlen = get_hlen(msg)

    print("Client's MAC Address is " + format(msg[28], 'x'), end='') 

    for i in range(29, 28+hlen): #Prints MAC ADDRESS
        print(":" + format(msg[i], 'x'), end='') #'x' prints in hexadecimal, end ='' is dont add a new line

    print()

def print_xid(msg):
    print("Client's transaction id is {}".format(hex(get_xid(msg))))

def print_flag(msg):

    print("Clients flag bit is set to {}".format(hex(get_flag(msg))))

def print_ciaddr(msg):
    ciaddr = get_ciaddr(msg)

    print("Clients IP Adress is {}".format(inet_ntoa(ciaddr)))

def print_giaddr():
    print("Gateway IP Adress is {}".format(inet_ntoa(get_giaddr()))) #raw bytes -> string




