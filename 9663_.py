def n_qun(arr, N, i):
    if (i == N):
        global count
        count = count + 1
        return (0)
    for j in range(N):
        n = 1
        for idx in range(i):
            if (j - i + idx >= 0 and arr[idx][j - i + idx] != 0):
                n = 0
                break
            if (j + i - idx < N and arr[idx][j + i - idx] != 0):
                n = 0
                break
            if (arr[idx][j] != 0):
                n = 0
                break
        if (n == 0):
            continue
        arr[i][j] = 1
        n_qun(arr, N, i + 1)
        arr[i][j] = 0
    return (0)

N = int(input())

arr = [[0] * (N) for i in range(N)]

global count

count = 0

n_qun(arr, N, 0)

print(count)