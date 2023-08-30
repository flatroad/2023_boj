import sys
readline = sys.stdin.readline
dict_arr = dict()

str = readline()

str = str.upper()[:-1]

for i in str:
    if (i in dict_arr):
        dict_arr[i] = dict_arr[i] + 1
    else:
        dict_arr[i] = 1
temp = [k for k, v in dict_arr.items() if max(dict_arr.values()) == v]

if (len(temp) > 1):
    print("?")
else:
    print(temp[0])