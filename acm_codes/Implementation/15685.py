# 드래곤 커브
# https://www.acmicpc.net/problem/15685

import sys

input = sys.stdin.readline
dydx = [(1, 0), (0, -1), (-1, 0), (0, 1)]

N = int(input())
dragon_points = set()

for _ in range(N):
    x, y, d, g = list(map(int, input().split()))

    points_to_update = set()
    start_point = (x, y)
    rotation_center = (x + dydx[d][0], y + dydx[d][1])
    points = (start_point, rotation_center)
    points_to_update.update(points)
    while g > 0:
        tmp = set()
        for dx, dy in points_to_update:
            relative_x = dx - rotation_center[0]
            relative_y = dy - rotation_center[1]
            tmp.add((-relative_y + rotation_center[0], relative_x + rotation_center[1]))
        points_to_update.update(tmp)
        rotation_center = (-start_point[1] + rotation_center[1] + rotation_center[0],
                           start_point[0] - rotation_center[0] + rotation_center[1])
        g -= 1
    dragon_points.update(points_to_update)

ans = 0
for i in range(100):
    for j in range(100):
        if (i, j) in dragon_points and (i + 1, j) in dragon_points and (i, j + 1) in dragon_points and (
                i + 1, j + 1) in dragon_points:
            ans += 1

print(ans)
