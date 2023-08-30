import sys
readline = sys.stdin.readline

A, B = map(int, readline().split())
C = int(readline())

B = B + C

A = A + (B // 60)
A = A % 24
B = B % 60

print(A, B)
