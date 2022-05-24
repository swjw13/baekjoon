from itertools import combinations

N = int(input())
lst = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    lst.append([x, y, 1])

for i in combinations(lst, 2):
    one = i[0]
    two = i[1]
    if one[0] > two[0] and one[1] > two[1]:
        two[2] += 1
    if one[0] < two[0] and one[1] < two[1]:
        one[2] += 1

for i in lst:
    print(i[2], end=' ')
