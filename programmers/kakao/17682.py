# https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3
# 다트게임
import re


def solution(dartResult):
    answer = 0

    words = []
    idx = 1
    while idx < len(dartResult):
        if dartResult[idx] in '123456789':
            words.append(dartResult[:idx])
            dartResult = dartResult[idx:]
            idx = 1
        elif (dartResult[idx] == '0') and (dartResult[idx - 1] != '1'):
            words.append(dartResult[:idx])
            dartResult = dartResult[idx:]
            idx = 1
        else:
            idx += 1
    words.append(dartResult)
    numbers = []
    a = [1, 1, 1]

    def extract(turn, word):
        lst = re.findall(r"\d+", word)
        if lst[0] == "10":
            tmp = 10
            if word[2] == "D":
                tmp **= 2
            elif word[2] == "T":
                tmp **= 3
            numbers.append(tmp)

            if len(word) == 4:
                if word[3] == "#":
                    a[turn] *= -1
                else:
                    a[turn] *= 2
                    if turn != 0:
                        a[turn - 1] *= 2

        else:
            tmp = int(lst[0])
            if word[1] == "D":
                tmp **= 2
            elif word[1] == "T":
                tmp **= 3
            numbers.append(tmp)

            if len(word) == 3:
                if word[2] == "#":
                    a[turn] *= -1
                else:
                    a[turn] *= 2
                    if turn != 0:
                        a[turn - 1] *= 2

    # first
    extract(0, words[0])
    # second
    extract(1, words[1])
    # third
    extract(2, words[2])

    for i in range(3):
        answer += a[i] * numbers[i]

    return answer

a = '1S2D*3T'
print(solution(a))