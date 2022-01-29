import itertools

N, M = list(map(int, input().split()))
lst = [i for i in range(1, N + 1)]

for i in itertools.permutations(lst, M):
    for j in i:
        print(j, end=' ')
    print()
