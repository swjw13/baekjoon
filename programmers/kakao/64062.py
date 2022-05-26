# https://programmers.co.kr/learn/courses/30/lessons/64062
# 징검다리 건너기
# kakao 2019

def solution(stones, k):
    answer = max(stones)

    length = len(stones)

    start = 1
    end = answer
    while start <= end:
        mid = (start + end) // 2
        count = 0
        tmp = False
        for i in range(length):
            if stones[i] <= mid:
                count += 1
            else:
                if count >= k:
                    tmp = True
                    break
                else:
                    count = 0
        if count >= k:
            tmp = True

        if tmp:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


a = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
b = 3
print(solution(a, b))
