import heapq
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = sys.maxsize

N, E = list(map(int, input().split()))
lines = [[] for _ in range(N + 1)]

for _ in range(E):
    start, end, weight = list(map(int, input().split()))
    lines[start].append([end, weight])
    lines[end].append([start, weight])
v1, v2 = list(map(int, input().split()))


def dijkstra(start, end):
    dist = [INF for _ in range(N + 1)]
    # (거리 정보, 점) 이렇게 큐를 구성
    priority_queue = [[dist[start], start]]
    dist[start] = 0

    while priority_queue:
        current_dist, current_point = heapq.heappop(priority_queue)

        # 만약 현재 값이 기록된 거리보다 멀다면 볼 필요도 없음
        if dist[current_point] < current_dist:
            continue
        # 연결 된 점들 중 distance update 가 필요 한 점이 있다면
        # update 를 한 후 큐에 넣어준다.
        for (new_point, w) in lines[current_point]:
            new_dist = current_dist + w
            if dist[new_point] > new_dist:
                dist[new_point] = new_dist
                heapq.heappush(priority_queue, [new_dist, new_point])

    return dist[end]


ans_1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
ans_2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

ans = min(ans_2, ans_1)
if ans >= INF:
    print(-1)
else:
    print(ans)
