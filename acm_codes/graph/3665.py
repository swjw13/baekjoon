# https://www.acmicpc.net/problem/3665
# 최종 순위

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    lst = list(map(int, input().split()))

    come_in = {i: set() for i in range(1, n + 1)}
    last_year_final = dict()
    for i in range(1, n + 1):
        last_year_final[i] = lst[i - 1]

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            come_in[last_year_final[j]].add(last_year_final[i])

    m = int(input())

    for _ in range(m):
        new_winner, new_loser = list(map(int, input().split()))

        if new_loser in come_in[new_winner]:
            come_in[new_winner].remove(new_loser)
            come_in[new_loser].add(new_winner)
        else:
            come_in[new_loser].remove(new_winner)
            come_in[new_winner].add(new_loser)

    ans = []
    check = ""
    for k in range(1, n + 1):
        tmp = set()
        for i in come_in.keys():
            if len(come_in[i]) == 0:
                tmp.add(i)
        if len(tmp) == 0:
            check = "IMPOSSIBLE"
            break
        elif len(tmp) > 1:
            check = "?"
            break
        else:
            tmp = list(tmp)
            ans.append(tmp[0])
            come_in.pop(tmp[0])
            for i in come_in.keys():
                if tmp[0] in come_in[i]:
                    come_in[i].remove(tmp[0])

    if check != "":
        print(check)
    else:
        for i in ans:
            print(i, end=' ')
        print()
