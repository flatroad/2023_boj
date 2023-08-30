import sys
readline = sys.stdin.readline

A, B = readline().split()

A = int(A[::-1])
B = int(B[::-1])

print(max(A, B))