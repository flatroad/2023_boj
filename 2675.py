import sys
readline = sys.stdin.readline

N = int(readline())
for i in range(N):
    A, S = readline().split()
    A = int(A)
    for i in S:
        print(i * A, end="")
    print()