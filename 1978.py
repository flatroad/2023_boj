def del_one(arr, num, dict_arr):
    if (arr[num] == 0):
        return 0
    add_num = num
    dict_arr[add_num] = num
    while (1):
        add_num = add_num + num
        if (add_num > 1000000):
            break
        arr[add_num] = 0
    return (k + 1)

max = 1000000
arr = [i for i in range(max + 1)]
dict_arr = dict()

arr[1] = 0

for i in range(max + 1):
    k = del_one(arr, i, dict_arr)
    
N = int(input())

lst = list(map(int, input().split()))

count = 0

for i in lst:
    if (i in dict_arr):
        count = count + 1

print(count)