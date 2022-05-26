# https://programmers.co.kr/learn/courses/30/lessons/12953
# n 개의 최소공배수

import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


def lcs(a, b):
    g = gcd(a, b)
    return a * b // g


def solution(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        g = lcs(arr[0], arr[1])
        for i in arr[2:]:
            g = lcs(g, i)
        return g
