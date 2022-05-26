# 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    length = len(nums)
    nums = set(nums)

    if len(nums) > length // 2:
        answer = length // 2
    else:
        answer = len(nums)

    return answer
