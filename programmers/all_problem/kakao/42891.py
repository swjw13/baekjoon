# 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891
# kakao 2019
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    else:
        start = 1
        end = max(food_times)
        while True:
            mid = (start + end) // 2
            count = 0
            min_count = 0

            for i in food_times:
                if mid <= i:
                    min_count += 1
                    count += mid
                else:
                    count += i

            if count == k:
                idx = 0
                while food_times[idx] <= mid:
                    idx += 1
                return idx + 1

            elif count < k:
                start = mid + 1

            else:
                if count - min_count < k:
                    k -= (count - min_count)
                    idx = 0
                    while k > -1:
                        if food_times[idx] >= mid:
                            k -= 1
                        idx += 1
                    return idx

                else:
                    end = mid - 1

