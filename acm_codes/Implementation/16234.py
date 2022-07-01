# https://www.acmicpc.net/problem/16234
# 인구 이동

import sys
from collections import deque

input = sys.stdin.readline
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, L, R = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

ans = 0

while True:
    cnt = 1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    total_population = dict()
    total_count = dict()

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = cnt
                queue = deque([(i, j)])
                total_population[cnt] = board[i][j]
                total_count[cnt] = 1

                while queue:
                    cur_row, cur_col = queue.popleft()
                    cur_population = board[cur_row][cur_col]

                    for dx, dy in dxdy:
                        new_row = cur_row + dx
                        new_col = cur_col + dy
                        if 0 <= new_row < N and 0 <= new_col < N and visited[new_row][new_col] == 0:
                            dist = abs(board[new_row][new_col] - cur_population)
                            if L <= dist <= R:
                                total_population[cnt] += board[new_row][new_col]
                                total_count[cnt] += 1
                                visited[new_row][new_col] = cnt
                                queue.append((new_row, new_col))

                cnt += 1
    if cnt == N * N + 1:
        sys.stdout.write("%d" % ans)
        break
    else:
        ans += 1
        for i in range(N):
            for j in range(N):
                group = visited[i][j]
                if total_count[group] > 1:
                    board[i][j] = total_population[group] // total_count[group]
