# https://www.acmicpc.net/problem/1715
# 카드 정렬하기

import sys
import heapq
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    heapq.heappush(numbers, int(input()))

answer = 0
while len(numbers) > 1:
    num1 = heapq.heappop(numbers)
    num2 = heapq.heappop(numbers)

    answer += num1 + num2
    heapq.heappush(numbers, num1 + num2)

print(answer)