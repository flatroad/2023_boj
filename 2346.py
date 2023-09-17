import sys
from collections import deque
readline = sys.stdin.readline

n = int(input())
idx = 0
arr = deque()
num_list = list(map(int, readline().split()))

for i in range(0, n):
    arr.append([num_list[i]])
    arr[i].append(i + 1)

while (len(arr) != 1):
    k, i = arr.popleft()
    print(i, end=" ")
    if (k <= 0):
        arr.rotate(-k)
    else:
        arr.rotate(1 - k)

print(arr[0][1])
arr.clear()