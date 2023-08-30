import sys
readline = sys.stdin.readline

K, N = map(int, readline().split())

arr = [0] * K
sum_arr = [0] * (K - N + 1)

arr = list(map(int, readline().split()))

sum_arr[0] = sum(arr[0 : N])

for i in range(1, K - N + 1):
    sum_arr[i] = sum_arr[i - 1] - arr[i - 1] + arr[i + N - 1]

sum_arr.sort()
print(sum_arr[-1])