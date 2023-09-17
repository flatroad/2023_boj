import math

N, M = map(int, input().split())

ans1 = math.gcd(N, M)

print(ans1)

ans2 = (N / ans1) * M

print(int(ans2))