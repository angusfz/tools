#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json

PORT_NUMBER = 80
DATA = { }

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

        #Handler for the GET requests
        def do_GET(self):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                # Send the html message
                self.wfile.write("Hello World !")
                return
        def do_POST(self):
                request_payload=self.rfile.read(int(self.headers.getheader('Content-Length'))) + str(self.headers)
                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.end_headers()
                # Send the html message
                DATA['response_type']='in_channel'
                DATA['text']=request_payload
                self.wfile.write(json.dumps(DATA))
                print request_payload
                print type(request_payload)
                return

try:
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print 'Started httpserver on port ' , PORT_NUMBER

        #Wait forever for incoming htto requests
        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
