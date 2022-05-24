# 톱니바퀴 돌리기
# https://www.acmicpc.net/problem/15662

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
tops = [deque()]
for _ in range(T):
    tops.append(deque(list(input())[:-1]))

K = int(input())

for _ in range(K):

    top_number, rotation = list(map(int, input().split()))
    queue = deque([(top_number, rotation)])
    visited = [False for _ in range(T + 1)]
    visited[top_number] = True
    while queue:
        top_number, rotation_direction = queue.popleft()

        if top_number + 1 <= T and not visited[top_number + 1] and tops[top_number][2] != tops[top_number + 1][6]:
            queue.append((top_number + 1, rotation_direction * -1))
            visited[top_number + 1] = True
        if top_number - 1 >= 1 and not visited[top_number - 1] and tops[top_number][6] != tops[top_number - 1][2]:
            queue.append((top_number - 1, rotation_direction * -1))
            visited[top_number - 1] = True

        tops[top_number].rotate(rotation_direction)
ans = 0
for top in tops[1:]:
    if top[0] == '1':
        ans += 1
print(ans)
