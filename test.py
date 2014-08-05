__author__ = 'ketkee'

with open('/home/ketkee/Documents/WS Data/PlayerData/Team_Player_Output500.txt', 'r') as f:
    line = f.readline()
    line = f.readline()
    print(line)
    dict_ = eval(line)
f.closed

print(dict_.keys())