# 입국 심사
# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0

    start = 0
    end = 10 ** 18
    while True:
        if start > end:
            break
        mid = (start + end) // 2

        tmp = 0
        for i in times:
            tmp += mid // i

        if tmp >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


n = 10
t = [6, 8, 10]
print(solution(n, t))


