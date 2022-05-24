# 모둔 순열 구하기
# https://www.acmicpc.net/problem/10974

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
lst = [i for i in range(1, N + 1)]

for i in permutations(lst, N):
    for j in i:
        print(j, end=' ')
    print()