__author__ = 'mru'
from mako.template import Template

#Create Templates
topTemplate = Template(filename="TopTemplate.mako", default_filters=['decode.utf8'])

def parse(output_command, header_separator, include_header=False):
    word_matrix = []
    watch_flag = not header_separator
    aux_line_split = output_command.split('\n')
    for line in aux_line_split:
        aux_word_split = line.split()
        if watch_flag:
            word_matrix.append(aux_word_split)

        if  (header_separator is not None) & (line == header_separator):
            watch_flag = True
            if include_header:
                word_matrix.append(aux_word_split)
    return topTemplate.render(matrix=word_matrix)


