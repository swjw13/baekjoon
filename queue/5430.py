import sys
from collections import deque
import ast

T = int(sys.stdin.readline())

for _ in range(T):
    todo = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    lst = sys.stdin.readline()
    lst = ast.literal_eval(lst)

    que = deque(lst)
    tmp = -1
    check_error = 0
    for i in todo:
        if i == "R":
            tmp *= -1
        elif i == "D":
            if len(que) == 0:
                check_error = 1
                break
            else:
                if tmp == -1:
                    que.popleft()
                else:
                    que.pop()
    if check_error == 1:
        print("error")
    else:
        print("[", end="")
        if len(que) == 0:
            print("]")
        elif tmp == -1:
            for i in range(len(que) - 1):
                print("{},".format(que[i]), end="")
            print("{}]".format(que[-1]))
        else:
            for i in range(len(que) - 1, 0, -1):
                print("{},".format(que[i]), end="")
            print("{}]".format(que[0]))
