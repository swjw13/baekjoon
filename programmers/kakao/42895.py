# https://programmers.co.kr/learn/courses/30/lessons/42895
# N으로 표현
# 카카오

from collections import defaultdict


def solution(N, number):
    dp = defaultdict(set)
    for i in range(1, 9):
        if number == int(str(N) * i):
            return i
        else:
            dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for tmp1 in dp[j]:
                for tmp2 in dp[i - j]:
                    add = tmp1 + tmp2
                    sub = abs(tmp1 - tmp2)
                    mul = tmp1 * tmp2
                    div = max(tmp1, tmp2) // min(tmp1, tmp2)

                    if number in {add, sub, mul, div}:
                        return i
                    else:
                        dp[i].add(add)
                        dp[i].add(mul)
                        if sub > 0:
                            dp[i].add(sub)
                        if div > 0:
                            dp[i].add(div)
    return -1
