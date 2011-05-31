'''
Created on May 30, 2011

@author: matthias
'''


from UDPTimeServerRequestHandler import UDPTimeServerRequestHandler
from TCPTimeServerRequestHandler import TCPTimeServerRequestHandler

from Interpreter import Interpreter
import SocketServer

if __name__ == '__main__':
    pass
    
    interpreter = Interpreter()
    print("Main %s Application Server Started on %s at port %s" % (
        interpreter.getProtocol(), interpreter.getHost(), interpreter.getPort()))
    
    # Start Server Process   
    if interpreter.isUdp() == True:
        s = SocketServer.UDPServer((interpreter.getHost(), 
            interpreter.getPort()),UDPTimeServerRequestHandler).serve_forever()
    else :
        s = SocketServer.TCPServer((interpreter.getHost(), 
            interpreter.getPort()),TCPTimeServerRequestHandler).serve_forever()
