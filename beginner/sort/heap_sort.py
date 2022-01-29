import heapq

lst = []

for i in range(10,0,-1):
    heapq.heappush(lst, i)

for i in range(10):
    print(heapq.heappop(lst))
