import sys
readline = sys.stdin.readline

def kanto(N):
    if (N == 1):
        print("-", end="")
        return (0)
    for i in range(0, 3):
        if (i == 0):
            kanto(N / 3)
        elif (i == 1):
            print(" " * int(N / 3), end="")
        else:
            kanto(N / 3)

while True:
    try:
        N = int(readline())
        kanto(3 ** N)
        print("")
    except:
        break
