# https://programmers.co.kr/learn/courses/30/lessons/12927
# 야근 지수

def solution(n, works):
    answer = 0

    start = 0
    end = max(works)

    if sum(works) <= n:
        return 0
    else:

        while start <= end:
            mid = (start + end) // 2
            tmp = 0
            for i in works:
                if i >= mid:
                    tmp += (i - mid)
            if tmp == n:
                for i in works:
                    if i >= mid:
                        answer += mid ** 2
                    else:
                        answer += i ** 2
                return answer
            elif tmp < n:
                end = mid - 1
            else:
                start = mid + 1

        remain = n
        for i in works:
            if i >= start:
                remain -= (i - start)
        print(start)

        for i in works:
            if i >= start:
                tmp = start
                if remain > 0:
                    tmp -= 1
                    remain -= 1
                answer += tmp ** 2
            else:
                answer += i ** 2
        return answer

a = 3
b = [1,1]
print(solution(a, b))