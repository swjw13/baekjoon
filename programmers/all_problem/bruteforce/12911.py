# https://programmers.co.kr/learn/courses/30/lessons/12911
# 다음 큰 숫자

def solution(n):
    def get_one_count(n):
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n //= 2
        return count

    default_count = get_one_count(n)
    n += 1
    while True:
        if get_one_count(n) == default_count:
            return n
        else:
            n += 1

