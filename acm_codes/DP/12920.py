# https://www.acmicpc.net/problem/12920
# 평범한 배낭 2

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = list(map(int, input().split()))
things = []
jump = defaultdict(int)
idx = 0
for _ in range(N):
    V, C, K = list(map(int, input().split()))
    for i in range(K):
        things.append((V, C))
        jump[idx] = idx + (K - i)
        idx += 1

queue = deque([(0, 0, 0)])
max_value = 0
max_length = len(things)
while queue:
    cur_turn, cur_weight, cur_happy = queue.popleft()

    if cur_turn >= max_length:
        max_value = max(max_value, cur_happy)
    else:
        if cur_weight + things[cur_turn][0] <= M:
            queue.append((cur_turn + 1, cur_weight, cur_happy))
            queue.append((cur_turn + 1, cur_weight + things[cur_turn][0], cur_happy + things[cur_turn][1]))
        else:
            queue.append((jump[cur_turn], cur_weight, cur_happy))

print(max_value)
