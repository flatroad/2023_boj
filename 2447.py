def repeat_star(i, j, N, arr):
	hole_star(int(i - (2 * (N / 3))), int(j - (2 * (N / 3))), int(N / 3), arr)
	if (N > 3):
		for x in range(1, 4):
			for y in range(1, 4):
				repeat_star(int(i - N + ((N / 3) * x)), int(j - N + ((N / 3) * y)), int(N / 3), arr)


def hole_star(i, j, N, arr):
	for x in range(i, i + N):
		for y in range(j, j + N):
			arr[x][y] = ' '

N = int(input())

arr = [['*' for j in range(N)] for i in range(N)]

repeat_star(N, N, N, arr)

for i in range(N):
	for j in range(N):
		print(arr[i][j], end='')
	print()