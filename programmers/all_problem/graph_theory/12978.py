# https://programmers.co.kr/learn/courses/30/lessons/12978
# 배달

from collections import defaultdict
import heapq

INF = 10 ** 9


def solution(N, road, K):
    answer = 0

    connection = defaultdict(dict)
    for p1, p2, w in road:
        if p2 in connection[p1].keys():
            connection[p1][p2] = min(connection[p1][p2].w)
        else:
            connection[p1][p2] = w

        if p1 in connection[p2].keys():

            connection[p2][p1] = min(connection[p2][p1], w)
        else:
            connection[p2][p1] = w

    distance = {i: INF for i in range(1, N + 1)}
    distance[1] = 0
    heap = [[distance[1], 1]]

    while heap:
        cur_dis, cur_point = heapq.heappop(heap)

        if cur_dis > distance[cur_point]:
            continue

        for con_point in connection[cur_point].keys():
            new_dist = cur_dis + connection[cur_point][con_point]
            if new_dist < distance[con_point]:
                distance[con_point] = new_dist
                heapq.heappush(heap, [new_dist, con_point])

    print(distance)

    for i in distance.keys():
        if distance[i] <= K:
            answer += 1

    return answer


a = 5
b = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
c = 3
print(solution(a, b, c))
