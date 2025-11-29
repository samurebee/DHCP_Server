
#dhcp offer, request, ack functions 

from dhcp_func import *
import helper_func
import dhcp_func
from socket import *



DHCP_SERVER = ('', 67)
DHCP_CLIENT = ('255.255.255.255', 68)

# Create a UDP socket
s = socket(AF_INET, SOCK_DGRAM)

# Allow socket to broadcast messages
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# Bind socket to the well-known port reserved for DHCP servers
s.bind(DHCP_SERVER)

# Receive a UDP message, clients mac address

# Print the client's MAC Address from the DHCP header
#print("Client's MAC Address is " + format(msg[28], 'x'), end='') 

# for i in range(29, 34): #Prints MAC ADDRESS
#     print(":" + format(msg[i], 'x'), end='') #'x' prints in hexadecimal, end ='' is dont add a new line
# print()


while True:
    msg, addr = s.recvfrom(1024)
    helper_func.print_chaddr(msg)
    helper_func.print_xid(msg)

    mtype = decode_message_type(msg)
    print("Received DHCP message type:", mtype, "from", addr)

    if mtype == 1:  # DISCOVER
        print("Handling DISCOVER")
        offer_pkt = dhcp_offer(msg)
        helper_func.print_xid(offer_pkt)
        s.sendto(offer_pkt, DHCP_CLIENT)
        print("Sent DHCPOFFER")

    elif mtype == 3:  # REQUEST
        print("Handling REQUEST")
        # later: ack_pkt = dhcp_ack(msg)
        # s.sendto(ack_pkt, DHCP_CLIENT)
        # print("  Sent DHCPACK")

    else:
        print("Unknown/unsupported type:", mtype)


# Send a UDP message (Broadcast) 
#s.sendto(b'Hello World!', DHCP_CLIENT)