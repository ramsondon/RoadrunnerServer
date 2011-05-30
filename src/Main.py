'''
Created on May 30, 2011

@author: matthias
'''

from Server import Server
from Config import Config

if __name__ == '__main__':
    pass

    server = Server(Config.IP, Config.PORT)
    server.run()