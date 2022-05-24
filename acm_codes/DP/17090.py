# 미로 탈출
# https://www.acmicpc.net/problem/17090

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
movement = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

N, M = list(map(int, input().split()))
answer_map = [[0 for _ in range(M)] for _ in range(N)]
mp = []

for _ in range(N):
    mp.append(list(input())[:-1])

visited = [[False for _ in range(M)] for _ in range(N)]


def find_line(row, col):
    if not 0 <= row < N or not 0 <= col < M:
        return True
    elif visited[row][col]:
        if answer_map[row][col] == 1:
            return True
        else:
            return False
    else:
        visited[row][col] = True

        dx, dy = movement[mp[row][col]]
        new_row = row + dx
        new_col = col + dy

        tmp = find_line(new_row, new_col)

        if tmp:
            answer_map[row][col] = 1
            return True
        else:
            answer_map[row][col] = -1
            return False


ans = 0
for i in range(N):
    for j in range(M):
        if answer_map[i][j] == 0:
            tmp = find_line(i, j)
            if tmp:
                ans += 1
        elif answer_map[i][j] == 1:
            ans += 1

print(ans)
