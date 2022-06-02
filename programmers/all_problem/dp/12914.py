# https://programmers.co.kr/learn/courses/30/lessons/12914
# 멀리 뛰기

def solution(n):
    jumps = [0 for _ in range(n + 1)]
    jumps[0] = 1
    for i in range(n):
        jumps[i + 1] += jumps[i]
        if i + 2 < n + 1:
            jumps[i + 2] += jumps[i]

    return jumps[n]