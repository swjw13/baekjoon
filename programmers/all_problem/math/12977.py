# 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations


def solution(nums):
    answer = 0

    nums.sort()

    end_num = nums[-1] + nums[-2] + nums[-3]
    primes = [i for i in range(end_num + 1)]

    for i in range(2, end_num // 2 + 1):
        tmp = 2 * i
        while tmp <= end_num:
            primes[tmp] = 0
            tmp += i

    for i in combinations(nums, 3):
        if primes[sum(i)] != 0:
            answer += 1

    return answer
