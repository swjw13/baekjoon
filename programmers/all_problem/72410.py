# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410
import re


def solution(new_id):
    # answer = ''
    answer = str(new_id)

    answer = answer.lower()

    idx = 0
    while idx < len(answer):
        if answer[idx].isalpha() or answer[idx] in [str(i) for i in range(10)] or answer[idx] in ["-", "_", "."]:
            idx += 1
        else:
            answer = answer[:idx] + answer[idx + 1:]

    while True:
        tmp = answer.find("..")
        if tmp == -1:
            break
        else:
            answer = answer.replace("..", ".")

    if answer.startswith("."):
        answer = answer[1:]
    if answer.endswith("."):
        answer = answer[:-1]

    if len(answer) == 0:
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]
    while answer.endswith("."):
        answer = answer[:-1]

    if len(answer) <= 2:
        while len(answer) <= 2:
            answer += answer[-1]

    return answer

