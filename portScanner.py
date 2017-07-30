import argparse
from socket import *

def main():
    parser=argparse.ArgumentParser('Smart TCP Client Scanner')
    parser.add_argument("-a", "--address", type=str, help="The target IP address")
    parser.add_argument("-p", "--port", type=str, help="The port number")
    args=parser.parse_args()
    
    ipaddress=args.address
    portNumbers=args.port.split(',')
    
    portScan(ipadrress,portNumbers)
    
if __name__=="__main__":
    main()
    
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print "[-] Error: Unknown Host"
        exit(0)
        
    try:
        tgtName=gethostbyaddr(tgtIP)
        print "[+]--- Scan result for:"+ tgtName[0] + "---"
    except:
        print "[+]--- Scan result for:"+ tgtIP[0] + "---"
        
    setdefaulttimeout(10)
    
    for tgtPort in tgtPorts:
        connScan(tgtHost, int(tgtPort))
        
        
def connScan(tgtHost,tgtPort):
    try:
        
        connSock=socket(AF_INET,SOCK_STREAM)
        connSock.connect((tgtHost, tgtPort))
        print "[+] %d tcp open "% tgtPort
        printBanner(connSock, tgtPort)
        
    except:
        print "[+] %d tcp closed"% tgtPort
    
    finally:
        connSock.close()
def printBanner(connSock, tgtPort):
    try:
        if(tgtPort==80):
            connSock.send("GET HTTP/1.1 \r\n")
        else:
            connSock.send("\r\n")
            
        results=connSock.recv(4096)
        print "[+] Banner:"+str(result)
    except:
        print "[-] Banner not available\n"
    
    
                    