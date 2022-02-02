# 0-1 BFS
# 간선의 길이가 0, 1 만 있을 경우
# BFS를 활용하여 다익스트라 알고리즘을 실행하는데
# 간선이 0일 경우 deque 의 앞에, 1일 경우 뒤에 추가 해준다.
# 다익스트라보다 효율적인 알고리즘이지만 특정한 경우에만 사용할 수 있다.

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
INF = 10 ** 6

dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

M, N = list(map(int, input().split()))
mp = []
for _ in range(N):
    mp.append(list(map(int, list(input()[:-1]))))

distance = [[INF for _ in range(M)] for _ in range(N)]

queue = deque([(0, 0, 0)])
distance[0][0] = 0

while queue:
    row, col, current_dist = queue.popleft()

    for (dx, dy) in dydx:
        x = row + dx
        y = col + dy
        if 0 <= x < N and 0 <= y < M:
            new_dist = current_dist + mp[x][y]
            if new_dist < distance[x][y]:
                if mp[x][y] == 1:
                    queue.append((x, y, new_dist))
                else:
                    queue.appendleft((x, y, new_dist))
                distance[x][y] = new_dist

print(distance[N - 1][M - 1])
