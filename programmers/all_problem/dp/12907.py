# https://programmers.co.kr/learn/courses/30/lessons/12907
# 거스름돈

def solution(n, money):
    money.sort()
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    for i in money:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]


a = 5
b = [1, 2, 5]
print(solution(a, b))