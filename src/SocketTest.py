'''
Created on May 30, 2011

@author: matthias
'''

import socket
from Config import Config

if __name__ == '__main__':
    pass
 
    # send UDP Socket with command `gettime` to Server to receive the current
    # UTC Timestamp
    cmd = "gettime"
    
    # SOCK_DGRAM is the socket type to use for UDP sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    sock.sendto(cmd, (Config.HOST, Config.PORT))
    received = sock.recv(1024)
    
    print("Sent:     %s" % cmd)
    print("Received: %s" % received)