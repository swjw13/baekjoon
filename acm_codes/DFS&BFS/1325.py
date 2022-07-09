# https://www.acmicpc.net/problem/1325
# 효율적인 해킹

import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
connection = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    connection[b].append(a)


def bfs(comp):
    queue = deque([comp])
    visited = [False] * (N + 1)
    visited[comp] = True
    count = 1
    while queue:
        target = queue.popleft()
        for new_target in connection[target]:
            if not visited[new_target]:
                queue.append(new_target)
                visited[new_target] = True
                count += 1

    return count


max_cnt = 0
answer = []
for i in range(1, N + 1):
    a = bfs(i)
    if max_cnt == a:
        answer.append(i)
    elif max_cnt < a:
        answer = [i]
        max_cnt = a

print(" ".join(list(map(str, answer))))