
import sys
readline = sys.stdin.readline

def recursion(s, l, r, count):
    if (l >= r - 1):
        return (1, count)
    elif (s[l] != s[r - 1]):
        return (0, count)
    else:
        count = count + 1
        return (recursion(s, l + 1, r - 1, count))

def isPalindrome(s):
    count = 1
    return recursion(s, 0, len(s) - 1, count)

N = int(readline())

for i in range(0, N):
	A, B = isPalindrome(readline())
	print(A, B)