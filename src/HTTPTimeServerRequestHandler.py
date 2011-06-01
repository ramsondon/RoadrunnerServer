'''
Created on May 30, 2011

@author: matthias schmid
'''

from SystemClock import SystemClock
import BaseHTTPServer

class HTTPTimeServerRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''
    Class HTTPTimeServerRequestHandler
    '''
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type',    'text/plain')
        self.end_headers()
        self.wfile.write(SystemClock.getUTCTime())

    