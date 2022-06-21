# https://programmers.co.kr/learn/courses/30/lessons/42898
# 등굣길

from collections import deque


def solution(m, n, puddles):
    board = [[0 for _ in range(m)] for _ in range(n)]
    for j, i in puddles:
        board[i - 1][j - 1] = -1
    board[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i + j > 0 and board[i][j] != -1:
                tmp = 0
                if i - 1 >= 0 and board[i - 1][j] != -1:
                    tmp += board[i - 1][j]
                if j - 1 >= 0 and board[i][j - 1] != -1:
                    tmp += board[i][j - 1]
                board[i][j] = tmp

    return board[n - 1][m - 1]


a = 4
b = 3
c = [[2, 2]]
print(solution(a, b, c))
