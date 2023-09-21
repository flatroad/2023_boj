import sys
readline = sys.stdin.readline

def divide_arr(arr, i, j, l):
	flag = 0
	count = arr[i][j]
	for n in range(i, i + l):
		for m in range(j, j + l):
			if (count != arr[n][m]):
				flag = 1
				break
	if (flag == 1):
		ln = int(l / 3)
		for n in range(i, i + l, ln):
			for m in range(j, j + l, ln):
				divide_arr(arr, n, m, ln)
	else:
		if (count == 1):
			global plus
			plus = plus + 1
		elif (count == 0):
			global zero
			zero = zero + 1
		elif (count == -1):
			global minus
			minus = minus + 1
		

N = int(readline())

arr = []

for i in range(N):
	arr.append(list(map(int, readline().split())))

minus = 0
plus = 0
zero = 0

divide_arr(arr, 0, 0, N)

print(minus)
print(zero)
print(plus)