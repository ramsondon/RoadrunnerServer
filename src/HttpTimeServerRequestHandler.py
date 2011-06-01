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
            self.send_header('Content-type',    'text/html')
            self.end_headers()
            self.wfile.write(str(SystemClock.getUTCTime()))
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
    