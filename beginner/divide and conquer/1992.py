# 쿼드 트리

import sys
sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline())
pic = []
for _ in range(N):
    line = list(map(int, list(input())))
    pic.append(line)


def check(row_start, row_end, col_start, col_end):
    value = pic[row_start][col_start]
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if pic[i][j] != value:
                return False, "-1"
    return True, str(value)


def quad(row_start, row_end, col_start, col_end):
    what, val = check(row_start, row_end, col_start, col_end)
    if what:
        return val
    what1, val1 = check(row_start, (row_start + row_end) // 2, col_start, (col_end + col_start) // 2)
    what2, val2 = check((row_start + row_end) // 2, row_end, col_start, (col_end + col_start) // 2)
    what3, val3 = check(row_start, (row_start + row_end) // 2, (col_end + col_start) // 2, col_end)
    what4, val4 = check((row_start + row_end) // 2, row_end, (col_end + col_start) // 2, col_end)
    if not what1:
        val1 = quad(row_start, (row_start + row_end) // 2, col_start, (col_end + col_start) // 2)
    if not what2:
        val2 = quad((row_start + row_end) // 2, row_end, col_start, (col_end + col_start) // 2)
    if not what3:
        val3 = quad(row_start, (row_start + row_end) // 2, (col_end + col_start) // 2, col_end)
    if not what4:
        val4 = quad((row_start + row_end) // 2, row_end, (col_end + col_start) // 2, col_end)

    return "(" + val1 + val3 + val2 + val4 + ")"


print(quad(0, N, 0, N))
