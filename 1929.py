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
arr = [i for i in range(max + 1)]

arr[1] = 0

for i in range(max + 1):
    del_one(arr, i)

A, B = map(int, input().split())

for i in range(A, B + 1):
	if (arr[i] != 0):
		print(i)
