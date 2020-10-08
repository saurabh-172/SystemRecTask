# SystemRecTask
# Task Name: Networks

In this task we build a program in which we try to get the different IP's addresses from 
where our packet is sent through i.e. the addresses of different router's used in the  
route to forward this packet to its destination.  

*It uses a similar logic which is used in tracert in windows and tracepath which is in linux.*  

**Code is written in python using sockets**  
The code sends a UDP(user datagram protocol) packet, UDP used because we need speed and becaue  
this message will be empty as we just aim to get the destination/host IP address so this packet  
will not need reliability. it is sent on a socket with some TTL(time to live) 1st packet will be  
having less value of TTL (example 1) because of which the packet will be discarded because at  
every hop the TTL value in the packet is decremented and so an ICMP(internet control message protocol)  
message will be sent back to us mentioning that the TTL got expiered from that respective router  
and this ICMP packet will be containing that router's IP address as source address which we want  
and then we will increment TTL by 1 and again send the packet. like this we will be getting IP  
address's of all routers present in the path.

**But not all router's reply or send ICMP message they are not just designed like it, so they  
will just drop the packet.** In this case we print "package dropped" or something similar.
