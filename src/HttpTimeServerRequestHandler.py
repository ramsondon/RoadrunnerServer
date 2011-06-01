'''
Created on May 30, 2011

@author: matthias schmid
'''

from SystemClock import SystemClock
import BaseHTTPServer

class HttpTimeServerRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''
    Class Server
    '''
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header('Content-type',    'text/plain')
            self.end_headers()
            self.wfile.write(SystemClock.getUTCTime())

    