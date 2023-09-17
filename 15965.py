def del_one(arr, num, dict_arr, k):
    if (arr[num] == 0):
        return k
    add_num = num
    dict_arr[k] = num
    while (1):
        add_num = add_num + num
        if (add_num > 10000000):
            break
        arr[add_num] = 0
    return (k + 1)

max = 10000000
arr = [i for i in range(max + 1)]
dict_arr = dict()

arr[1] = 0
k = 1

for i in range(max + 1):
    k = del_one(arr, i, dict_arr, k)


print(len(dict_arr))
