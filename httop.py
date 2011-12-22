__author__ = 'mrutid'
import BaseHTTPServer
import commands
from mako.template import Template

HOST_NAME = 'bandini.hi.inet'
PORT_NUMBER = 8080

class ParseConsole:
    @staticmethod
    def parse_to_table(output_command):
        #returns a Matrix with the string
        aux_line_split = output_command.split('\n')
        word_matrix = []
        watch_flag = False
        #PURGE TILL HEADER (empty ROW [])
        for line in aux_line_split:
            aux_word_split = line.split()
            if watch_flag:
                word_matrix.append(aux_word_split)
            if not aux_word_split:
                watch_flag=True
        return topTemplate.render(matrix=word_matrix)
        #return ParseConsole.matrix_to_html(word_matrix)

class ExecHandler:
    #Static class to systems calls
    @staticmethod
    def do_top():
        #execTOP
        output_command = commands.getoutput("export TERM=vt100 && top -l 1")
        #return
        return  ParseConsole.parse_to_table(output_command)

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(response):
        response.send_response(200)
        response.send_header("Content-type", "text/html")
        response.end_headers()
        response.wfile.write(ExecHandler.do_top())


#create templates
#TOP template (I suppouse I only need this once)
topTemplate = Template(filename="TopTemplate.mako")
#Other templates Just in case...

http_server = server_class = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
try:
    http_server.serve_forever()
except KeyboardInterrupt:
    pass
http_server.server_close()
