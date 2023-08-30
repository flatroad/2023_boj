T = int(input())

answer = 0

for i in range(T):
    C = input()
    arr = dict()
    k = '1'
    for i in C:
        if (k == i):
            continue
        k = i
        if (i in arr):
            arr[i] = 0
        else:
            arr[i] = 1
    if (0 in arr.values()):
        del arr
        continue
    del arr
    answer = answer + 1

print(answer)
