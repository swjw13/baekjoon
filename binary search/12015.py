# LIS with DP

from bisect import bisect_left

N = int(input())
lst = list(map(int, input().split()))

dp = [lst.pop(0)]
for i in lst:
    if i > dp[-1]:
        dp.append(i)
    else:
        idx = bisect_left(dp, i)
        dp[idx] = i
print(len(dp))
