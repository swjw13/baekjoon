# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
# kakao 2020

def solution(key, lock):
    answer = True

    M = len(key)
    N = len(lock)
    keys = [key,
            [[-1 for _ in range(M)] for _ in range(M)],
            [[-1 for _ in range(M)] for _ in range(M)],
            [[-1 for _ in range(M)] for _ in range(M)]]
    whole_count = 0
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                whole_count += 1

    for i in range(M):
        for j in range(M):
            keys[1][j][M - i - 1] = key[i][j]
            keys[2][M - 1 - i][M - 1 - j] = key[i][j]
            keys[3][M - j - 1][i] = key[i][j]

    for row_base in range(-M, N):
        for col_base in range(-M, N):
            for i in range(4):
                flatten_count = 0
                total_count = 0
                start_row = max(0, row_base)
                start_col = max(0, col_base)
                end_row = min(N, row_base + M)
                end_col = min(N, col_base + M)
                for row in range(start_row, end_row):
                    for col in range(start_col, end_col):
                        if keys[i][row - row_base][col - col_base] == 0 and lock[row][col] == 1:
                            total_count += 1
                        elif keys[i][row - row_base][col - col_base] == 1 and lock[row][col] == 0:
                            flatten_count += 1
                if flatten_count == whole_count and total_count + flatten_count == (end_col - start_col) * (
                        end_row - start_row):
                    return True

    return False


a = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
b = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(a, b))
