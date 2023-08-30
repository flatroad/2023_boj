import sys
readline = sys.stdin.readline

def chr_time(c):
    num = ord(c) - 65
    if (num < 3):
        return (3)
    elif (num < 6):
        return (4)
    elif (num < 9):
        return (5)
    elif (num < 12):
        return (6)
    elif (num < 15):
        return (7)
    elif (num < 19):
        return (8)
    elif (num < 22):
        return (9)
    else:
        return (10)

str = readline()

time = 0
for i in range(len(str) - 1):
    time = time + chr_time(str[i])
    
print(time)