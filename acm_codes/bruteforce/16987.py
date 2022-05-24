# 계란으로 계란치기
# https://www.acmicpc.net/problem/16987

import sys

input = sys.stdin.readline

N = int(input())
weights = []
strengths = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    strengths.append(a)
    weights.append(b)

ans = 0


def egging(current_index):
    global ans
    if current_index == N:
        cnt = 0
        for num in strengths:
            if num <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return

    if strengths[current_index] <= 0:
        egging(current_index + 1)
    else:
        for i in range(N):
            if i == current_index:
                if i == N - 1:
                    egging(i + 1)
                    return
                else:
                    continue
            if strengths[i] <= 0:
                if i == N - 1:
                    egging(current_index + 1)
                    return
                else:
                    continue
            strengths[current_index] -= weights[i]
            strengths[i] -= weights[current_index]
            egging(current_index + 1)
            strengths[current_index] += weights[i]
            strengths[i] += weights[current_index]


egging(0)
print(ans)
