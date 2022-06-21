# KCM Travel
# https://www.acmicpc.net/problem/10217

import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = list(map(int, input().split()))
    airplanes = {i: dict() for i in range(N + 1)}
    for _ in range(K):
        start, end, cost, dist = list(map(int, input().split()))
        airplanes[start][end] = (cost, dist)
    dist = [sys.maxsize for _ in range(N + 1)]
    dist[1] = 0
    visited = [[dist[1], 1, 0]]
    while visited:
        cur_dist, cur_city, cur_cost = heapq.heappop(visited)
        for con_city in airplanes[cur_city].keys():
            new_dist = cur_dist + airplanes[cur_city][con_city][1]
            new_cost = cur_cost + airplanes[cur_city][con_city][0]
            if new_cost <= M:
                if dist[con_city] > new_dist:
                    dist[con_city] = new_dist
                heapq.heappush(visited, [new_dist, con_city, new_cost])
    if dist[N] == sys.maxsize:
        print("Poor KCM")
    else:
        print(dist[N])
