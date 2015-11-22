__all__ = ["SimpleHTTPRequestHandler"]

import os
import posixpath
import BaseHTTPServer
import urllib
import cgi
import sys
import shutil
import mimetypes
import re

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    server_version = "SimpleHTTP/0.1" 

    def do_GET(self):
        self.send_head()

    def send_head(self):
	print self.path
	f = open('action.txt', 'w')
	f.write(re.sub('/', '', self.path))
	f.close()
        self.send_response(200)
        self.send_header("Content-type", "application/javascript")
        self.send_header("Content-Length", 0)
        self.end_headers()

def test(HandlerClass = SimpleHTTPRequestHandler,
         ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()
