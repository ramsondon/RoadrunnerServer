'''
Created on May 30, 2011

@author: matthias
'''

import socket
from Interpreter import Interpreter

if __name__ == '__main__':
    pass
    
    interpreter = Interpreter()
   
    
    # SOCK_DGRAM is the socket type to use for UDP sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    sock.sendto("dummy",0,(interpreter.getHost(),interpreter.getPort()))
    received = sock.recv(1024)
    
    print("Received: %s" % received)