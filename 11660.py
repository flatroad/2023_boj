import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())

arr_2 = []

for i in range(0, N):
    arr_2.append(list(map(int, readline().split())))

sum_arr = [[0] * (N + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum_arr[i][j] = sum_arr[i][j - 1] + sum_arr[i - 1][j] - sum_arr[i - 1][j - 1] + arr_2[i - 1][j - 1]

for i in range(0, M):
    x1, y1, x2, y2 = map(int, readline().split())
    print(sum_arr[x2][y2] - sum_arr[x2][y1 - 1] - sum_arr[x1 - 1][y2] + sum_arr[x1 - 1][y1 - 1])

