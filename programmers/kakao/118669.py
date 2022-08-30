# https://school.programmers.co.kr/learn/courses/30/lessons/118669
# 등산코스 정하기

import sys
from collections import defaultdict, deque


def solution(n, paths, gates, summits):
    max_size = 11500000
    ans = [-1, max_size]
    lines = dict()
    for i in range(1, n + 1):
        lines[i] = defaultdict(int)

    for p1, p2, dist in paths:
        lines[p1][p2] = dist
        lines[p2][p1] = dist

    summits = set(summits)
    heap = deque()
    intensity = [max_size for _ in range(n + 1)]

    for i in gates:
        for connected in lines[i].keys():
            heap.append((lines[i][connected], connected))
            intensity[connected] = min(lines[i][connected], intensity[connected])

    while heap:
        cur_dist, cur_point = heap.popleft()

        if cur_point in summits:
            if (cur_dist < ans[1]) or (cur_dist == ans[1] and cur_point < ans[0]):
                ans = [cur_point, max(intensity[cur_point], cur_dist)]
            continue

        for i in lines[cur_point].keys():
            if intensity[i] > max(lines[cur_point][i], cur_dist):
                intensity[i] = max(lines[cur_point][i], cur_dist)
                heap.append((max(lines[cur_point][i], cur_dist), i))

    return ans
