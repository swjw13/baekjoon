# 타일 채우기
# https://www.acmicpc.net/problem/14852

n = int(input())
l = [[2, 2], [7, 9], [22, 31]]
if n > 3:
    for i in range(3, n):
        c = 2 * l[i - 1][0] + 3 * l[i - 2][0] + 2 * l[i - 3][1] + 2
        s = (l[i - 1][1] + c) % 1_000_000_007
        l.append([c % 1_000_000_007, s])
print(l[n - 1][0])
