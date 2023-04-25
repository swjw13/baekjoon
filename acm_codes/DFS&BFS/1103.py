# 게임
# https://www.acmicpc.net/problem/1103

import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

dxdy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
res = -1

N, M = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(input().strip()))

visited = [[False for _ in range(M)] for _ in range(N)]
cache = [[-2 for _ in range(M)] for _ in range(N)]


def dfs(cur_row: int, cur_col: int):
    global res
    cur_dist = int(board[cur_row][cur_col])
    res_tmp = -2

    for dx, dy in dxdy:
        new_row = cur_row + dx * cur_dist
        new_col = cur_col + dy * cur_dist

        if 0 <= new_row < N and 0 <= new_col < M:
            if board[new_row][new_col] == "H":
                res_tmp = max(res_tmp, 1)
            elif visited[new_row][new_col]:
                res_tmp = -1
                break
            else:
                if cache[new_row][new_col] == -2:
                    visited[new_row][new_col] = True
                    dfs(new_row, new_col)
                    visited[new_row][new_col] = False
                if cache[new_row][new_col] == -1:
                    res_tmp = -1
                    break
                else:
                    res_tmp = max(res_tmp, cache[new_row][new_col] + 1)

        else:
            res_tmp = max(res_tmp, 1)

    cache[cur_row][cur_col] = res_tmp


visited[0][0] = True
dfs(0, 0)
print(cache[0][0])
