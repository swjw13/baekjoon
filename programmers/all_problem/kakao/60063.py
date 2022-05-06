# https://programmers.co.kr/learn/courses/30/lessons/60063
# 블록 이동하기

from collections import deque


def solution(board):
    answer = 0
    visited = set()
    length = len(board)

    queue = deque([(0, 0, 0, 1, 0)])
    visited.add((0, 0, 0, 1))

    while queue:
        first_row, first_col, second_row, second_col, turn = queue.popleft()
        first_row, second_row = min(first_row, second_row), max(first_row, second_row)
        first_col, second_col = min(first_col, second_col), max(first_col, second_col)
        
        if (first_row == length - 1 and first_col == length - 1) or (second_row == length - 1 and second_col == length - 1):
            answer = turn
            break

        # 가로 형태일 경우
        if first_row == second_row:
            # 오른쪽
            if second_col + 1 < length and board[first_row][second_col + 1] == 0 and (first_row, first_col+1, second_row, second_col + 1) not in visited:
                visited.add((first_row, first_col+1, second_row, second_col + 1))
                queue.append((first_row, first_col+1, second_row, second_col + 1, turn + 1))
            # 왼쪽
            if first_col - 1 >= 0 and board[first_row][first_col - 1] == 0 and (first_row, first_col - 1, second_row, second_col - 1) not in visited:
                visited.add((first_row, first_col - 1, second_row, second_col - 1))
                queue.append((first_row, first_col - 1, second_row, second_col - 1, turn + 1))

            # 위쪽 확인
            if first_row - 1 >= 0 and board[first_row - 1][first_col] + board[second_row - 1][second_col] == 0:
                # 위 이동
                if (first_row - 1, first_col, second_row - 1, second_col) not in visited:
                    visited.add((first_row - 1, first_col, second_row - 1, second_col))
                    queue.append((first_row - 1, first_col, second_row - 1, second_col, turn + 1))

                if (first_row - 1, first_col + 1, second_row, second_col) not in visited:
                    visited.add((first_row - 1, first_col + 1, second_row, second_col))
                    queue.append((first_row - 1, first_col + 1, second_row, second_col, turn + 1))

                if (second_row - 1, second_col - 1, first_row, first_col) not in visited:
                    visited.add((second_row - 1, second_col - 1, first_row, first_col))
                    queue.append((second_row - 1, second_col - 1, first_row, first_col, turn + 1))

            # 아래쪽 확인
            if first_row + 1 < length and board[first_row + 1][first_col] + board[second_row + 1][second_col] == 0:
                # 아래 이동
                if (first_row + 1, first_col, second_row + 1, second_col) not in visited:
                    visited.add((first_row + 1, first_col, second_row + 1, second_col))
                    queue.append((first_row + 1, first_col, second_row + 1, second_col, turn + 1))
                if (first_row + 1, second_col, second_row, second_col) not in visited:
                    visited.add((first_row + 1, second_col, second_row, second_col))
                    queue.append((first_row + 1, second_col, second_row, second_col, turn + 1))
                if (first_row, first_col, second_row + 1, first_col) not in visited:
                    visited.add((first_row, first_col, second_row + 1, first_col))
                    queue.append((first_row, first_col, second_row + 1, first_col, turn + 1))


        # 세로 형태일 경우
        else:
            if first_row - 1 >= 0 and board[first_row -1][first_col] == 0 and (first_row - 1, first_col, second_row - 1, second_col) not in visited:
                visited.add((first_row - 1, first_col, second_row - 1, second_col))
                queue.append((first_row - 1, first_col, second_row - 1, second_col, turn + 1))

            if second_row + 1 < length and board[second_row + 1][second_col] == 0 and (first_row + 1, first_col, second_row + 1, second_col) not in visited:
                visited.add((first_row + 1, first_col, second_row + 1, second_col))
                queue.append((first_row + 1, first_col, second_row + 1, second_col, turn + 1))

            if first_col + 1 < length and board[first_row][first_col + 1] + board[second_row][second_col + 1] == 0:
                if (first_row, first_col + 1, second_row, second_col + 1) not in visited:
                    visited.add((first_row, first_col + 1, second_row, second_col + 1))
                    queue.append((first_row, first_col + 1, second_row, second_col + 1, turn + 1))
                if (first_row, first_col, second_row - 1, second_col + 1) not in visited:
                    visited.add((first_row, first_col, second_row - 1, second_col + 1))
                    queue.append((first_row, first_col, second_row - 1, second_col + 1, turn + 1))
                if (second_row, second_col,first_row + 1, first_col + 1) not in visited:
                    visited.add((second_row, second_col,first_row + 1, first_col + 1))
                    queue.append((second_row, second_col,first_row + 1, first_col + 1, turn + 1))

            if first_col - 1 >= 0 and board[first_row][first_col - 1] + board[second_row][second_col - 1] == 0:
                if (first_row, first_col - 1, second_row, second_col - 1) not in visited:
                    visited.add((first_row, first_col - 1, second_row, second_col - 1))
                    queue.append((first_row, first_col - 1, second_row, second_col - 1, turn + 1))
                if (second_row - 1, second_col-1, first_row, first_col) not in  visited:
                    visited.add((second_row - 1, second_col-1, first_row, first_col))
                    queue.append((second_row - 1, second_col-1, first_row, first_col, turn + 1))
                if (first_row + 1, first_col - 1, second_row, second_col) not in visited:
                    visited.add((first_row + 1, first_col - 1, second_row, second_col))
                    queue.append((first_row + 1, first_col - 1, second_row, second_col, turn + 1))

    return answer

a = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(a))