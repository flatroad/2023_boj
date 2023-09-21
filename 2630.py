import sys
readline = sys.stdin.readline

def divide_square(arr, i, j, l):
	count = 0
	for n in range(i, i + l):
		for m in range(j, j + l):
			count = count + arr[n][m]
	if (count == l * l):
		global blue
		blue = blue + 1
	elif (count == 0):
		global white
		white = white + 1
	else:
		l = int(l / 2)
		for n in range(2):
			for m in range(2):
				divide_square(arr, i + (n * l), j + (m * l), l)

N = int(readline())

arr = []

for i in range(N):
	arr.append(list(map(int, readline().split())))

blue = 0
white = 0

divide_square(arr, 0, 0, N)

print(white)
print(blue)
