# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065
# kakao 2019

def solution(s):
    answer = []
    numbers = []
    tmp = 0
    for i in range(len(s)):
        if s[i] == "{":
            tmp = i
        elif s[i] == "}":
            if tmp != 0:
                numbers_str = s[tmp + 1: i].split(",")
                numbers_str = list(map(int, numbers_str))
                numbers.append(set(numbers_str))
                tmp = 0

    numbers.sort(key=lambda x:len(x))

    prev = set()
    for i in range(len(numbers)):
        tmp = numbers[i].difference(prev)
        answer.append(list(tmp)[0])
        prev = numbers[i]

    return answer

