import sys
readline = sys.stdin.readline

total = int(readline())
N = int(readline())
credit = 0

for i in range(0, N):
     M, N = map(int, readline().split())
     credit = credit + (M * N)

if (total == credit):
     print("Yes")
else:
     print("No")