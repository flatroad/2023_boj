N = int(input())
arr = dict()
dp = dict()

for i in range(N):
	x, y = map(int, input().split())
	if (y in arr):
		if (y == x and (y in dp)):
			dp[y] = dp[y] + 1
		elif (y == x):
			dp[y] = 1
		if ((y == arr[y] or arr[y] < x) and x != y):
			if (arr[y] == y):
				dp[y] = dp[y] + 1
			arr[y] = x
	else:
		arr[y] = x
		if (y == x):
			dp[y] = 0

arr = sorted(arr.items())

i = 0
count = 0
max = -1
end = len(arr)
flag = 0

while (i < end):
	if (max <= arr[i][1]):
		if (arr[i][0] in dp):
			count = count + dp[arr[i][0]]
			del dp[arr[i][0]]
		if (arr[i][1] in dp):
			count = count + dp[arr[i][1]]
			del dp[arr[i][1]]
		count = count + 1
		flag = arr[i][1]
		max = arr[i][0]
	elif (arr[i][0] in dp):
		count = count + dp[arr[i][0]]
	i = i + 1

if (flag != max and (max in dp)):
	count = count + dp[max]

print(count)
