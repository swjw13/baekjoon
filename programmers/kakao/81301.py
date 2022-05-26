# 숫자와 문자열
# https://programmers.co.kr/learn/courses/30/lessons/81301
# kakao 2021

def solution(s):
    a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    b = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(10):
        s = s.replace(a[i], b[i])
    answer = int(s)
    return answer
