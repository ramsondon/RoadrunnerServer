'''
Created on May 30, 2011

@author: matthias
'''

import time

class SystemClock():
    '''
    class SystemClock
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    @staticmethod
    def getUTCTime():
        '''
        Returns the current UTC Timestamp as an integer number
        '''
        return int(time.time())
        
        

    