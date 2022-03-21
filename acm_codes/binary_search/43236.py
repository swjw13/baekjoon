# 징검다리
# https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = 0
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    length = len(rocks)

    start = 0
    end = distance

    while True:
        if start > end:
            break
        mid = (start + end) // 2

        count = 1
        cur_pos = 0
        for i in range(len(rocks)):
            if rocks[i] - cur_pos >= mid:
                count += 1
                cur_pos = rocks[i]

        if count == length - n:
            answer = mid
            start = mid + 1
        elif count < length - n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer

a = 48
rocks = [12,25,38,43]
n = 1
print(solution(a, rocks, n))
