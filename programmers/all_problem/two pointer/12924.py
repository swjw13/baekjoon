# https://programmers.co.kr/learn/courses/30/lessons/12924
# 숫자의 표현

def solution(n):
    answer = 0

    lst = [i for i in range(n + 1)]
    start = 1
    end = 1
    total = 1
    while (end <= n) and (start <= n):
        
        if start > end:
            break

        if total == n:
            answer += 1
            total -= lst[start]
            start += 1
            end += 1
            if end <= n:
                total += lst[end]
        elif total < n:
            end += 1
            if end <= n:
                total += lst[end]
        else:
            total -= lst[start]
            start += 1

    return answer

n = 15
print(solution(n))