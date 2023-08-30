def arr_make (i, N, K, arr):
    i = i + 1
    if(i==K):
        for i in range(1, K-1):
            print(arr[i], end=' ')
        print(arr[K-1])
    else:
        for j in range(1, N+1):
            arr[i]=j
            arr_make(i, N, K, arr)


N, M = map(int, input().split())

arr = [0]*(M+1)

K = len(arr)

arr_make(0, N, K, arr)