# 차이를 최대로
# https://www.acmicpc.net/problem/10819
# 결국에는 순열 문제

from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))


def get_distance(indexes, length):
    ans = 0
    for i in range(length - 1):
        ans += abs(indexes[i] - indexes[i + 1])
    return ans


mx = 0
for i in permutations(lst, N):
    mx = max(mx, get_distance(i, N))

print(mx)
