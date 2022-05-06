# https://programmers.co.kr/learn/courses/30/lessons/17681
# 비밀 지도

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = arr1[i] | arr2[i]
        line = ""
        for i in range(n):
            if tmp & 1 == 1:
                line = "#" + line
            else:
                line = " " + line
            tmp = tmp >> 1

        answer.append(line)
    return answer