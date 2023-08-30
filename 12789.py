import sys

readline = sys.stdin.readline
stack = []
n = 1

cnt = int(input())
arr = list(map(int, readline().split()))

for i in range(0, cnt):
    while (0 != stack.__len__() and stack[-1] == n):
        stack.pop()
        n = n + 1
    stack.append(arr[i])

while (0 != stack.__len__() and stack[-1] == n):
        stack.pop()
        n = n + 1

if (stack.__len__() != 0):
	print("Sad")
else:
	print("Nice")




