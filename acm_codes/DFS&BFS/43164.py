# 여행 경로
# https://programmers.co.kr/learn/courses/30/lessons/43164

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def solution(tickets):
    answer = []
    connected = dict()
    for start, end in tickets:
        if start in connected.keys():
            connected[start].append(end)
        else:
            connected[start] = [end]

    queue = deque([("ICN", ["ICN"], 0)])

    while queue:
        cur_city, prev, ticket_count = queue.popleft()

        if ticket_count == len(tickets):
            if len(answer) == 0:
                answer = prev
            else:
                if prev < answer:
                    answer = prev
        else:
            if cur_city in connected.keys():
                for con_city in connected[cur_city]:
                    prev_length = len(prev)
                    tmp = 0
                    for i in range(prev_length - 1):
                        if prev[i] == cur_city and prev[i + 1] == con_city:
                            tmp += 1
                    if tmp != connected[cur_city].count(con_city):
                        queue.append((con_city, prev + [con_city], ticket_count + 1))

    return answer


a = [["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "BOO"], ["BOO", "AOO"],
     ["BOO", "FOO"], ["FOO", "COO"], ["COO", "ZOO"]]
print(solution(a))
