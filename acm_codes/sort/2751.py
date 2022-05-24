import heapq
import sys

N = int(input())
lst = []
for _ in range(N):
    n = int(sys.stdin.readline())
    heapq.heappush(lst, n)

for i in range(N):
    sys.stdout.write("%d\n" % (heapq.heappop(lst)))
