# coding=utf-8
import subprocess
import string
import BaseHTTPServer
import unicodedata
import parsers
import collections

HOST_NAME = "localhost" #'bandini.hi.inet'
PORT_NUMBER = 8080

#Config Commands for
#USED IN parsers.parse_top(output_command, header_separator=False, include_header=False)
class MyDict(dict):
    def __missing__(self, key):
        return False
#todo TDD LINK

requestDispatcher = MyDict({
    '/ls': MyDict({'path': "ls -la $HOME", 'parse': parsers.parse}),
    '/top': MyDict({'path': "top -l 1", 'parse': parsers.parse, 'header_separator':"" }),
    '/top/basic': MyDict({'path': "ls -la $HOME", 'parse': parsers.parse, 'header_separator':'drwxr-xr-x    2 mru   mru          68 May 17  2010 .Xcode', 'include_header':True})
})

def do_command(command, shell_flag=True):
    output_command = subprocess.check_output(command['path'], shell=shell_flag)
    html = command['parse'](output_command, command['header_separator'],command['include_header'])
    return html

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

