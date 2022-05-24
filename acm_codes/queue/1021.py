# 회전하는 큐
from collections import deque

N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))
que = deque([i for i in range(1, N + 1)])
answer = 0

while lst:
    turn = 0
    value = lst.pop(0)
    while que[0] != value:
        tmp = que.popleft()
        que.append(tmp)
        turn += 1
    answer += min(turn, N - turn)
    que.popleft()
    N -= 1

print(answer)