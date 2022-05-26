# https://programmers.co.kr/learn/courses/30/lessons/12949
# 행렬의 곱셈

def solution(arr1, arr2):
    answer = []

    a = len(arr1)
    b = len(arr1[0])
    c = len(arr2[0])

    for i in range(a):
        tmp = []
        for j in range(c):
            count = 0
            for k in range(b):
                count += arr1[i][k] * arr2[k][j]
            tmp.append(count)
        answer.append(tmp)

    return answer
