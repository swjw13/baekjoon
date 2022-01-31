from itertools import combinations

moeum = ['a', 'e', 'i', 'o', 'u']

L, C = list(map(int, input().split()))
lst = input().split()
lst.sort()

for i in combinations(lst, L):
    tmp = "".join(i)
    check = 0
    for letters in moeum:
        check += tmp.count(letters)
    if 1 <= check <= L - 2:
        print(tmp)
