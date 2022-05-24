# Traveling Salesman Problem
# https://www.acmicpc.net/problem/10971
# https://jjangsungwon.tistory.com/4 에 있는 코드
# 결국 요점은 모든 점들을 방문하고 난 후 마지막 도시에서 첫 번째 도시로 돌아올 수 있는가
# 그리고 그 방법들 중 거리가 최소인 것은 얼마나 되는가 이다

import sys


def dfs(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel[next][start] != 0:
            min_value = min(min_value, value + travel[next][start])
        return

    for i in range(N):
        if travel[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            visited.pop()


if __name__ == "__main__":

    N = int(input())
    travel = [list(map(int, input().split())) for _ in range(N)]

    min_value = sys.maxsize

    # 각 번호에서 시작
    for i in range(N):
        dfs(i, i, 0, [i])

    print(min_value)
