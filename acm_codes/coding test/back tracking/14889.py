# 스타트와 링크
# https://www.acmicpc.net/problem/14889

from itertools import combinations
import sys
input = sys.stdin.readline

mp = []
N = int(input())
for i in range(N):
    mp.append(list(map(int, input().split())))
    for j in range(i):
        mp[j][i] += mp[i][j]

members = [i for i in range(N)]

mn = sys.maxsize


for i in combinations(members, N // 2):
    teamA = set(i)
    teamB = set(members) - teamA

    tmp = 0
    for j in combinations(teamA, 2):
        tmp += mp[j[0]][j[1]]
    for j in combinations(teamB, 2):
        tmp -= mp[j[0]][j[1]]

    mn = min(mn, abs(tmp))

print(mn)