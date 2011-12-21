__author__ = 'mrutid'
import BaseHTTPServer

HOST_NAME = 'LOCALHOST'
PORT_NUMBER = 8080

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        s.wfile.write("Hello WORLD");

http_server = server_class = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
try:
    http_server.serve_forever()
except KeyboardInterrupt:
    pass
http_server.server_close()
