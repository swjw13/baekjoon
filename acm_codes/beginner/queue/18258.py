# 큐 기초

from collections import deque
import sys

N = int(sys.stdin.readline())
que = deque()

for _ in range(N):
    q = sys.stdin.readline().split()

    if q[0] == 'push':
        que.append(int(q[1]))
    elif q[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            value = que.popleft()
            print(value)
    elif q[0] == 'size':
        print(len(que))
    elif q[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif q[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif q[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
