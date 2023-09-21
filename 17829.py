import sys
readline = sys.stdin.readline

def polling(arr, l):
	arr_re = []
	for i in range(0, l, 2):
		arr_part = []
		for j in range(0, l, 2):
			arr_part.append(sorted([arr[i][j], arr[i][j + 1], arr[i + 1][j], arr[i + 1][j + 1]])[2])
		arr_re.append(arr_part)
	if (l == 2):
		print(arr_re[0][0])
	else:
		polling(arr_re, int(l / 2))

N = int(readline())
arr = []

for i in range(N):
	arr.append(list(map(int, readline().split())))

polling(arr, N)