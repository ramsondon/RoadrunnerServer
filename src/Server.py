'''
Created on May 30, 2011

@author: matthias schmid
'''

from SystemClock import SystemClock

class Server():
    '''
    Class Server
    '''

    def __init__(self, ip, port):
        '''
        Constructor
        '''
        self.ip = ip
        self.port = port
        
    def run(self):
        '''
        Starts the server process
        '''
        print(SystemClock.getUTCTime())