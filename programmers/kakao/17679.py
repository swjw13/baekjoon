from collections import defaultdict


def solution(m, n, board):
    answer = 0

    lst = [[] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            lst[j] = [board[i][j]] + lst[j]

    while True:
        changed = False
        points_for_change = defaultdict(set)
        for i in range(n - 1):
            for j in range(m - 1):
                if "-" not in lst[i][j] + lst[i][j + 1] + lst[i + 1][j] + lst[i + 1][j + 1]:
                    tmp = set()
                    tmp.add(lst[i][j])
                    tmp.add(lst[i][j + 1])
                    tmp.add(lst[i + 1][j])
                    tmp.add(lst[i + 1][j + 1])
                    if len(tmp) == 1:
                        points_for_change[i].update({j, j + 1})
                        points_for_change[i + 1].update({j, j + 1})
                        changed = True

        if not changed:
            break
        else:
            for col in range(n):
                row_changed = list(points_for_change[col])
                row_changed.sort(reverse=True)
                for rows in row_changed:
                    lst[col].pop(rows)
                    lst[col].append("-")
                    answer += 1

    return answer


m = 6
n = 6
b = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, b))
