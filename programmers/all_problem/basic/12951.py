# https://programmers.co.kr/learn/courses/30/lessons/12951
# Jaden Case 문자열 만들기

def solution(s: str):
    answer = ""
    tmp = s.split(" ")
    print(tmp)
    for i in tmp:
        if len(i) >= 1:
            lst = list(i)
            if lst[0].isalpha():
                lst[0] = lst[0].upper()
            for j in range(len(lst) - 1):
                lst[1 + j] = lst[1 + j].lower()

            answer += "".join(lst) + " "
    return answer[:-1]

a = "one more   time"
print(solution(a))
