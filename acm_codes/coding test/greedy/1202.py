import sys
import heapq

input = sys.stdin.readline

N, K = list(map(int, input().split()))

jewels = []
bags = []
for _ in range(N):
    jewels.append(list(map(int, input().split())))
for _ in range(K):
    bags.append(int(input()))

jewels.sort(key=lambda x: x[0])
bags.sort()

queue = []
ans = 0

i = 0
for b in bags:
    while i < N and jewels[i][0] <= b:
        heapq.heappush(queue, -jewels[i][1])
        i += 1
    if len(queue) != 0:
        prev = heapq.heappop(queue)
        ans += -prev

print(ans)
