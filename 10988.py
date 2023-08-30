import sys
readline = sys.stdin.readline

def repeat_str(str, i, j):
    if (i >= j):
            return (1)
    if (str[i] == str[j]):
          return(repeat_str(str, i + 1, j - 1))
    else:
          return (0)

str = readline()

print(repeat_str(str, 0, str.__len__() - 2))
