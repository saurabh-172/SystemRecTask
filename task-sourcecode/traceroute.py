import socket
import sys

#setting Time-To-Live for sending packets
ttl = 1
#getting the IP address of the host to which message is being sent
host_IP = socket.gethostbyname(sys.argv[1])

def send(ttl):
    #creating UDP scoket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #setting ttl for the message to be sent
    sock.setsockopt(socket.IPPROTO_IP,socket.IP_TTL,ttl)
    #sending the message
    sock.sendto(b"",(host_IP,5000))

def receive():
    ttl=1
    # creating raw socket for receiving icmp messages
    sock = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    print("listening...")
    #listening to incoming icmp messages
    while(1):
        #receiving the data and addresss of the router sending it
        data,addr = sock.recvfrom(1024)
        print(f"{addr[0]}")
        #if received ip address equal to the final destination host IP then stop listening
        if addr[0]==host_IP:
            break
        #if not then increament ttl and send
        ttl+=1
        send(ttl)
send(ttl)
receive()

