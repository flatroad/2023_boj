def del_one(arr, num):
    if (arr[num] == 0):
        return 0
    add_num = num
    while (1):
        add_num = add_num + num
        if (add_num > 1000000):
            break
        arr[add_num] = 0

max = 1000000

arr = [1 for i in range(max + 1)]

arr[1] = 0
arr[0] = 0

for i in range(max + 1):
    del_one(arr, i)

while(True):
    A = int(input())
    if (A == 0):
        break
    else:
        B = A * 2
        print(arr[A + 1: B + 1].count(1))
