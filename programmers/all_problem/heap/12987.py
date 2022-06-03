# https://programmers.co.kr/learn/courses/30/lessons/12987
# 숫자 게임

import heapq


def solution(A, B):
    answer = 0

    heapq.heapify(A)
    heapq.heapify(B)

    while A and B:
        a = heapq.heappop(A)
        b = heapq.heappop(B)

        if a > b:
            heapq.heappush(A, a)
        elif a == b:
            heapq.heappush(A, a)
        else:
            answer += 1

    return answer
