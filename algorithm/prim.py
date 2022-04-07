# 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197

import heapq
import sys
input = sys.stdin.readline

V, E = list(map(int, input().split()))
lines = [[] for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]
ans = 0

for _ in range(E):
    point1, point2, weight = list(map(int, input().split()))
    lines[point1].append([weight, point2])
    lines[point2].append([weight, point1])

queue = lines[1]
heapq.heapify(queue)
visited[1] = True
while queue:
    w, p = heapq.heappop(queue)
    if not visited[p]:
        ans += w
        visited[p] = True
        for con_weight, con_point in lines[p]:
            if not visited[con_point]:
                heapq.heappush(queue, [con_weight, con_point])

print(ans)
