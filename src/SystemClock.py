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
        Returns the current UTC Timestamp as a floating point number
        '''
        return time.time()
        
        

    