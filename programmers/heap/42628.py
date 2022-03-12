# 이중 우선순위 큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq


def solution(operations):
    answer = []

    max_heap = []
    min_heap = []

    for i in operations:
        op, num = i.split()
        if op == "I":
            num = int(num)
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        else:
            if len(max_heap) == 0 or len(min_heap) == 0:
                continue
            else:
                if num == "1":
                    tmp = heapq.heappop(max_heap)
                    min_heap.remove(-tmp)
                else:
                    tmp = heapq.heappop(min_heap)
                    max_heap.remove(-tmp)

    if len(min_heap) == 0:
        answer = [0, 0]
    else:
        a1 = heapq.heappop(min_heap)
        a2 = -heapq.heappop(max_heap)
        answer = [a2, a1]

    return answer
