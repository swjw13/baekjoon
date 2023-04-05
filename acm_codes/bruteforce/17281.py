# https://www.acmicpc.net/problem/17281
# 야구

import sys
from itertools import permutations

input = sys.stdin.readline


def change_batter_idx(num):
    return (num + 1) % 9


res = 0

n = int(input())
batter_hits = []
for _ in range(n):
    batter_hits.append(list(map(int, input().split())))

for i in permutations([1, 2, 3, 4, 5, 6, 7, 8]):
    tmp = 0
    cur_batter_idx = 0
    new_list = [element for element in i[:3]] + [0] + [element for element in i[3:]]
    for batter_cur_inning in batter_hits:
        outs = 0
        b1, b2, b3 = 0, 0, 0
        while outs < 3:

            cur_action = batter_cur_inning[new_list[cur_batter_idx]]
            if cur_action == 0:
                outs += 1
            elif cur_action == 1:
                tmp += b3
                b1, b2, b3 = 1, b1, b2
            elif cur_action == 2:
                tmp += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif cur_action == 3:
                tmp += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            else:
                tmp += (b1 + b2 + b3) + 1
                b1, b2, b3 = 0, 0, 0

            cur_batter_idx = change_batter_idx(cur_batter_idx)

    res = max(res, tmp)

print(res)
