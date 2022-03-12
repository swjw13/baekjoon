# K번째 수
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for i, j, k in commands:
        tmp = array[i - 1:j]
        tmp.sort()
        answer.append(tmp[k - 1])
    return answer

