# https://www.acmicpc.net/problem/17472
# 다리 만들기2

import sys
from collections import deque, defaultdict
import heapq

input = sys.stdin.readline
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]
island_num = 2

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            board[i][j] = island_num
            visited[i][j] = True
            queue = deque([(i, j)])
            while queue:
                cur_row, cur_col = queue.popleft()
                for dx, dy in dxdy:
                    new_row = cur_row + dx
                    new_col = cur_col + dy
                    if 0 <= new_row < N and 0 <= new_col < M and board[new_row][new_col] == 1:
                        board[new_row][new_col] = island_num
                        queue.append((new_row, new_col))
            island_num += 1

t = []
for i in range(N):
    memory = defaultdict(set)
    order = []
    for j in range(M):
        if board[i][j] != 0:
            memory[board[i][j]].add(j)
            order.append(board[i][j])

    if len(memory.keys()) > 1:
        for i in range(len(order) - 1):
            if order[i] != order[i + 1]:
                one = memory[order[i]]
                two = memory[order[i + 1]]
                tmp = min(abs(min(one) - max(two)), abs(max(one) - min(two)))

                if tmp > 2:
                    start_point = min(order[i], order[i + 1])
                    end_point = max(order[i], order[i + 1])
                    t.append([tmp - 1, start_point, end_point])

for j in range(M):
    memory = defaultdict(set)
    order = []
    for i in range(N):
        if board[i][j] != 0:
            memory[board[i][j]].add(i)
            order.append(board[i][j])

    if len(memory.keys()) > 1:
        for i in range(len(order) - 1):
            if order[i] != order[i + 1]:
                one = memory[order[i]]
                two = memory[order[i + 1]]
                tmp = min(abs(min(one) - max(two)), abs(max(one) - min(two)))
                if tmp > 2:
                    start_point = min(order[i], order[i + 1])
                    end_point = max(order[i], order[i + 1])
                    t.append([tmp - 1, start_point, end_point])

parent = [i for i in range(island_num)]


def find_parend(p):
    if parent[p] != p:
        parent[p] = find_parend(parent[p])
    return parent[p]


def union(p1, p2):
    p1 = find_parend(p1)
    p2 = find_parend(p2)
    tmp = min(p1, p2)
    parent[p1] = tmp
    parent[p2] = tmp


heapq.heapify(t)
length = len(t)
ans = 0
for _ in range(length):
    tmp = heapq.heappop(t)
    a = find_parend(tmp[1])
    b = find_parend(tmp[2])
    if a != b:
        ans += tmp[0]
        union(a, b)
tmp = True
for i in range(2, island_num):
    if find_parend(i) != find_parend(2):
        tmp = False
        break
if tmp:
    print(ans)
else:
    print(-1)
