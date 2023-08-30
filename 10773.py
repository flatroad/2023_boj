k = int(input())

arr = []

for i in range(0, k):
    num = int(input())
    if (num == 0 and arr.__len__ != 0):
        arr.pop()
    else:
        arr.append(num)

count = 0
for i in arr:
    count = count + i

print(count)
