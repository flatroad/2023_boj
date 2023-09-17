import sys
readline = sys.stdin.readline

def del_one(arr, num, dict_arr, count, max):
    if (arr[num] == 0):
        return 0
    add_num = num
    dict_arr[add_num] = 1
    while (1):
        if (count == max):
            print(add_num)
            return (-1)
        add_num = add_num + num
        if (add_num > 1000000):
            break
        arr[add_num] = 0
        count = count + 1
    return (count)

N, M = map(int, input().split())

max = N
arr = [i for i in range(max + 1)]
dict_arr = dict()


for i in range(max + 1):
    if(del_one(arr, i, dict_arr) == -1):
        break