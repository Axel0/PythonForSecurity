import socket
import threading

ip="0.0.0.0"
port=9999
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip, port))

server.listen(5)

print "Listeining on port %s:%d"% (ip,port)

def handle_client(client_socket):
    request=client_socket.recv(1024);
    print "[+]-Received %s"%request
    client_socket.send("OK")
    client_socket.close()
    
while True:
    client,addr=server.accept()
    print "[+]-Connection accepted from %s:%d"% (addr[0],addr[1])
    
    client_handler=threading.Thread(target=handle_client, args=(client,)) 
    #the args has comma because it accepts tuples. When there's 1 param comma needed to distinguish from other types
    client_handler.start()
    
    
