import sys
readline = sys.stdin.readline
count = 0
num = 0

def find_n(n):
	if (n[0] == 'A'):
		return (4.0 + find_n2(n))
	elif (n[0] == 'B'):
		return (3.0 + find_n2(n))
	elif (n[0] == 'C'):
		return (2.0 + find_n2(n))
	elif (n[0] == 'D'):
		return (1.0 + find_n2(n))
	else:
		return (0.0)

def find_n2(n):
	if (n[1] == '+'):
		return (0.5)
	else:
		return (0.0)

while(True):
	try:
			noneed, j, n = map(str, readline().split())
			if (n == 'P'):
				continue
			num = num + (float(j) * find_n(n))
			count = count + float(j)
	except:
		break
print(round(num / count, 6))