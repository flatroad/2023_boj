import sys
readline = sys.stdin.readline

A, B, C = map(int, readline().split())

if (A != B and C != A and B != C):
    print(max(A, B, C) * 100)
elif (A == B == C):
    print(10000 + (A * 1000))
else:
    if (A == B):
        print(1000 + (A * 100))
    elif (C == A):
        print(1000 + (C * 100))
    else:
        print(1000 + (B * 100))
