import sys
readline = sys.stdin.readline

def del_one(arr, num, dict_arr):
    if (arr[num] == 0):
        return 0
    add_num = num
    dict_arr[add_num] = 1
    while (1):
        add_num = add_num + num
        if (add_num > 1000000):
            break
        arr[add_num] = 0

max = 1000000
arr = [i for i in range(max + 1)]
dict_arr = dict()

arr[1] = 0

for i in range(max + 1):
    del_one(arr, i, dict_arr)

T = int(readline())

for i in range(T):
    n = int(readline())
    k = int(n / 2)
    for i in range(k):
        if (k - i in dict_arr):
            if (k + i in dict_arr):
                print(k - i, k + i)
                break