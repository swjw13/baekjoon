# 로마 숫자 만들기
# https://www.acmicpc.net/problem/16922

from itertools import combinations_with_replacement
import sys

input = sys.stdin.readline

N = int(input())
romans = [1, 5, 10, 50]
decimals = set()

for i in combinations_with_replacement(romans, N):
    decimals.add(sum(i))

print(len(decimals))
