from controller import controller

import SimpleHTTPServer
import SocketServer
import os

__author__ = 'Nasinyama Bernard'

if __name__ == '__main__':

    # Server
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", 8080), Handler)

        print "serving at port 8080"
        print "Press Ctrl+c twice to exit"
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            os.remove('index.html')
            raise KeyboardInterrupt()
