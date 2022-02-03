import heapq
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = 10 ** 9

T = int(input())


def dijkstra(road, start_point, max_point):
    dist = [INF for _ in range(max_point + 1)]
    visited = []

    dist[start_point] = 0
    heapq.heappush(visited, [dist[start_point], start_point])

    while visited:
        current_dist, current_point = heapq.heappop(visited)

        if current_dist > dist[current_point]:
            continue

        for (new_point, new_weight) in road[current_point].items():
            new_dist = current_dist + new_weight
            if dist[new_point] > new_dist:
                dist[new_point] = new_dist
                heapq.heappush(visited, [new_dist, new_point])

    return dist


for _ in range(T):
    # n: 점의 갯수, m: 도로의 갯수, t: 정답 후보 갯수
    n, m, t = list(map(int, input().split()))

    # s: 출발지, g, h: 반드시 지나가는 두 점
    s, g, h = list(map(int, input().split()))
    
    roads = {i: {} for i in range(n + 1)}

    for _ in range(m):
        start, end, weight = list(map(int, input().split()))

        roads[start][end] = weight
        roads[end][start] = weight

    final_avail = []
    for _ in range(t):
        final_avail.append(int(input()))

    mandatory_weight = roads[g][h]
    answers = []
    for end_point in final_avail:
        dists = dijkstra(roads, s, n)

        res1 = dists[g] + mandatory_weight + dijkstra(roads, h, n)[end_point]
        res2 = dists[h] + mandatory_weight + dijkstra(roads, g, n)[end_point]

        res = min(res1, res2)

        tmp = dists[end_point]

        if res == tmp:
            answers.append(end_point)

    answers.sort()
    for i in answers:
        print(i, end=' ')
    print()
