import math

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

up_num = (A1 * B2) + (A2 * B1)
down_num = B1 * B2

gcd_num = math.gcd(up_num, down_num)

print(int(up_num / gcd_num), int(down_num / gcd_num))