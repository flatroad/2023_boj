import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())

arr = list(map(int, readline().split()))

add_arr = [0] * (N + 1)
add_arr[0] = 0
add_arr[1] = arr[0]

for i in range(2, N + 1):
    add_arr[i] = add_arr[i - 1] + arr[i - 1]

while (M != 0):
    i, j = map(int, readline().split())
    print(add_arr[j] - add_arr[i - 1])
    M = M - 1