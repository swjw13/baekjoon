# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
connection = defaultdict(set)

for _ in range(N - 1):
    p1, p2 = list(map(int, input().split()))
    connection[p1].add(p2)
    connection[p2].add(p1)

visited = [False for _ in range(N + 1)]
queue = deque([1])
visited[1] = True

answer = defaultdict(int)
while queue:
    cur_point = queue.popleft()
    for i in connection[cur_point]:
        if not visited[i]:
            visited[i] = True
            answer[i] = cur_point
            queue.append(i)

for i in range(2, N + 1):
    print(answer[i])