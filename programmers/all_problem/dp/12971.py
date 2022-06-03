# https://programmers.co.kr/learn/courses/30/lessons/12971
# 스티커 모으기

def solution(sticker):
    def find_max(lst, l):
        if l == 1:
            return lst[0]
        else:
            dp = [0 for _ in range(l)]
            dp[0] = lst[0]

            for i in range(1, l):
                dp[i] = max(dp[i - 2] + lst[i], dp[i - 1])
            return dp[l - 1]

    l = len(sticker)
    if l <= 3:
        return max(sticker)
    else:
        tmp1 = find_max(sticker[1:-1], l - 2)
        tmp2 = find_max(sticker[2:-1], l - 3) + sticker[0]
        tmp3 = find_max(sticker[1:-2], l - 3) + sticker[-1]

        return max(tmp1, tmp2, tmp3)


a = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(a))