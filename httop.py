# coding=utf-8
import subprocess
__author__ = 'mrutid'
import string
import BaseHTTPServer
import unicodedata
import parsers

HOST_NAME = "localhost" #'bandini.hi.inet'
PORT_NUMBER = 8080

def do_command(command):
    output_command = subprocess.check_output(command['path'], shell=True)
    html = command['parse'](output_command)
    return html

#:( I don't like this place
#Config Commands
requestDispatcher = {
    '/ls': {'path': "ls -la $HOME", 'parse': parsers.parse},
    '/top': {'path': "top -l 1", 'parse': parsers.parse_top},
    '/top/basic': {'path': "top -l 1", 'parse': parsers.parse}
}

class HTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        global requestDispatcher
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        #manage request
        path = string.lower(self.path)
        try:
            command = requestDispatcher[path]
        except:
            self.wfile.write("Unsupported Command")
        else:
            if command:
                html = do_command(command)
                html = unicodedata.normalize('NFKD', html).encode('ascii','ignore')
                #html = html.encode('utf-8','ignore')
                self.wfile.write(html)

#Start the Http Server
http_server = server_class = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), HTTPHandler)
try:
    http_server.serve_forever()
except KeyboardInterrupt:
    pass
http_server.server_close()

