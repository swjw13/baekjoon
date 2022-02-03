# 신해빈의 옷입기

T = int(input())

for _ in range(T):
    clothes = dict()
    n = int(input())
    for _ in range(n):
        specific, tpe = input().split()
        if tpe in clothes.keys():
            clothes[tpe] += 1
        else:
            clothes[tpe] = 1
    lst = list(clothes.values())

    total = 1
    for i in lst:
        total *= (i + 1)
    print(total - 1)
