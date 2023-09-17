import math

N, M = map(int, input().split())

i = math.gcd(N, M)

for j in range(i):
	print(1, end='')
print()