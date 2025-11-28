
def get_flag(msg):
    return None
    
def get_ciaddr(msg):
    return None


def get_hlen(msg): #gets mac address length 
    return msg[2]


def print_chaddr(msg):
    hlen = get_hlen(msg)

    print("Client's MAC Address is " + format(msg[28], 'x'), end='') 

    for i in range(29, 28+hlen): #Prints MAC ADDRESS
        print(":" + format(msg[i], 'x'), end='') #'x' prints in hexadecimal, end ='' is dont add a new line

    print()


def get_chaddr(msg):
    hlen = get_hlen(msg)

    mac_address = msg[28:28+hlen]

    return mac_address


def get_xid(msg):
    return None

def is_unicast(msg):
    return None


