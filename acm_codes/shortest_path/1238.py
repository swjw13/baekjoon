# 파티
# https://www.acmicpc.net/problem/1238

import sys
import heapq

input = sys.stdin.readline
INF = 10 ** 6

N, M, X = list(map(int, input().split()))
lines = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, length = list(map(int, input().split()))
    lines[start].append([end, length])


def dijkstra(s):
    dist = [INF for _ in range(N + 1)]
    heap = [(0, s)]
    dist[s] = 0

    while heap:
        cur_dist, cur_point = heapq.heappop(heap)

        if dist[cur_point] < cur_dist:
            continue

        for con_point, con_dist in lines[cur_point]:
            new_dist = cur_dist + con_dist
            if new_dist < dist[con_point]:
                dist[con_point] = new_dist
                heapq.heappush(heap, (new_dist, con_point))
    return dist


back_dist = dijkstra(X)
ans = 0
for i in range(1, N + 1):
    start_dist = dijkstra(i)[X]
    ans = max(ans, start_dist + back_dist[i])
print(ans)