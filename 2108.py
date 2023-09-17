from collections import deque
import sys
readline = sys.stdin.readline
N = int(readline())

dq = deque()
dct = dict()

for i in range(N):
    K = int(readline())
    dq.append(K)
    if (K in dct):
        dct[K] = dct[K] + 1
    else:
        dct[K] = 1

dq = sorted(dq)
lst = sorted([k for k, v in dct.items() if max(dct.values()) == v])

print(round(sum(dq) / N))
print(dq[int(N / 2)])
if (len(lst) == 1):
    print(lst[0])
else:
    print(lst[1])
print(dq[N - 1] - dq[0])




