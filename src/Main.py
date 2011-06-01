'''
Created on May 30, 2011

@author: matthias
'''


from UDPTimeServerRequestHandler import UDPTimeServerRequestHandler
from TCPTimeServerRequestHandler import TCPTimeServerRequestHandler
from HTTPTimeServerRequestHandler import HTTPTimeServerRequestHandler
from Interpreter import Interpreter
import SocketServer

if __name__ == '__main__':
    pass
    
    interpreter = Interpreter()
    print("Main %s Application Server Started on %s at port %s" % (
        interpreter.getProtocol(), interpreter.getHost(), interpreter.getPort()))
    
    # Start Server Process   
    if interpreter.isUdp() == True:
        SocketServer.UDPServer((interpreter.getHost(), 
            interpreter.getPort()),UDPTimeServerRequestHandler).serve_forever()
    elif interpreter.isHttp() == True:
        SocketServer.TCPServer((interpreter.getHost(), 
            interpreter.getPort()),HTTPTimeServerRequestHandler).serve_forever()
    elif interpreter.isTcp() == True:
        SocketServer.TCPServer((interpreter.getHost(), 
            interpreter.getPort()),TCPTimeServerRequestHandler).serve_forever()