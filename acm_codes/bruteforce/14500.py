# 테크로미노
# https://www.acmicpc.net/problem/14500

import sys

checklist_row = [(0, 0, 0, 1), (0, 0, 0, 2), (0, 0, 1, 2), (0, 1, 0, 2), (0, 2, 1, 0), (1, 0, 1, 1), (1, 0, 1, 2),
                 (1, 1, 1, 2)]
checklist_col = [(0, 0, 1, 0), (0, 0, 2, 0), (0, 0, 2, 1), (0, 1, 1, 1), (0, 1, 2, 0), (0, 1, 2, 1), (1, 0, 2, 0),
                 (1, 1, 2, 1)]
input = sys.stdin.readline
mp = []
N, M = list(map(int, input().split()))

for _ in range(N):
    mp.append(list(map(int, input().split())))

mx = 0

for i in range(N - 1):
    for j in range(M - 1):
        # 네모
        mx = max(mx, mp[i][j] + mp[i][j + 1] + mp[i + 1][j] + mp[i + 1][j + 1])

        # 막대기
        if i < N - 3:
            mx = max(mx, mp[i][j] + mp[i + 1][j] + mp[i + 2][j] + mp[i + 3][j])

        if j < M - 3:
            mx = max(mx, mp[i][j] + mp[i][j + 1] + mp[i][j + 2] + mp[i][j + 3])

        # 나머지
        if i < N - 2:
            tmp = mp[i][j] + mp[i + 1][j] + mp[i + 2][j] + mp[i][j + 1] + mp[i + 1][j + 1] + mp[i + 2][j + 1]
            for (a, b, c, d) in checklist_col:
                mx = max(mx, tmp - mp[i + a][j + b] - mp[i + c][j + d])

        if j < M - 2:
            tmp = mp[i][j] + mp[i][j + 1] + mp[i][j + 2] + mp[i + 1][j] + mp[i + 1][j + 1] + mp[i + 1][j + 2]
            for (a, b, c, d) in checklist_row:
                mx = max(mx, tmp - mp[i + a][j + b] - mp[i + c][j + d])

for j in range(0, M - 3):
    mx = max(mx, mp[N - 1][j] + mp[N - 1][j + 1] + mp[N - 1][j + 2] + mp[N - 1][j + 3])
for i in range(0, N - 3):
    mx = max(mx, mp[i][M - 1] + mp[i + 1][M - 1] + mp[i + 2][M - 1] + mp[i + 3][M - 1])

print(mx)