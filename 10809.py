import sys
readline = sys.stdin.readline


arr = [-1 for i in range(26)]
S = readline()

for i in range(S.__len__() - 1):
    if (arr[ord(S[i]) - 97] == -1):
    	arr[ord(S[i]) - 97] = i
    
for i in range(25):
    print(arr[i], end=' ')
print(arr[25])