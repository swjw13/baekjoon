# 124 숫자의 나라
# https://programmers.co.kr/learn/courses/30/lessons/12899

# 3 9 27 81 ...

def solution(n):
    answer = ''

    while n > 0:
        n -= 1
        tmp = n % 3
        if tmp == 0:
            answer += "1"
        elif tmp == 1:
            answer += "2"
        else:
            answer += "4"
        n //= 3

    answer_reversed = ""
    length = len(answer)
    for i in range(length):
        answer_reversed += answer[length - i - 1]

    return answer_reversed

a = 9
print(solution(a))