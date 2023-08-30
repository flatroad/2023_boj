import sys
readline = sys.stdin.readline

full = [1, 1, 2, 2, 2, 8]

arr = list(map(int, readline().split()))

for i in range(5):
    print(full[i] - arr[i], end=' ')
print(full[5] - arr[5])