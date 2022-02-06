# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

import sys
from itertools import permutations

input = sys.stdin.readline
a = ['+', '-', '*', '/']

N = int(input())
numbers = list(map(int, input().split()))

yun = list(map(int, input().split()))
checks = []
for i in range(4):
    checks += [a[i]] * yun[i]

max_num = -sys.maxsize
min_num = sys.maxsize
indexes = [i for i in range(N - 1)]
for i in permutations(indexes, N - 1):
    index = 0
    ans = numbers[0]
    while index < N - 1:
        tmp = i[index]
        index += 1
        if checks[tmp] == "+":
            ans += numbers[index]
        elif checks[tmp] == "-":
            ans -= numbers[index]
        elif checks[tmp] == "*":
            ans *= numbers[index]
        else:
            if ans >= 0:
                ans = ans // numbers[index]
            else:
                ans = -((-ans) // numbers[index])
    max_num = max(max_num, ans)
    min_num = min(min_num, ans)

print(max_num)
print(min_num)
