##아직 못품

import sys
readline = sys.stdin.readline

n = int(input())
idx = 0
arr = []
num_list = list(map(int, readline().split()))

for i in range(0, n):
    arr.append([num_list[i]])
    arr[i].append(i + 1)

while (n != 1):
    k = arr[idx][0]
    print(arr[idx][1], end=" ")
    del arr[idx]
    n = n - 1
    idx = idx + k
    if (idx - 1 < n and idx - 1 >= idx - k):
        idx = idx - 1
    elif (n == idx):
        idx = 0
    elif (idx - 1 >= n):
        idx = n % idx
    elif (idx < 0):
        while (idx <= 0):
            idx = n + idx
        if (n == idx):
            idx = 0 
print(arr[0][1])
