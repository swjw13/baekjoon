# 밸만 포드 알고리즘: 간선 중 음수가 있는 경우

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = 10 ** 9

N, M = list(map(int, input().split()))
lines = []
for _ in range(M):
    s, e, w = list(map(int, input().split()))
    lines.append([s, e, w])


def balman_ford(start):
    dist = [INF for _ in range(N + 1)]
    dist[start] = 0

    # n - 1 번 모든 node에 대해 update 반복
    for i in range(N - 1):
        for [s, e, w] in lines:
            if dist[s] != INF and dist[s] + w < dist[e]:
                dist[e] = dist[s] + w

    # cycle 판독. n - 1 번 뒤에도 update가 계속된다면 cycle이 존재하는 것이다.
    cycle = False
    for s, e, w in lines:
        if dist[s] != INF and dist[s] + w < dist[e]:
            cycle = True
            break

    if cycle:
        return [-1]
    else:
        return dist


ans = balman_ford(1)

if len(ans) == 1:
    print(-1)
else:
    for i in ans[2:]:
        if i == INF:
            print(-1)
        else:
            print(i)
