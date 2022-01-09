from itertools import combinations

N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))

most = 0

for i in combinations(lst, 3):
    total = sum(i)
    if total <= M and M - total <= M - most:
        most = total

print(most)
