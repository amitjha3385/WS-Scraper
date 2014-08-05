__author__ = 'Amit'

file_path = '/home/ketkee/Documents/WS Data/TeamData/'
file_name = 'WS_Output500.txt'
file = file_path + file_name

# noinspection PyUnresolvedReferences
from WS_DataClean import player_data


# Read the file one line at a time
# Since the files have data for the teams it will return one team at a time as a string
with open(file, 'r') as f:
    for line in f:
        player_data(line)
f.closed










