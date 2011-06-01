'''
Created on May 30, 2011

@author: matthias
'''

import sys

class Interpreter():
    '''
    Class Config
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.handleArguments(sys.argv)
        
        
    def handleArguments(self, argv):
        '''
        Handles the Arguments passed form Console
        '''
        if (argv[1] != "--ip" or argv[3] != "--port" or argv[5] != "--protocol") :
            print("Call with: --ip <ip> --port <port> --protocol <protocol>")
            print("<ip>: host ip address")
            print("<port>: host port number")
            print("<protocol>: tcp, udp, http")
            sys.exit()
        
        self.host = "".join(sys.argv[2])
        self.port = int(sys.argv[4])
        self.protocol = "".join(sys.argv[6])
        
            
    def getHost(self):
        '''
        Returns the Argument Host Address
        '''
        return self.host
    
    def getPort(self):
        '''
        Returns the Argument Host Port
        '''
        return self.port
    
    def getProtocol(self):
        '''
        Returns the specified Protocol
        Valid: udp, tcp
        '''
        return self.protocol
    
    def isUdp(self):
        '''
        Determines if the configured Protocol is UDP
        '''
        if self.protocol == "udp":
            return True
        else:
            return False


    def isTcp(self):
        '''
        Determines if the configured Protocol is TCP
        '''
        if self.protocol == "tcp":
            return True
        else:
            return False
    
    def isHttp(self):
        '''
        Determines if the configured Protocol is HTTP
        '''
        if self.protocol == "http":
            return True
        else:
            return False