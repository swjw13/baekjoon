# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []

    matched_number = 0
    num_zeros = 0
    for i in lottos:
        if i != 0:
            if i in win_nums:
                win_nums.remove(i)
                matched_number += 1
        else:
            num_zeros += 1

    if matched_number == 0:
        if num_zeros <= 1:
            answer = [6, 6]
        else:
            answer = [6 - num_zeros + 1, 6]
    else:
        answer = [6 - matched_number + 1 - num_zeros, 6 - matched_number + 1]

    return answer
