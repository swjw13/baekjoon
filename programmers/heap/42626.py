# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    scoville.sort()
    answer = 0
    tmp = False

    while scoville:
        a = heapq.heappop(scoville)
        if a >= K:
            tmp = True
            break
        elif len(scoville) == 0:
            break
        else:
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + 2 * b)
            answer += 1

    if len(scoville) == 0:
        if not tmp:
            answer = -1

    return answer

