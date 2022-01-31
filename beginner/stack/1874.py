# 스택 수열

import sys

success = -1

N = int(sys.stdin.readline())
given = []
for _ in range(N):
    given.append(int(sys.stdin.readline()))

stack = [1]
answer = ['+']
lst = [i for i in range(2, N + 1)]

while True:
    if len(given) == 0:
        success = 1
        break

    n = given.pop(0)
    if len(stack) == 0:
        value = lst.pop(0)
        stack.append(value)
        answer.append("+")

    while stack[-1] < n:
        value = lst.pop(0)
        stack.append(value)
        answer.append("+")

    if stack[-1] > n:
        success = -1
        break

    stack.pop()
    answer.append("-")

if success == 1:
    for i in answer:
        print(i)
else:
    print("NO")