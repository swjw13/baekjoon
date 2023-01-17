# AcmCraft
# https://www.acmicpc.net/problem/1005

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(point: int, in_line: dict, time: list, dp_table: dict):
    if len(in_line[point]) == 0:
        dp_table[point] = time[point - 1]
        return time[point - 1]

    prev_length = 0
    for connected in in_line[point]:
        if connected not in dp_table.keys():
            dp_table[connected] = dfs(connected, in_line, time, dp_table)
        prev_length = max(prev_length, dp_table[connected])
    return prev_length + time[point - 1]


T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    times = list(map(int, input().split()))

    in_lines = {i: set() for i in range(1, N + 1)}
    dp = dict()
    for _ in range(K):
        start, end = list(map(int, input().split()))
        in_lines[end].add(start)
    end_point = int(input())
    print(dfs(end_point, in_lines, times, dp))
