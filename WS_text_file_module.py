__author__ = 'Amit'

file_path = '/home/ketkee/Documents/WS Data/PlayerCompleteraw/'
file_name = 'Output_Raw_500.txt'
file = file_path + file_name


def write_text_file(input_line):
    if type(input_line) != 'str':
        input_line = str(input_line)+'\n'
    with open(file, 'a') as f:
        f.write(input_line)
    f.closed




