# 요세푸스 문제

from collections import deque

N, K = list(map(int, input().split()))

que = deque([i for i in range(1, N + 1)])
ans = []
turn = 1
while que:
    value = que.popleft()
    if turn == K:
        ans.append(value)
        turn = 0
    else:
        que.append(value)
    turn += 1

print("<", end="")
for i in range(N - 1):
    print("{}, ".format(ans[i]), end="")
print("{}>".format(ans[N - 1]))
