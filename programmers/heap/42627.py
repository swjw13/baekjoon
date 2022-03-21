# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq
import math


def solution(jobs):
    jobs.sort(key=lambda x: x[0])

    answer = 0
    length = len(jobs)
    time = 0
    schedule = []
    count = 0

    while True:
        while jobs:
            if jobs[0][0] > time:
                break
            tmp = jobs.pop(0)
            heapq.heappush(schedule, (tmp[1], tmp[0]))

        if len(schedule) == 0:
            time += 1
            continue

        tmp = heapq.heappop(schedule)
        time += tmp[0]
        answer += (time - tmp[1])
        count += 1

        if count == length:
            break
    answer /= length

    return math.floor(answer)

