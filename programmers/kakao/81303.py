# 표 편집
# https://programmers.co.kr/learn/courses/30/lessons/81303
# 2021 kakao
from collections import deque


def solution(n, k, cmd):
    answer = ""
    lst = [True for _ in range(n)]
    stack = deque()
    up = [i - 1 for i in range(n)]
    down = [i + 1 for i in range(n)]

    for q in cmd:
        tmp = q.split()

        if tmp[0] == "U":
            for _ in range(int(tmp[1])):
                k = up[k]

        elif tmp[0] == "D":
            for _ in range(int(tmp[1])):
                k = down[k]

        elif tmp[0] == "C":
            if down[k] < n:
                a = down[k]
                b = up[k]
                down[b] = a
                up[a] = b
                lst[k] = False
                stack.append(k)
                k = down[k]
            else:
                a = up[k]
                down[a] = n
                lst[k] = False
                stack.append(k)
                k = a

        else:
            tmp = stack.pop()
            idx = tmp + 1
            while idx < n and not lst[idx]:
                idx += 1
            down[tmp] = idx
            if idx < n:
                up[idx] = tmp

            idx = tmp - 1
            while idx >= 0 and not lst[idx]:
                idx = up[idx]
            up[tmp] = idx
            if idx >= 0:
                down[idx] = tmp

            lst[tmp] = True

    for i in lst:
        if i:
            answer += "O"
        else:
            answer += "X"
    return answer
