import heapq

a = []
heapq.heappush(a, 3)
heapq.heappush(a, 2)
ans = heapq.heappop(a)
print(ans)  # 2
