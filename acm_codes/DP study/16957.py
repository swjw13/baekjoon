# 체스판 위의 공
# https://www.acmicpc.net/problem/16957

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
dxdy = [(1, 1), (1, 0), (1, -1), (0, 1), (0, 0), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

R, C = list(map(int, input().split()))

parent = [[[i, j] for j in range(C)] for i in range(R)]
board = []

for _ in range(R):
    board.append(list(map(int, input().split())))


def find_parent(row, col):
    mn = sys.maxsize
    mn_row = None
    mn_col = None

    if not (parent[row][col] == [row, col]):
        return parent[row][col]

    for dx, dy in dxdy:
        new_row = row + dx
        new_col = col + dy
        if 0 <= new_row < R and 0 <= new_col < C:
            if board[new_row][new_col] < mn:
                mn = board[new_row][new_col]
                mn_row = new_row
                mn_col = new_col

    if not (mn_row == row and mn_col == col):
        parent[row][col] = find_parent(mn_row, mn_col)
    return parent[row][col]


for i in range(R):
    for j in range(C):
        find_parent(i, j)

ans = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        row, col = parent[i][j]
        ans[row][col] += 1

for i in range(R):
    for j in range(C):
        print(ans[i][j], end=' ')
    print()
