N = int(input())

dict_arr = dict()
arr = list()

arr = list(map(int, input().split()))

for i in arr:
    if (i not in dict_arr):
        dict_arr[i] = 1

print(len(dict_arr))
