# 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302
# 2021 kakao

from collections import deque

dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(places):
    answer = []

    for place in places:
        ans = 1
        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P':
                    is_good = True
                    queue = deque([(row, col, 0)])
                    visited = [[False for _ in range(5)] for _ in range(5)]
                    visited[row][col] = True

                    while queue:
                        cur_row, cur_col, cur_dist = queue.popleft()

                        if place[cur_row][cur_col] == "P" and 1 <= cur_dist <= 2:
                            is_good = False
                            break

                        if cur_dist <= 1:
                            for dx, dy in dxdy:
                                new_row = cur_row + dx
                                new_col = cur_col + dy
                                if 0 <= new_row < 5 and 0 <= new_col < 5 and not visited[new_row][new_col] and \
                                        place[new_row][new_col] != "X":
                                    queue.append((new_row, new_col, cur_dist + 1))
                                    visited[new_row][new_col] = True

                    if not is_good:
                        ans = 0
        answer.append(ans)

    return answer


a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(a))
