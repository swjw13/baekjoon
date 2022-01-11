lst = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

N = int(input())
if N == 1:
    print(sum(lst))
else:
    for i in range(1, N):
        tmp = [0 for _ in range(10)]
        tmp[0] = lst[1]
        tmp[9] = lst[8]
        for i in range(1, 9):
            tmp[i] = lst[i - 1] + lst[i + 1]
        lst = tmp.copy()

    print(sum(lst) % 1000000000)