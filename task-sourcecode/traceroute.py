import socket
import sys

# assgining IP for sending packets (source IP)
UDP_IP = "127.0.0.1"
#UDP_PORT = 5000

#getting host/destination IP from the hostname porvided as argument
hostIP = socket.gethostbyname(f"{sys.argv[1]}")
print(f"{hostIP}")

def sendPacket(hostIP):
    # creating UDP socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # sending the message packet with empty message to hostIP on HTTP port
    sock.sendto(b"",(hostIP,80))

def receivePacket():
    #creating UDP socket for receiving
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # binding the address to the socket
    sock.bind((UDP_IP,80))
    # listening for the packet to receive
    while True:
        #packet being received in chunks of 4096 size
        data,addr = sock.recvfrom(4096)
        print(f"{addr[0]}")

# sending packets
sendPacket(hostIP)

#receiving packets
receivePacket()
