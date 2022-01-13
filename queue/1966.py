# 프린터

from collections import deque
import heapq

T = int(input())
for _ in range(T):
    turn = 1
    heap = []

    N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    lst2 = []

    for i in range(len(lst)):
        if i == M:
            lst2.append((lst[i], 1))
        else:
            lst2.append((lst[i], 0))
        heapq.heappush(heap, -lst[i])
    que = deque(lst2)

    while True:
        value = -heapq.heappop(heap)

        while True:
            val2 = que.popleft()
            if value == val2[0]:
                break
            else:
                que.append(val2)

        if val2[1] == 1:
            print(turn)
            break
        else:
            turn += 1