# 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

from collections import deque


def solution(n, results):
    answer = 0

    total = [[set(), set()] for i in range(n + 1)]
    for win, lose in results:
        total[win][1].add(lose)
        total[lose][0].add(win)

    for i in range(1, n + 1):
        if len(total[i][0].union(total[i][1])) == n:
            answer += 1
        else:
            low_count = set()
            queue = deque([i])
            while queue:
                point = queue.popleft()
                low_count.add(point)
                for con_point in total[point][1]:
                    if con_point not in low_count:
                        queue.append(con_point)
            high_count = set()
            queue = deque([i])
            while queue:
                point = queue.popleft()
                high_count.add(point)
                for con_point in total[point][0]:
                    if con_point not in high_count:
                        queue.append(con_point)
            if len(low_count.union(high_count)) == n:
                answer += 1

    return answer


a = 5
b = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(a, b))
