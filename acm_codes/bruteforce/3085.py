# 봄보니 사탕 게임
# https://www.acmicpc.net/problem/3085

import sys

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(input())[:-1])


def find_longest_line(row_start=0, row_end=N, col_start=0, col_end=N):
    checkboard = [[[1, 1] for _ in range(N)] for _ in range(N)]
    max_length = 0

    for i in range(row_start, row_end):
        for j in range(N):
            if i != 0:
                if board[i][j] == board[i - 1][j]:
                    checkboard[i][j][1] = checkboard[i - 1][j][1] + 1
            if j != 0:
                if board[i][j] == board[i][j - 1]:
                    checkboard[i][j][0] = checkboard[i][j - 1][0] + 1
            max_length = max(max_length, max(checkboard[i][j]))
    for i in range(N):
        for j in range(col_start, col_end):
            if i != 0:
                if board[i][j] == board[i - 1][j]:
                    checkboard[i][j][1] = checkboard[i - 1][j][1] + 1
            if j != 0:
                if board[i][j] == board[i][j - 1]:
                    checkboard[i][j][0] = checkboard[i][j - 1][0] + 1
            max_length = max(max_length, max(checkboard[i][j]))

    return max_length


ans = find_longest_line()

for i in range(N):
    for j in range(N):
        # 아래 값이랑 교환
        if i != N - 1 and board[i][j] != board[i + 1][j]:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            ans = max(ans, find_longest_line(i, i + 2, j, j + 1))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

        # 오른 쪽 값이랑 교환
        if j != N - 1 and board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            ans = max(ans, find_longest_line(i, i + 1, j, j + 2))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

print(ans)
