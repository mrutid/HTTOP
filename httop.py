import string

__author__ = 'mrutid'
import BaseHTTPServer
import commands

HOST_NAME = 'bandini.hi.inet'
PORT_NUMBER = 8080

class ParseConsole:
    @staticmethod
    def parse_basic(output_command):
        #first parse: adding </BR>
        return output_command.replace('\n','</BR></BR>')

    @staticmethod
    def matrix_to_html(word_matrix):
        html_str = "<TABLE border='1'>"
        for line in word_matrix:
            html_str +="<TR>"
            for word in line:
                html_str +="<TD>"+word+"</TD>"
            html_str+="</TR>"
        html_str +="</TABLE>"
        return html_str

    @staticmethod
    def parse_to_table(output_command):
        #returns an [][] with the string
        aux_line_split = output_command.split('\n')
        word_matrix = []
        watch_flag = False
        #PURGE TILL HEADER
        for line in aux_line_split:
            aux_word_split = line.split()
            if (watch_flag==True):
                word_matrix.append(aux_word_split);
            if (aux_word_split==[]):
                watch_flag=True
        return ParseConsole.matrix_to_html(word_matrix)

class ExecHandler:
    #Static class to systems calls
    @staticmethod
    def do_top():
        #execTOP
        output_command = commands.getoutput("export TERM=vt100 && top -l 1");
        #return
        return  ParseConsole.parse_to_table(output_command)

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><body>")
        s.wfile.write(ExecHandler.do_top());
        s.wfile.write("</body></head></html>")



http_server = server_class = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
try:
    http_server.serve_forever()
except KeyboardInterrupt:
    pass
http_server.server_close()
