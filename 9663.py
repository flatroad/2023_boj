def check_down_left(arr, i, j):
    if (i == 0 or j == 0):
        if (arr[i][j] == 0):
            return (1)
        else:
            return (0)
    if (arr[i][j] == 0):
        return (check_down_left(arr, i - 1, j - 1))
    else:
        return (0)

def check_down_right(arr, i, j, N):
    if (i == 0 or j == N - 1):
        if (arr[i][j] == 0):
            return (1)
        else:
            return (0)
    if (arr[i][j] == 0):
        return (check_down_right(arr, i - 1, j + 1, N))
    else:
        return (0)

def check_down_l(arr, i, j):
    if (i == 0):
        if (arr[i][j] == 0):
            return (1)
        else:
            return (0)
    if (arr[i][j] == 0):
        return (check_down_l(arr, i - 1, j))
    else:
        return (0)

def checker(arr, i, j, N):
    if (check_down_l(arr, i, j) == 0):
        return (0)
    if (check_down_left(arr, i, j) == 0):
        return (0)
    if (check_down_right(arr, i, j, N) == 0):
        return (0)
    arr[i][j] = 1
    return (1)

def n_qun(arr, N, i):
    global count
    if (i == N):
        count = count + 1
        return (0)
    for j in range(N):
        if (checker(arr, i, j, N) == 0):
            continue
        else:
            n_qun(arr, N, i + 1)
            arr[i][j] = 0
    return (0)

N = int(input())

arr = [[0] * (N) for i in range(N)]

global count

count = 0

n_qun(arr, N, 0)

print(count)