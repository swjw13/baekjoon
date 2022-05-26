# https://programmers.co.kr/learn/courses/30/lessons/12952
# n-queen
def able(col, prev):
    unable = set()
    for i in range(len(prev)):
        r = prev[i]
        unable.add(r)
        unable.add(r + i - col)
        unable.add(r - i + col)
    return list(unable)


c = 0


def nQueen(N, current_col, previous):
    global c
    if current_col == N:
        c += 1
    else:
        un = able(current_col, previous)
        ab = [i for i in range(N) if i not in un]
        for i in ab:
            nQueen(N, current_col + 1, previous + [i])


def solution(n):
    nQueen(n, 0, [])
    return c


a = 4
print(solution(a))
