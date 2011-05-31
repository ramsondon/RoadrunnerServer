'''
Created on May 30, 2011

@author: matthias schmid
'''

from SystemClock import SystemClock
import SocketServer

class TCPTimeServerRequestHandler(SocketServer.BaseRequestHandler):
    '''
    Class Server
    '''
    
    def handle(self):
        self.request.send(str(SystemClock.getUTCTime()))
        print("request from %s" % (self.client_address[0]))