import socket
import sys

ttl = 1

host_IP = socket.gethostbyname(sys.argv[1])

def send():
    sock = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    sock.setsockopt(socket.IPPROTO_ICMP,socket.IP_HDRINCL,ttl)
    sock.sendto(b"",(host_IP,80))

def receive():
    # Raw packet sending icmp echo request
    sock = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    sock.setsockopt(socket.IPPROTO_ICMP,socket.IP_HDRINCL,ttl)
    sock.bind(("127.0.0.1",80))

    while True:
        data,addr = sock.recvfrom(1024)
        print(f"reply received from {addr}")

send()
receive()

'''setsockopt(): is used to control socket behaviour like allocate buffer size, control timeout etc'''
