# https://www.acmicpc.net/problem/1686
# 복날
import sys
from collections import deque

input = sys.stdin.readline
INF = 1000000.0

v, m = list(map(int, input().split()))
xs, ys = list(map(float, input().split()))
xt, yt = list(map(float, input().split()))
bunkers = [[xs, ys]]


def get_distance(x_start: float, y_start: float, x_end: float, y_end: float):
    return ((x_start - x_end) ** 2 + (y_start - y_end) ** 2) ** 0.5


while True:
    try:
        a, b = list(map(float, input().split()))
        bunkers.append([a, b])

    except:
        bunkers.append([xt, yt])
        length = len(bunkers)
        distances = [[INF for _ in range(length)] for _ in range(length)]
        for i in range(length):
            for j in range(length):
                if i != j:
                    cur_dist = get_distance(bunkers[i][0], bunkers[i][1], bunkers[j][0], bunkers[j][1])
                    distances[i][j] = cur_dist
                    distances[j][i] = cur_dist

        visited = [False for _ in range(length)]
        queue = deque([(0, 0)])
        visited[0] = True
        check = -1
        while queue:
            cur_point, turn = queue.popleft()
            if cur_point == length - 1:
                check = turn
                break

            for i in range(length):
                if distances[i][cur_point] <= v * m * 60 and not visited[i]:
                    queue.append((i, turn + 1))
                    visited[i] = True

        if check != -1:
            print("Yes, visiting %d other holes." % (check - 1))
        else:
            print("No.")
        break
