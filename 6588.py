import sys
readline = sys.stdin.readline

max = 1000000
arr = [1 for i in range(max + 1)]

for i in range(3, max + 1, 2):
    if (arr[i] == 0):
        continue
    add_num = i
    while (1):
        add_num = add_num + i
        if (add_num > 1000000):
            break
        arr[add_num] = 0

while(1):
    n = int(readline())
    if (n % 2 == 1):
        print("Goldbach's conjecture is wrong.")
        continue
    k = int(n / 2)
    if (n == 0):
        break
    for i in range(3, k + 1, 2):
        if (arr[i] == 1):
            if (arr[n - i] == 1):
                print(n, "=", i, "+",  n - i)
                n = 0
                break
    if (n != 0):
        print("Goldbach's conjecture is wrong.")