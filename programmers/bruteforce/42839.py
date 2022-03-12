# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


def solution(numbers):
    def find_prime(num):
        check = 0
        if num == 1:
            return False
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                check += 1
        if check == 1:
            return True
        else:
            return False

    answer = set()
    length = len(numbers)
    for l in range(1, length + 1):
        for i in permutations(numbers, l):
            number = int("".join(i))
            if find_prime(number):
                answer.add(number)
    print(answer)
    return len(answer)

a = "011"
print(solution(a))