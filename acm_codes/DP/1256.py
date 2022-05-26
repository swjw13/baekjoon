# https://www.acmicpc.net/problem/1256
# 사전

import sys
import math

input = sys.stdin.readline

N, M, K = list(map(int, input().split()))

board = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, M + 1):
    board[0][i] = 1
for i in range(1, N + 1):
    board[i][0] = 1

for row in range(1, N + 1):
    for col in range(1, M + 1):
        board[row][col] = board[row - 1][col] + board[row][col - 1]


def dictionary(row, col, remain_count):
    if row == 0 and col == 0:
        return ""
    elif row == 0:
        return "z" * col
    elif col == 0:
        return "a" * row
    else:
        if remain_count <= board[row - 1][col]:
            return "a" + dictionary(row - 1, col, remain_count)
        else:
            return "z" + dictionary(row, col - 1, remain_count - board[row - 1][col])


if K > math.comb(N + M, N):
    print(-1)
else:
    print(dictionary(N, M, K))
