# https://www.acmicpc.net/problem/1158
# 요세푸스 문제

from collections import deque
N, K = list(map(int, input().split()))

queue = deque([i for i in range(1, N + 1)])
stack = []

idx = 0
while queue:
    cur_point = queue.popleft()
    idx += 1

    if idx == K:
        stack.append(cur_point)
        idx = 0
    else:
        queue.append(cur_point)

print("<" + ", ".join(list(map(str, stack))) + ">")
