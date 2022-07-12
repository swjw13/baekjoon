# https://www.acmicpc.net/problem/1744
# 수 묶기

N = int(input())
pos = []
neg = []
for _ in range(N):
    tmp = int(input())
    if tmp <= 0:
        neg.append(tmp)
    else:
        pos.append(tmp)
pos.sort(reverse=True)
neg.sort()
answer = 0
while len(neg) > 1:
    num1 = neg.pop(0)
    num2 = neg.pop(0)

    if num1 * num2 >= num1 + num2:
        answer += num1 * num2

    else:
        answer += num1 + num2
while len(pos) > 1:
    num1 = pos.pop(0)
    num2 = pos.pop(0)

    if num1 * num2 >= num1 + num2:
        answer += num1 * num2

    else:
        answer += num1 + num2

if len(pos) == 1 and len(neg) == 1:
    print(answer + max(pos[0] * neg[0], pos[0] + neg[0]))
else:
    print(answer + sum(neg) + sum(pos))