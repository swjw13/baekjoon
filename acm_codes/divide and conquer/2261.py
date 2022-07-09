# 가장 가까운 두 점의 거리(미해결)

import sys

sys.setrecursionlimit(1000000)
points = set()
n = int(sys.stdin.readline())
for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    points.add((x, y))
points = list(points)
n = len(points)
points.sort(key=lambda xt: xt[0])


def dist(num1, num2):
    return (points[num1][0] - points[num2][0]) ** 2 + (points[num1][1] - points[num2][1]) ** 2


def nearest(start, end):
    if start == end:
        return 800000001
    mid = (start + end) // 2
    side = min(nearest(start, mid), nearest(mid + 1, end))

    low = mid
    hi = mid + 1

    lst = []
    while low >= start and low >= mid - int(side ** 0.5):
        lst.append(low)
        low -= 1
    while hi <= end and hi <= mid + int(side ** 0.5):
        lst.append(hi)
        hi += 1

    for i in lst:
        for j in lst:
            if i != j:
                side = min(side, dist(i, j))
    return side


print(nearest(0, n - 1))
