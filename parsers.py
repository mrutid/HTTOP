__author__ = 'mru'
from mako.template import Template

#Create Templates
topTemplate = Template(filename="TopTemplate.mako", default_filters=['decode.utf8'])

def parse(output_command):
    #returns a Matrix with the top string
    aux_line_split = output_command.split('\n')
    word_matrix = []
    for line in aux_line_split:
        aux_word_split = line.split()
        word_matrix.append(aux_word_split)
    return topTemplate.render(matrix=word_matrix)

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




