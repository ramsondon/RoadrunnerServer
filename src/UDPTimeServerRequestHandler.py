'''
Created on May 30, 2011

@author: matthias schmid
'''

from SystemClock import SystemClock
import SocketServer

class UDPTimeServerRequestHandler(SocketServer.BaseRequestHandler):
    '''
    Class Server
    '''
    
    def handle(self):
        self.request[1].sendto(str(SystemClock.getUTCTime()),0, self.client_address)
        print("request from %s" % (self.client_address[0]))