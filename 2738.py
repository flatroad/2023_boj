import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())

arr = [[] for i in range(N * 2)]

for i in range(N * 2):
    arr[i] = list(map(int, readline().split()))

max = N

for i in range(max):
    for j in range(M):
            print(arr[i][j] + arr[i + N][j], end=' ')
    print()
