M, N = list(map(int, input().split()))

lst = [i for i in range(N + 1)]
lst[1] = 0

for i in range(2, int(N ** 0.5)+1):
    tmp = 2 * i
    if lst[i] != 0:
        while tmp < N + 1:
            lst[tmp] = 0
            tmp += i
lst = [i for i in lst if i != 0 and i >= M]

for i in lst:
    print(i)