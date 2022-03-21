# H-index
# https://programmers.co.kr/learn/courses/30/lessons/42747
from bisect import bisect_left, bisect_right


def solution(citations):
    answer = 0

    citations.sort()
    total = len(citations)
    for i in range(10001):
        left = bisect_left(citations, i)
        right = bisect_right(citations, i)

        if right <= i <= total - left:
            answer = i

    return answer
