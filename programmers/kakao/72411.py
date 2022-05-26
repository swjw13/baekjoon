# 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411
# kakao 2021

from itertools import combinations


def solution(orders, course):
    answer = []

    prev_menues = {i: dict() for i in range(2, 11)}

    for i in orders:
        length = len(i)

        for sub_length in range(2, length + 1):
            for j in combinations(i, sub_length):
                j = list(j)
                j.sort()
                sub_menu = "".join(j)
                if sub_menu in prev_menues[sub_length].keys():
                    prev_menues[sub_length][sub_menu] += 1
                else:
                    prev_menues[sub_length][sub_menu] = 1

    for i in course:
        if len(prev_menues[i].keys()) == 0:
            continue
        else:
            max_count = max(prev_menues[i].values())
            if max_count == 1:
                continue
            else:
                for key, value in prev_menues[i].items():
                    if value == max_count:
                        answer.append(key)

    answer.sort()

    return answer
