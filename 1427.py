
N = input()

N = sorted(N)[::-1]

ans = ""

for i in N:
	ans = ans + i

print(ans)
