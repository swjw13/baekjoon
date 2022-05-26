# https://programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수

def solution(n):
    fibo = [0, 1]
    for i in range(2, n + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])

    return fibo[n]