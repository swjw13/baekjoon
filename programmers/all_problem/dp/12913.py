# https://programmers.co.kr/learn/courses/30/lessons/12913
# 땅따먹기

def solution(land):
    answer = 0

    row = len(land)
    col = len(land[0])

    board = [[0 for _ in range(col)] for _ in range(row)]
    board[0] = land[0]
    for i in range(1, row):
        for j in range(col):
            board[i][j] = max([board[i - 1][k] for k in range(col) if k != j]) + land[i][j]

    
    return max(board[row - 1])

a = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(a))