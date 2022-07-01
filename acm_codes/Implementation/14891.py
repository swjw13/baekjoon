# https://www.acmicpc.net/problem/14891
# 톱니바퀴

import sys
from collections import deque
input = sys.stdin.readline

ring = []
for _ in range(4):
    ring.append(deque(list(map(int, list(input().strip())))))

K = int(input())
for _ in range(K):
    ring_no, dir = list(map(int, input().split()))
    rotate_list = [(ring_no, dir)]
    if ring_no == 1:
        if ring[0][2] != ring[1][6]:
            rotate_list.append((2, -dir))
            if ring[1][2] != ring[2][6]:
                rotate_list.append((3, dir))
                if ring[2][2] != ring[3][6]:
                    rotate_list.append((4, -dir))
    elif ring_no == 2:
        if ring[1][6] != ring[0][2]:
            rotate_list.append((1, -dir))
        if ring[1][2] != ring[2][6]:
            rotate_list.append((3, -dir))
            if ring[2][2] != ring[3][6]:
                rotate_list.append((4, dir))
    elif ring_no == 3:
        if ring[2][2] != ring[3][6]:
            rotate_list.append((4, -dir))
        if ring[2][6] != ring[1][2]:
            rotate_list.append((2, -dir))
            if ring[1][6] != ring[0][2]:
                rotate_list.append((1, dir))
    else:
        if ring[3][6] != ring[2][2]:
            rotate_list.append((3, -dir))
            if ring[2][6] != ring[1][2]:
                rotate_list.append((2, dir))
                if ring[1][6] != ring[0][2]:
                    rotate_list.append((1, -dir))
    for num, direction in rotate_list:
        ring[num - 1].rotate(direction)

ans = 0
tmp = 1
for i in range(4):
    ans += ring[i][0] * tmp
    tmp *= 2

print(ans)