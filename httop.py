# coding=utf-8
import subprocess

__author__ = 'mrutid'
import string
import BaseHTTPServer
from mako.template import Template

HOST_NAME = "localhost" #'bandini.hi.inet'
PORT_NUMBER = 8080
class Command:
    @staticmethod
    def do_command(command):
        output_command = subprocess.check_output(command['path'], shell=True)
        html = command['parse'](output_command)
        return html


class ParseConsole:
    @staticmethod
    def parse(output_command):
    #returns a Matrix with the top string
        aux_line_split = output_command.split('\n')
        word_matrix = []
        for line in aux_line_split:
            aux_word_split = line.split()
            word_matrix.append(aux_word_split)
        return topTemplate.render(matrix=word_matrix)

    @staticmethod
    def parse_top(output_command):
        #returns a Matrix with the top string
        aux_line_split = output_command.split('\n')
        word_matrix = []
        watch_flag = False
        #PURGE TILL HEADER (empty ROW [])
        for line in aux_line_split:
            aux_word_split = line.split()
            if watch_flag:
                word_matrix.append(aux_word_split)
            if not aux_word_split:
                watch_flag = True
        return topTemplate.render(matrix=word_matrix)


#:( I don't like this place
#Config Commands
requestDispatcher = {
    '/ls': {'path': "ls -la /usr", 'parse': ParseConsole.parse},
    '/top': {'path': "top -l 1", 'parse': ParseConsole.parse_top}
}

class HTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        global requestDispatcher
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        #manage request
        command = requestDispatcher[string.lower(self.path)]
        if command:
            html = Command.do_command(command)
            self.wfile.write(html)
        else:
            self.wfile.write("Unsupported Command")


#Create Templates
topTemplate = Template(filename="TopTemplate.mako")

#Start the Http Server
http_server = server_class = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), HTTPHandler)
try:
    http_server.serve_forever()
except KeyboardInterrupt:
    pass
http_server.server_close()

