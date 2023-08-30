import sys
readline = sys.stdin.readline

N = int(readline())
arr = list(map(int, readline().split()))

print(arr.count(int(readline())))
