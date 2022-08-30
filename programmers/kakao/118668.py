# https://school.programmers.co.kr/learn/courses/30/lessons/118668
import heapq


def solution(alp, cop, problems: list):
    max_alp = 0
    max_cop = 0
    for i in problems:
        max_alp = max(max_alp, i[0])
        max_cop = max(max_cop, i[1])

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    distance = [[250 for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    distance[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                distance[i + 1][j] = min(distance[i + 1][j], distance[i][j] + 1)
            if j + 1 <= max_cop:
                distance[i][j + 1] = min(distance[i][j + 1], distance[i][j] + 1)

            for prev in problems:
                if prev[0] <= i and prev[1] <= j:
                    distance[min(max_alp, i + prev[2])][min(max_cop, j + prev[3])] = min(distance[min(max_alp, i + prev[2])][min(max_cop, j + prev[3])],
                                                                                         distance[i][j] + prev[4])
    return distance[-1][-1]


a = 0
b = 0
c = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
print(solution(a, b, c))