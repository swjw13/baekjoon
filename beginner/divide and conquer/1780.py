# 종이의 갯수
# 유의점: 전체를 비교하는 task에서는 list 줄마다 비교해보면 어떨지 생각해보자

import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
pic = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    pic.append(line)


def check(row_start, row_end, col_start, col_end):
    for i in range(row_start, row_end):
        if set(pic[i][col_start:col_end]) != {pic[row_start][col_start]}:
            return False, -2
    return True, pic[row_start][col_start]


count = [0, 0, 0]
tmp = 1
while tmp <= N:
    for i in range(0, N, tmp):
        for j in range(0, N, tmp):
            what, val = check(i, i + tmp, j, j + tmp)
            if what:
                if tmp == 1:
                    count[val + 1] += 1
                else:
                    count[val + 1] -= 8
    tmp *= 3

for i in count:
    print(i)