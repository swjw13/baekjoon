# 숫자판 점프
# https://www.acmicpc.net/problem/2210

import sys
from collections import deque

input = sys.stdin.readline
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

mp = []
for _ in range(5):
    mp.append(list(map(int, input().split())))

word_list = set()
for i in range(5):
    for j in range(5):
        queue = deque([(i, j, str(mp[i][j]), 0)])
        while queue:
            row, col, prev, turn = queue.popleft()
            if turn == 5:
                word_list.add(prev)
                continue
            for dx, dy in dydx:
                x = row + dx
                y = col + dy
                if 0 <= x < 5 and 0 <= y < 5:
                    queue.append((x, y, prev + str(mp[x][y]), turn + 1))

print(len(word_list))