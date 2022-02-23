# 파이프 옮기기
# https://www.acmicpc.net/problem/17070

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
mp = []
for _ in range(N):
    mp.append(list(map(int, input().split())))

# visited 기준은 시작점 기준
# 0: 가로, 1: 대각선, 2: 세로
visited = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
visited[0][0][0] = 1

for i in range(N):
    for j in range(N):
        # 가로
        if i == 0 and j == 0:
            pass
        if mp[i][j] == 1:
            pass

        if j + 1 < N and mp[i][j + 1] != 1:
            visited[i][j][0] += visited[i][j - 1][0]
        if i + 1 < N and j + 1 < N and mp[i][j + 1] + mp[i + 1][j] + mp[i + 1][j + 1] == 0:
            visited[i][j][1] += visited[i][j - 1][0]

        if i >= 1:
            if i + 1 < N and mp[i + 1][j] != 1:
                visited[i][j][2] += visited[i - 1][j][2]
            if i + 1 < N and j + 1 < N and mp[i + 1][j] + mp[i][j + 1] + mp[i + 1][j + 1] == 0:
                visited[i][j][1] += visited[i - 1][j][2]
            if j >= 1:
                if j + 1 < N and mp[i][j + 1] != 1:
                    visited[i][j][0] += visited[i - 1][j - 1][1]
                if i + 1 < N and mp[i + 1][j] != 1:
                    visited[i][j][2] += visited[i - 1][j - 1][1]
                if i + 1 < N and j + 1 < N and mp[i + 1][j] + mp[i][j + 1] + mp[i + 1][j + 1] == 0:
                    visited[i][j][1] += visited[i - 1][j - 1][1]

print(visited[N - 2][N - 1][2] + visited[N - 1][N - 2][0] + visited[N - 2][N - 2][1])
