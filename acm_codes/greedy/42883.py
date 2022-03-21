# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883
# 해결 X


def solution(number, k):
    number = list(number)
    while k > 0:
        index = 0
        length = len(number)
        while index < length - 1 and number[index] >= number[index + 1]:
            index += 1

        if length - index < k:
            for i in range(k):
                number[index - i] = ""
            k = 0

        elif index == length - 1:
            for i in range(k):
                number[index - i] = ""
            k = 0
        else:
            del number[index]
            k -= 1
    return "".join(number)

