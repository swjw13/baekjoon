# https://programmers.co.kr/learn/courses/30/lessons/12942
# 최적의 행렬 곱셈
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
INF = 10 ** 6


def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for i in range(1, n):
        for start in range(n):
            end = start + i

            if end >= n:
                break
            for fixed in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][fixed] + dp[fixed + 1][end] + (
                        matrix_sizes[start][0] * matrix_sizes[fixed + 1][0] * matrix_sizes[end][1]))

    return dp[0][n - 1]


q = [[5, 3], [3, 10], [10, 6]]
print(solution(q))
