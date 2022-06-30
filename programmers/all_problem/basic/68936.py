# https://programmers.co.kr/learn/courses/30/lessons/68936
# 쿼드 후 세기
def solution(arr):
    answer = [0, 0]
    length = len(arr)

    def find(start_row, start_col, end_row, end_col, n):
        if n == 1:
            if arr[start_row][start_col] == 1:
                answer[1] += 1
                return 1
            else:
                answer[0] += 1
                return 0
        else:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            a1 = find(start_row, start_col, mid_row, mid_col, n // 2)
            a2 = find(start_row, mid_col, mid_row, end_col, n // 2)
            a3 = find(mid_row, start_col, end_row, mid_col, n // 2)
            a4 = find(mid_row, mid_col, end_row, end_col, n // 2)

            if a1 == 1 and a2 == 1 and a3 == 1 and a4 == 1:
                answer[1] -= 3
                return 1
            elif a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0:
                answer[0] -= 3
                return 0
            else:
                return -1

    find(0, 0, length, length, length)

    return answer

a = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(a))