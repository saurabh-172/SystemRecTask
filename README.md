# SystemRecTask
# Task Name: Networks

In this task we build a program similar to traceroute. whenever you browse on internet clicking  
on some website link a **request** message is sent from your system to **server** which has whole  
database of that site and it sends those information as a **reply** to your request which the  
browser gets and renders it according to structure mentioned in the webpage code. the message  
traverse from many intermediate machines which are called **routers** which are responsible for  
routing the message packet path back to us. all these routers have a unique address called **IP  
address** i.e. **Internet Protocol address**. we are interested to find all the ip addresses of  
all these routers from which our request message packet traverse to reach the server.

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
will just drop the packet.** In this case we will just print "package dropped" or something similar.
