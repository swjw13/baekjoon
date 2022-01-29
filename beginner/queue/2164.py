# 큐, 카드문제

from collections import deque

N = int(input())

que = deque([i for i in range(1, N + 1)])

while len(que) != 1:
    que.popleft()
    value = que.popleft()
    que.append(value)
print(que[0])