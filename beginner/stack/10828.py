# 스택

import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    action = sys.stdin.readline().split()
    if action[0] == "push":
        value = int(action[1])
        stack.append(value)

    elif action[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            value = stack.pop()
            print(value)

    elif action[0] == "size":
        print(len(stack))

    elif action[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif action[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])