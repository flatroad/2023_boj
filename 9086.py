import sys
readline = sys.stdin.readline

N = int(readline())

for i in range(N):
	S = readline()
	str = S[0] + S[-2]
	print(str)