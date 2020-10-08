import socket
import sys

ttl = 1

host_IP = socket.gethostbyname(sys.argv[1])

def send():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP,socket.IP_TTL,ttl)
    sock.sendto(b"",(host_IP,5000))

def receive():
    ttl=1
    # Raw packet sending icmp echo request
    sock = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    print("listening...")
    while(sock.setsockopt(socket.SOL_IP,socket.IP_HDRINCL,ttl)==0):
        print(ttl)
        data,addr = sock.recvfrom(1024)
        print(f"{addr[0]}")
        ttl+=1
    print(ttl)
'''
    while True:
        data,addr = sock.recvfrom(1024)
        print(f"reply received from {addr}")
'''
send()
receive()

'''setsockopt(): is used to control socket behaviour like allocate buffer size, control timeout etc'''
