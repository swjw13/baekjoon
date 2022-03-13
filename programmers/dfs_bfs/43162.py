# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def bfs(start_index):
        visited[start_index] = True
        queue = deque([start_index])
        while queue:
            cur_pos = queue.popleft()
            for connected_point, val in enumerate(computers[cur_pos]):
                if val == 1 and not visited[connected_point]:
                    visited[connected_point] = True
                    queue.append(connected_point)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer

