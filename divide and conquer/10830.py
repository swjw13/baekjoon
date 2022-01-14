# 행렬의 거듭제곱

import sys


def twotwo(lst1, lst2, N):
    ans = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(N):
                total += lst1[i][k] * lst2[k][j] % 1000
            ans[i].append(total)
    return ans


def mat(matrix, num, N):
    if num == 1:
        return matrix
    else:
        one = mat(matrix, num // 2, N)
        tmp = twotwo(one, one, N)

        if num % 2 == 0:
            return tmp
        else:
            return twotwo(tmp, matrix, N)


N, B = list(map(int, sys.stdin.readline().split()))
m = []
for _ in range(N):
    m.append(list(map(int, sys.stdin.readline().split())))

ans = mat(m, B, N)

for i in ans:
    for j in i:
        print(j % 1000, end=' ')
    print()
