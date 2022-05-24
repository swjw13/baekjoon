# 컨베이어 벨트
# https://www.acmicpc.net/problem/20055

import sys
from collections import deque
input = sys.stdin.readline

N, K = list(map(int, input().split()))

strengths = deque(list(map(int, input().split())))
robots_on_line = deque([False for _ in range(2 * N)])

turn = 1

while True:
    strengths.rotate(1)
    robots_on_line.rotate(1)

    # 로봇을 내림
    robots_on_line[N - 1] = False

    # 로봇을 이동시킴
    if robots_on_line[N - 2] and strengths[N - 1] > 0:
        robots_on_line[N - 2] = False
        strengths[N - 1] -= 1

    for i in range(N-3, -1, -1):
        if robots_on_line[i] and not robots_on_line[i + 1] and strengths[i + 1] > 0:
            robots_on_line[i] = False
            robots_on_line[i + 1] = True
            strengths[i + 1] -= 1

    # 로봇을 올림
    if not robots_on_line[0] and strengths[0] != 0:
        strengths[0] -= 1
        robots_on_line[0] = True

    ans = 0
    for i in range(2 * N):
        if strengths[i] == 0:
            ans += 1

    if ans >= K:
        print(turn)
        break
    else:
        turn += 1
