# 최소비용 구하기
# https://www.acmicpc.net/problem/1916
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())
lines = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, dist = list(map(int, input().split()))
    lines[start].append([end, dist])
s, e = list(map(int, input().split()))
distance = [INF for _ in range(N + 1)]
heap = [(0, s)]
distance[s] = 0
while heap:
    cur_dist, cur_point = heapq.heappop(heap)

    if distance[cur_point] < cur_dist:
        continue

    for con_point, con_dist in lines[cur_point]:
        new_dist = cur_dist + con_dist
        if distance[con_point] > new_dist:
            distance[con_point] = new_dist
            heapq.heappush(heap, (new_dist, con_point))

print(distance[e])
