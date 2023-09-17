import sys
readline = sys.stdin.readline

def del_one(arr, num, dict_arr):
    if (arr[num] == 0):
        return 0
    add_num = num
    dict_arr[add_num] = 1
    while (1):
        add_num = add_num + num
        if (add_num > 2000000):
            break
        arr[add_num] = 0

def check_pe(s, n, m):
     if (n > m):
           print(s)
           return (1)
     else:
          if (s[n] == s[m]):
               return (check_pe(s, n + 1, m - 1))
          else:
               return (0)
    

max = 2000000
arr = [i for i in range(max + 1)]
dict_arr = dict()

arr[1] = 0

for i in range(max + 1):
    del_one(arr, i, dict_arr)

T = int(input())

if (T <= 2):
     print(2)
else:
     if (T % 2 == 0):
           T = T + 1
     for i in range(T, max + 1, 2):
           if (i in dict_arr):
                  if(check_pe(str(i), 0, len(str(i)) - 1) == 1):
                          break
