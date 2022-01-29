import sys

input = sys.stdin.readline

N = int(input())

lst = [0 for i in range(N + 1)]
track = [[] for _ in range(N + 1)]
if N == 1:
    track[1] = [1]
elif N == 2:
    lst[2] = 1
    track[2] = [2, 1]
else:
    lst[2] = 1
    track[2] = [2, 1]
    lst[3] = 1
    track[3] = [3, 1]

    for i in range(4, N + 1):
        tmp = lst[i - 1]
        term = i - 1
        if i % 2 == 0 and tmp > lst[i // 2]:
            tmp = lst[i // 2]
            term = i // 2
        if i % 3 == 0 and tmp > lst[i // 3]:
            tmp = lst[i // 3]
            term = i // 3

        lst[i] = tmp + 1
        track[i] = [i] + track[term]

print(lst[N])
for i in track[N]:
    print(i, end=' ')
