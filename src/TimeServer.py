'''
Created on May 30, 2011

@author: matthias schmid
'''

from SystemClock import SystemClock
import SocketServer

class TimeServer(SocketServer.BaseRequestHandler):
    '''
    Class Server
    '''
    
    def handle(self):
        cmd = self.request[0].strip()
        if cmd == "gettime": 
            socket = self.request[1]
            socket.sendto(str(SystemClock.getUTCTime()),0, self.client_address)
            print("%s from %s" % (cmd, self.client_address[0]))