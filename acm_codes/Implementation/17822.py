# 원판 돌리기
# https://www.acmicpc.net/problem/17822

import sys
from collections import deque

input = sys.stdin.readline
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M, T = list(map(int, input().split()))
circles = []

for _ in range(N):
    circles.append(deque(list(map(int, input().split()))))


def check():
    point_to_change = []

    for i in range(N):
        for j in range(M):
            if circles[i][j] == 0:
                continue
            else:
                for dx, dy in dxdy:
                    new_row = i + dx
                    new_col = (j + dy) % M
                    if 0 <= new_row < N and circles[i][j] == circles[new_row][new_col]:
                        point_to_change.append((i, j))
                        break

    if len(point_to_change) == 0:
        mid = 0
        count = 0
        for i in circles:
            for number in i:
                if number != 0:
                    mid += number
                    count += 1
        for i in range(N):
            for j in range(M):
                if circles[i][j] != 0:
                    if circles[i][j] > mid / count:
                        circles[i][j] -= 1
                    elif circles[i][j] < mid / count:
                        circles[i][j] += 1
    else:
        for (row, col) in point_to_change:
            circles[row][col] = 0


for _ in range(T):
    circle_num, direction, how_much = list(map(int, input().split()))
    start_circle = circle_num - 1

    while start_circle < N:
        if direction == 0:
            circles[start_circle].rotate(how_much)
        else:
            circles[start_circle].rotate(-how_much)
        start_circle += circle_num

    check()

ans = 0
for circle in circles:
    ans += sum(circle)

print(ans)
