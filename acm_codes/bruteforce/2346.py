# https://www.acmicpc.net/problem/2346
# 풍선 터트리기

from collections import deque

N = int(input())
lst = list(map(int, input().split()))

answer = []
queue = deque()
for i in range(N):
    queue.append((i + 1, lst[i]))

while queue:
    cur_idx, cur_number = queue.popleft()
    answer.append(cur_idx)
    if cur_number < 0:
        queue.rotate(-cur_number)
    elif cur_number > 0:
        queue.rotate(-cur_number + 1)

print(" ".join(list(map(str, answer))))