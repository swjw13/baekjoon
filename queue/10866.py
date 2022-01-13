# 덱 기초

from collections import deque
import sys
N = int(input())
que = deque()

for _ in range(N):
    ans = sys.stdin.readline().split()

    if ans[0] == 'push_front':
        que.appendleft(int(ans[1]))
    elif ans[0] == 'push_back':
        que.append(int(ans[1]))
    elif ans[0] == 'pop_front':
        if len(que) == 0:
            print(-1)
        else:
            val = que.popleft()
            print(val)
    elif ans[0] == 'pop_back':
        if len(que) == 0:
            print(-1)
        else:
            val = que.pop()
            print(val)
    elif ans[0] == 'size':
        print(len(que))
    elif ans[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif ans[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif ans[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])