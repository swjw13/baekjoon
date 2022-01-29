from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = sys.maxsize

T = int(input())
for _ in range(T):
    N, M, K = list(map(int, input().split()))
    airplane = [[] for _ in range(N + 1)]

    for _ in range(K):
        start, end, cost, time = list(map(int, input().split()))
        airplane[start].append([end, cost, time])

    point_info = [(INF, INF) for _ in range(N + 1)]
    queue = deque([(1, 0, 0)])
    while queue:
        current_point, current_cost, current_time = queue.popleft()
        if current_cost > M:
            continue
        if current_cost > point_info[current_point][0] and current_time > point_info[current_point][1]:
            continue

        for (new_point, new_cost, new_time) in airplane[current_point]:
            cost = current_cost + new_cost
            time = current_time + new_time
            if cost <= point_info[current_point][0] or time <= point_info[current_point][1]:
                queue.append((new_point, cost, time))

    print(point_info[N])
