# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860


def solution(name):
    answer = 0
    length = len(name)
    diff_index = []

    for i in range(1, length):
        if name[i] != "A":
            diff_index.append(i)

    width_movement = 0

    if len(diff_index) != 0:
        width_movement = min(diff_index[-1], length - diff_index[0])
        for i in range(len(diff_index) - 1):
            a1 = (length - diff_index[i]) * 2 + diff_index[i + 1]
            a2 = (length - diff_index[i + 1]) * 2 + diff_index[i]
            a3 = diff_index[i] * 2 + (length - diff_index[i + 1])
            a4 = diff_index[i + 1] * 2 + (length - diff_index[i])
            width_movement = min(width_movement, a1, a2, a3, a4)

    answer += width_movement

    for i in name:
        answer += min(ord(i) - ord("A"), ord("Z") - ord(i) + 1)

    return answer


