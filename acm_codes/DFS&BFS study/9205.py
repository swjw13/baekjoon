import sys
from collections import deque

input = sys.stdin.readline
MAX = 32767 + 32768


def get_distance(start_x, start_y, end_x, end_y):
    return abs(start_x - end_x) + abs(start_y - end_y)


T = int(input())
for _ in range(T):
    tmp = False
    N = int(input())

    points = []
    visited = {}
    start_x, start_y = list(map(int, input().split()))

    for _ in range(N):
        x, y = list(map(int, input().split()))
        points.append((x, y))
        if x not in visited.keys():
            visited[x] = {}
        visited[x][y] = False

    end_x, end_y = list(map(int, input().split()))
    points.append((end_x, end_y))
    if end_x not in visited.keys():
        visited[end_x] = {}
    visited[end_x][end_y] = False

    queue = deque([(start_x, start_y)])

    while queue:
        current_x, current_y = queue.popleft()
        if current_x == end_x and current_y == end_y:
            tmp = True
            break

        for (middle_x, middle_y) in points:
            if not visited[middle_x][middle_y] and get_distance(current_x, current_y, middle_x,
                                                                                middle_y) <= 1000:
                visited[middle_x][middle_y] = True
                queue.append((middle_x, middle_y))

    if tmp:
        print("happy")
    else:
        print("sad")
