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

T = int(input())

for i in range(T):
    N = int(input())
    answer = 0
    max = N / 2
    for i in dict_arr:
        if (max < i):
            break
        if (N - i in dict_arr):
            answer = answer + 1
    print(answer)
