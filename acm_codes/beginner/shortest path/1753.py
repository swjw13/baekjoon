# 다익스트라 알고리즘

import heapq
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = sys.maxsize

V, E = list(map(int, input().split()))
start_point = int(input())

lines = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = list(map(int, input().split()))
    lines[s].append([e, w])

visited = []
length = [INF for _ in range(V + 1)]
length[start_point] = 0
heapq.heappush(visited, [length[start_point], start_point])

while visited:
    dist, point = heapq.heappop(visited)

    if length[point] < dist:
        continue
    for new_point, new_dist in lines[point]:
        _distance = dist + new_dist
        if _distance < length[new_point]:
            length[new_point] = _distance
            heapq.heappush(visited, [_distance, new_point])

for i in length[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)
