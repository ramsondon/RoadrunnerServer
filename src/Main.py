'''
Created on May 30, 2011

@author: matthias
'''

from TimeServer import TimeServer
from Config import Config
import SocketServer

if __name__ == '__main__':
    pass
    print("Main Application Server Started on %s at port %s" % (Config.HOST, Config.PORT))
    
    # Start Server Process   
    s = SocketServer.UDPServer((Config.HOST, Config.PORT),TimeServer).serve_forever()