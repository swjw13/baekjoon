# abs heap

import sys
import heapq

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        if len(lst) == 0:
            print(0)
        else:
            (num, check) = heapq.heappop(lst)
            if check == 0:
                print(-num)
            else:
                print(num)
    else:
        if number >= 0:
            heapq.heappush(lst, (abs(number), 1))
        else:
            heapq.heappush(lst, (abs(number), 0))
