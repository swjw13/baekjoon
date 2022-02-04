# 이전 순열
# https://www.acmicpc.net/problem/10973
# 이산 수학 에서 배운 순열, 조합 순서 구하는 문제인데 조금 변형된 모습

import sys
input = sys.stdin.readline

N = int(input())
target = list(map(int, input().split()))

pivot_index = N - 2
while target[pivot_index] < target[pivot_index + 1]:
    pivot_index -= 1

if pivot_index == -1:
    print(-1)
else:
    index_for_change = N - 1
    while target[index_for_change] > target[pivot_index]:
        index_for_change -= 1

    target[pivot_index], target[index_for_change] = target[index_for_change], target[pivot_index]

    target = target[:pivot_index + 1] + sorted(target[pivot_index + 1:], reverse=True)

    for i in target:
        print(i, end=' ')
