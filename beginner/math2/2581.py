M = int(input())
N = int(input())

lst = [i for i in range(N + 1)]
lst[1] = 0

for i in range(2, int(N ** 0.5)+1):
    tmp = 2 * i
    if lst[i] != 0:
        while tmp < N + 1:
            lst[tmp] = 0
            tmp += i

min = 1e9
min_idx = 0
total = 0

for i in range(M, N + 1):
    total += lst[i]
    if lst[i] < min and lst[i] != 0:
        min = lst[i]
        min_idx = i

if min_idx == 0:
    print(-1)
else:
    print(total)
    print(min_idx)
