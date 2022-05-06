import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = 10 ** 9

n = int(input())
m = int(input())


def floyd_warshal(n):
    distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n):
        distance[i][i] = 0

    # 그래프 정보를 통해 distance를 update
    for _ in range(m):
        start, end, weight = list(map(int, input().split()))
        distance[start][end] = min(weight, distance[start][end])

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != k and j != k:
                    new_dist = distance[i][k] + distance[k][j]
                    if distance[i][j] > new_dist:
                        distance[i][j] = new_dist

    return distance


distance = floyd_warshal(n)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()
