n, m = map(int, input().split())
s = []

def go(i=0):
    if len(s) == m:
        print(*s)
        return

    for k in range(i, n+1):
          s.append(k)
          go(k)
          s.pop()

go(1)
