# 색종이 4분할

import sys

board = []
N = int(sys.stdin.readline())
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)


def check(row_start, row_end, col_start, col_end):
    tmp = board[row_start][col_start]
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if board[i][j] != tmp:
                return False, -1
    return True, tmp


to_compute = [(0, N, 0, N)]
total = [0, 0]
while to_compute:
    (rs, re, cs, ce) = to_compute.pop()
    (after, value) = check(rs, re, cs, ce)
    if after:
        total[value] += 1
    else:
        to_compute.append((rs, (rs + re) // 2, cs, (cs + ce) // 2))
        to_compute.append((rs, (rs + re) // 2, (cs + ce) // 2, ce))
        to_compute.append(((rs + re) // 2, re, cs, (cs + ce) // 2))
        to_compute.append(((rs + re) // 2, re, (cs + ce) // 2, ce))

print(total[0])
print(total[1])
