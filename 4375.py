import sys
readline = sys.stdin.readline

while True:
    try:
        N = int(readline())
        num = 1
        while (num % N != 0):
            num = num * 10 + 1
        print(len(str(num)))
    except:
        break
