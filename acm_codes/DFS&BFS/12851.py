# https://www.acmicpc.net/problem/12851
# 숨바꼭질

import sys
from collections import deque

input = sys.stdin.readline

N, K = list(map(int, input().split()))

if N >= K:
    print(N - K)
    print(1)
else:
    distance = [100000 for _ in range(100001)]
    cnt = 0
    queue = deque([(N, 0)])

    while queue:
        cur_point, cur_dist = queue.popleft()
        if cur_point == K:
            if cur_dist < distance[K]:
                distance[K] = cur_dist
                cnt = 1
            elif cur_dist == distance[K]:
                cnt += 1
        else:
            if cur_point + 1 <= 100000 and distance[cur_point + 1] >= cur_dist + 1:
                distance[cur_point + 1] = cur_dist + 1
                queue.append((cur_point + 1, cur_dist + 1))
            if cur_point * 2 <= 100000 and distance[cur_point * 2] >= cur_dist + 1:
                distance[cur_point * 2] = cur_dist + 1
                queue.append((cur_point * 2, cur_dist + 1))
            if cur_point - 1 >= 0 and distance[cur_point - 1] >= cur_dist + 1:
                distance[cur_point - 1] = cur_dist + 1
                queue.append((cur_point - 1, cur_dist + 1))

    print(distance[K])
    print(cnt)
