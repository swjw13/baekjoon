from collections import deque
import sys

input = sys.stdin.readline

visited = set()


def if_visited(str):
    if str in visited:
        return True
    else:
        return False


def check_visited(str):
    visited.add(str)


board = ""
for _ in range(3):
    board += "".join(input().split())

queue = deque([(board, 0)])
check_visited(board)

turn = -1

while queue:
    tmp = None
    point, t = queue.popleft()

    if point == "123456780":
        turn = t
        break
    point = list(point)
    zero_index = point.index("0")

    # 왼쪽
    if zero_index % 3 != 0:
        point[zero_index], point[zero_index - 1] = point[zero_index - 1], point[zero_index]
        tmp = "".join(point)
        if not if_visited(tmp):
            check_visited(tmp)
            queue.append((tmp, t + 1))
        point[zero_index], point[zero_index - 1] = point[zero_index - 1], point[zero_index]
        tmp = None

    # 오른쪽
    if zero_index % 3 != 2:
        point[zero_index], point[zero_index + 1] = point[zero_index + 1], point[zero_index]
        tmp = "".join(point)
        if not if_visited(tmp):
            check_visited(tmp)
            queue.append((tmp, t + 1))
        point[zero_index], point[zero_index + 1] = point[zero_index + 1], point[zero_index]
        tmp = None

    # 위쪽
    if zero_index // 3 != 0:
        point[zero_index], point[zero_index - 3] = point[zero_index - 3], point[zero_index]
        tmp = "".join(point)
        if not if_visited(tmp):
            check_visited(tmp)
            queue.append((tmp, t + 1))
        point[zero_index], point[zero_index - 3] = point[zero_index - 3], point[zero_index]
        tmp = None

    # 아래쪽
    if zero_index // 3 != 2:
        point[zero_index], point[zero_index + 3] = point[zero_index + 3], point[zero_index]
        tmp = "".join(point)
        if not if_visited(tmp):
            check_visited(tmp)
            queue.append((tmp, t + 1))
        point[zero_index], point[zero_index + 3] = point[zero_index + 3], point[zero_index]
        tmp = None

print(turn)
