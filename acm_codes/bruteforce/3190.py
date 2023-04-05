import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
k = int(input())

apples = [[False for _ in range(n)] for _ in range(n)]
for _ in range(k):
    row, col = list(map(int, input().split()))
    apples[row - 1][col - 1] = True

direction = 0
movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
l = int(input())
direction_change = defaultdict(str)
for _ in range(l):
    t, new_dir = input().split()
    direction_change[int(t)] = new_dir

snake = deque([(0, 0)])
turn = 0
while True:
    head = snake[-1]
    new_head = (head[0] + movement[direction][0], head[1] + movement[direction][1])
    turn += 1

    if new_head in snake:
        print(turn)
        break

    if not (0 <= new_head[0] < n) or not (0 <= new_head[1] < n):
        print(turn)
        break

    if not apples[new_head[0]][new_head[1]]:
        snake.popleft()
    else:
        apples[new_head[0]][new_head[1]] = False

    snake.append(new_head)

    new_direction_change = direction_change[turn]
    if len(new_direction_change) != 0:
        if new_direction_change == "L":
            direction -= 1
            if direction < 0:
                direction = 3
        else:
            direction = (direction + 1) % 4
