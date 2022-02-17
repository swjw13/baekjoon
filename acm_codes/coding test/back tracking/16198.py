# 에너지 모으기
# https://www.acmicpc.net/problem/16198

import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
energies = list(map(int, input().split()))
mx = 0
for i in permutations([i for i in range(1, N - 1)], N - 2):
    energy = 0
    index_to_get_energy = [energies[i] for i in range(N)]
    for index in i:
        index_to_get_energy[index] = 0
        tmp1 = index - 1
        tmp2 = index + 1
        while index_to_get_energy[tmp1] == 0:
            tmp1 -= 1
        while index_to_get_energy[tmp2] == 0:
            tmp2 += 1
        energy += index_to_get_energy[tmp1] * index_to_get_energy[tmp2]
    mx = max(mx, energy)

print(mx)
