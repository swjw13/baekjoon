# https://www.acmicpc.net/problem/1449
# 수리공 항승

import sys
input = sys.stdin.readline

N, L = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst.sort()

cnt = 0
tape = set()
minimum = -1
for i in lst:
    if len(tape) == 0:
        tape.add(i)
        cnt += 1
        minimum = i
    else:
        if minimum + L > i:
            tape.add(i)
            if len(tape) == L:
                tape = set()
                minimum = -1
        else:
            tape = {i}
            cnt += 1
            minimum = i

print(cnt)