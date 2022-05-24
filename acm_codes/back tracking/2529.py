# 부등호 숫자
# https://www.acmicpc.net/problem/2529

import sys

input = sys.stdin.readline

K = int(input())
Ks = input().split()
numbers = [i for i in range(10)]
visited = [False for _ in range(10)]

mx = "0"
mn = str(sys.maxsize)


def find_number(index, number, prev_number):
    global mx, mn
    if index == K:
        if int(mx) < int(number):
            mx = number
        if int(mn) > int(number):
            mn = number
    else:
        current_op = Ks[index]
        for i in range(10):
            if not visited[i]:
                if current_op == "<":
                    if prev_number < numbers[i]:
                        visited[i] = True
                        find_number(index + 1, number + str(numbers[i]), numbers[i])
                        visited[i] = False
                else:
                    if prev_number > numbers[i]:
                        visited[i] = True
                        find_number(index + 1, number + str(numbers[i]), numbers[i])
                        visited[i] = False


for i in range(10):
    visited[i] = True
    find_number(0, str(i), i)
    visited[i] = False
print(mx)
print(mn)
