def factorial(a):
    if (a != 0):
        return (a * factorial(a - 1))
    return (1)

N = int(input())

print(factorial(N))
