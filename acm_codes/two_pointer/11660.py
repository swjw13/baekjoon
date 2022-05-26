# https://www.acmicpc.net/problem/11660
# 2차원 구간 합 구하기

import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(1, N):
    board[0][i] += board[0][i - 1]
for i in range(1, N):
    board[i][0] += board[i - 1][0]

for i in range(1, N):
    for j in range(1, N):
        board[i][j] += (board[i][j - 1] + board[i - 1][j] - board[i - 1][j - 1])

for _ in range(M):
    r1, c1, r2, c2 = list(map(int, input().split()))
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1

    if r1 == 0 and c1 == 0:
        print(board[r2][c2])
    elif r1 == 0:
        print(board[r2][c2] - board[r2][c1 - 1])
    elif c1 == 0:
        print(board[r2][c2] - board[r1 - 1][c2])
    else:
        print(board[r2][c2] - board[r2][c1 - 1] - board[r1 - 1][c2] + board[r1 - 1][c1 - 1])
