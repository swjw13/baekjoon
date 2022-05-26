# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque
import sys


def solution(n, edge):
    connected = {i: [] for i in range(1, n + 1)}
    for lines in edge:
        connected[lines[0]].append(lines[1])
        connected[lines[1]].append(lines[0])

    distance = [10 ** 6 for i in range(n + 1)]
    queue = deque([(1, 0)])
    distance[1] = 0

    while queue:
        cur_point, cur_dist = queue.popleft()
        for connected_points in connected[cur_point]:
            new_dist = cur_dist + 1
            if new_dist < distance[connected_points]:
                queue.append((connected_points, new_dist))
                distance[connected_points] = new_dist

    distance[0] = 0
    max_dist = max(distance)
    answer = distance.count(max_dist)

    return answer
