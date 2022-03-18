# 기능 개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        count = 0
        while len(progresses) > 0 and progresses[0] >= 100:
            count += 1
            progresses.popleft()
            speeds.popleft()
        if count != 0:
            answer.append(count)

    return answer

a =[95, 90, 99, 99, 80, 99]
b =[1, 1, 1, 1, 1, 1]
print(solution(a, b))
