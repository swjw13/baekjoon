# https://www.acmicpc.net/problem/1269
# 대칭차집합

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = set()
ans = ans.union(A.difference(B))
ans = ans.union(B.difference(A))

print(len(ans))