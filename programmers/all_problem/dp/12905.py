# https://programmers.co.kr/learn/courses/30/lessons/12905
# 가장 큰 정사각형 찾기

def solution(board):
    row = len(board)
    col = len(board[0])

    dp = [[0 for _ in range(col)] for _ in range(row)]
    m = 0

    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                tmp = 1
                if i - 1 >= 0 and j - 1 >= 0:
                    tmp += min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                dp[i][j] = tmp
                m = max(m, tmp)

    return m ** 2
