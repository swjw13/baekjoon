# 사각지대
# https://www.acmicpc.net/problem/15683

import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
mp = []
for _ in range(N):
    mp.append(list(map(int, input().split())))


def find_safe_zone(camera_num, row, col):
    lst = []
    tmp1, tmp2, tmp3, tmp4 = set(), set(), set(), set()
    start = 0
    # tmp1: 위 방향
    while row - start >= 0 and mp[row - start][col] != 6:
        tmp1.add((row - start, col))
        start += 1

    # tmp2: 오른쪽
    start = 0
    while col + start < M and mp[row][col + start] != 6:
        tmp2.add((row, col + start))
        start += 1

    # tmp3: 아래
    start = 0
    while row + start < N and mp[row + start][col] != 6:
        tmp3.add((row + start, col))
        start += 1

    # tmp4: 왼쪽
    start = 0
    while col - start >= 0 and mp[row][col - start] != 6:
        tmp4.add((row, col - start))
        start += 1
    all_dir = set()
    all_dir.update(tmp1, tmp2, tmp3, tmp4)

    if camera_num == 1:
        lst.append(tmp1)
        lst.append(tmp2)
        lst.append(tmp3)
        lst.append(tmp4)
    elif camera_num == 2:
        lst.append(tmp1.union(tmp3))
        lst.append(tmp2.union(tmp4))
    elif camera_num == 3:
        lst.append(tmp1.union(tmp2))
        lst.append(tmp2.union(tmp3))
        lst.append(tmp3.union(tmp4))
        lst.append(tmp4.union(tmp1))
    elif camera_num == 4:
        lst.append(all_dir.difference(tmp1).union({(row, col)}))
        lst.append(all_dir.difference(tmp2).union({(row, col)}))
        lst.append(all_dir.difference(tmp3).union({(row, col)}))
        lst.append(all_dir.difference(tmp4).union({(row, col)}))
    elif camera_num == 5:
        lst.append(all_dir)
    return lst


a = []
count_wall = 0
for i in range(N):
    for j in range(M):
        if mp[i][j] in [1, 2, 3, 4, 5]:
            a.append(find_safe_zone(mp[i][j], i, j))
        elif mp[i][j] == 6:
            count_wall += 1

mx = 0
from itertools import product

for i in product(*a):
    tm = set()
    for points in i:
        tm.update(points)
    mx = max(mx, len(tm))

print(M * N - mx - count_wall)
