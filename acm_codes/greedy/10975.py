# https://www.acmicpc.net/problem/10975
# 데크 소트

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
turn = defaultdict(int)
numbers = []
for i in range(N):
    a = int(input())
    turn[a] = i
    numbers.append(a)

if N == 1:
    print(1)
else:
    numbers.sort()
    idxs = []
    for i in numbers:
        idxs.append(turn[i])
    cur_state = -1
    if idxs[0] < idxs[1]:
        cur_state = 0
    else:
        cur_state = 1

    answer = 1
    for i in range(len(idxs) - 1):
        if idxs[i] < idxs[i + 1] and cur_state == 1:
            cur_state = 0
        elif idxs[i] > idxs[i + 1] and cur_state == 0:
            cur_state = 1
            answer += 1
    print(answer)
