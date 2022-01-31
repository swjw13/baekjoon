# 종이의 갯수
# 쿼드 트리

import sys
from collections import deque

sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
pic = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    pic.append(line)


def check(row_start, row_end, col_start, col_end):
    value = pic[row_start][col_start]
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if pic[i][j] != value:
                return False, "-2"
    return True, value


count = [0, 0, 0]
to_compute = deque([(0, N, 0, N)])
while to_compute:
    (rs, re, cs, ce) = to_compute.popleft()
    (after, value) = check(rs, re, cs, ce)
    if after:
        count[value + 1] += 1
    else:
        row_diff = re - rs
        col_diff = ce - cs
        for i in range(3):
            for j in range(3):
                r_s = rs + row_diff // 3 * i
                r_e = rs + row_diff // 3 * (i + 1)
                c_s = cs + col_diff // 3 * j
                c_e = cs + col_diff // 3 * (j + 1)
                to_compute.append((r_s, r_e, c_s, c_e))

for i in count:
    print(i)
