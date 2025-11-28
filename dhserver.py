
#dhcp offer, request, ack functions 

import struct 
from socket import *

#import dhcp_func
import helper_func



DHCP_SERVER = ('', 67)
DHCP_CLIENT = ('255.255.255.255', 68)

# Create a UDP socket
s = socket(AF_INET, SOCK_DGRAM)

# Allow socket to broadcast messages
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# Bind socket to the well-known port reserved for DHCP servers
s.bind(DHCP_SERVER)

# Receive a UDP message, clients mac address
msg, addr = s.recvfrom(1024) #IP: 0.0.0.0, PORT: 68


# Print the client's MAC Address from the DHCP header
#print("Client's MAC Address is " + format(msg[28], 'x'), end='') 
xid = msg[4:8]
xid = struct.unpack('!I', xid)[0]

# for i in range(29, 34): #Prints MAC ADDRESS
#     print(":" + format(msg[i], 'x'), end='') #'x' prints in hexadecimal, end ='' is dont add a new line
# print()

helper_func.print_chaddr(msg)

print("Client's transaction id is {}".format(hex(xid)))

#DHCP Offer
# dhcp_offer()


# Send a UDP message (Broadcast) 
s.sendto(b'Hello World!', DHCP_CLIENT)