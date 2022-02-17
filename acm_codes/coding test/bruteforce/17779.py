# 게리맨더링
# https://www.acmicpc.net/problem/17779

import sys

input = sys.stdin.readline

N = int(input())
mp = []
for _ in range(N):
    mp.append(list(map(int, input().split())))


def point_in_board(point):
    if 0 <= point[0] < N and 0 <= point[1] < N:
        return True
    else:
        return False


def point_in_square(row, col, main_point, d1_, d2_):
    if d1_ > d2_:
        if main_point[0] <= row <= main_point[0] + d2_:
            dist = row - main_point[0]
            if main_point[1] - dist <= col <= main_point[1] + dist:
                return True
            else:
                return False

        elif main_point[0] + d2_ < row <= main_point[0] + d1_:
            if sum(main_point) <= row + col <= sum(main_point) + 2 * d2_:
                return True
            else:
                return False

        elif main_point[0] + d1_ < row <= main_point[0] + d1_ + d2_:
            dist = main_point[0] + d1_ + d2_ - row
            if main_point[1] - d1_ + d2_ - dist <= col <= main_point[1] - d1_ + d2_ + dist:
                return True
            else:
                return False

        else:
            return False

    else:
        if main_point[0] <= row <= main_point[0] + d1_:
            dist = row - main_point[0]
            if main_point[1] - dist <= col <= main_point[1] + dist:
                return True
            else:
                return False

        elif main_point[0] + d1_ < row <= main_point[0] + d2_:
            if main_point[1] - main_point[0] - 2 * d1_ <= col - row <= main_point[1] - main_point[0]:
                return True
            else:
                return False

        elif main_point[0] + d2_ < row <= main_point[0] + d1_ + d2_:
            dist = main_point[0] + d1_ + d2_ - row
            if main_point[1] - d1_ + d2_ - dist <= col <= main_point[1] - d1_ + d2_ + dist:
                return True
            else:
                return False
        else:
            return False


def find_population(main_point, d1_, d2_):
    ans = [0, 0, 0, 0, 0]
    for i in range(N):
        for j in range(N):
            if point_in_square(i, j, main_point, d1_, d2_):
                ans[4] += mp[i][j]
            elif 0 <= i < main_point[0] + d1_ and 0 <= j <= main_point[1]:
                ans[0] += mp[i][j]
            elif 0 <= i <= main_point[0] + d2_ and main_point[1] < j < N:
                ans[1] += mp[i][j]
            elif main_point[0] + d1_ <= i < N and 0 <= j < main_point[1] - d1_ + d2_:
                ans[2] += mp[i][j]
            elif main_point[0] + d2_ < i < N and main_point[1] - d1_ + d2_ <= j < N:
                ans[3] += mp[i][j]
    return ans


mn = sys.maxsize

for first_row in range(1, N - 2):
    for first_col in range(1, N - 1):
        first_point = (first_row, first_col)

        for d1 in range(1, N):
            for d2 in range(1, N):
                second_point = (first_row + d1, first_col - d1)
                third_point = (first_row + d1 + d2, first_col - d1 + d2)
                fourth_point = (first_row + d2, first_col + d2)

                if point_in_board(second_point) and point_in_board(third_point) and point_in_board(fourth_point):
                    lst = find_population(first_point, d1, d2)
                    mn = min(mn, max(lst) - min(lst))

print(mn)
