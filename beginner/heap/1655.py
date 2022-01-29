# heap문제 중 중간값을 다루는 문제가 있을 때는
# min, max 둘다 생각해보자

import sys
import heapq

N = int(sys.stdin.readline())
minheap = []
maxheap = []

for i in range(1, N + 1):
    number = int(sys.stdin.readline())
    heapq.heappush(minheap, (number, number))
    heapq.heappush(maxheap, (-number, number))

    a = heapq.heappop(minheap)[0]
    b = heapq.heappop(maxheap)[0]

    heapq.heappush(minheap, (-b, -b))
    heapq.heappush(maxheap, (-a, a))

    print(maxheap[0][1])