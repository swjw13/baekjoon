N, M = list(map(int, input().split()))


def back(N, M, lst):
    if len(lst) == M:
        for i in lst:
            print(i, end=' ')
        print()
    else:
        for i in range(1, N + 1):
            if (len(lst) == 0) or (lst[-1] <= i):
                back(N, M, lst + [i])


back(N, M, [])
