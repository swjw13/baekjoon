# 시간....해결이 필요하다....

import sys

input = sys.stdin.readline

dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

R, C = list(map(int, input().split()))
board = []
for _ in range(R):
    board.append(list(input())[:-1])

visited = [False for _ in range(26)]

count = 0


def word_to_num(word):
    return ord(word) - ord("A")


def dfs(row, col, turn):
    global count
    count = max(count, turn)
    visited[word_to_num(board[row][col])] = True
    for (dx, dy) in dydx:
        x = row + dx
        y = col + dy
        if 0 <= x < R and 0 <= y < C and not visited[word_to_num(board[x][y])]:
            dfs(x, y, turn + 1)
            visited[word_to_num(board[x][y])] = False


dfs(0, 0, 1)

print(count)
