# 정수 삼각형
# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    prev = triangle[0]
    for line in triangle[1:]:
        tmp = []
        for i in range(len(line)):
            if i == 0:
                tmp.append(prev[0] + line[i])
            elif i == len(line) - 1:
                tmp.append(prev[-1] + line[i])
            else:
                tmp.append(max(prev[i], prev[i - 1]) + line[i])
        prev = tmp
    return max(prev)

