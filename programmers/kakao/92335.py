# https://programmers.co.kr/learn/courses/30/lessons/92335
# 소수 구하기

def solution(n, k):
    answer = 0

    def getPrime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # prime = getPrime(10 ** 7)

    num_to_str = ""
    while n > 0:
        tmp = n % k
        num_to_str = str(tmp) + num_to_str
        n //= k

    a = num_to_str.split("0")
    for dec in a:
        if len(dec) > 0:
            if getPrime(int(dec)):
                answer += 1
    return answer


a = 437674
k = 3
print(solution(a, k))
