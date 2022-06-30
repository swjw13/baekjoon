# 부분수열의 합
# https://www.acmicpc.net/problem/1182

import sys

input = sys.stdin.readline

N, S = list(map(int, input().split()))
lst = list(map(int, input().split()))

total = 0


def find_total(index, prev, prev_str):
    global total
    if index == N:
        if prev == S and prev_str and len(prev_str) > 0:
            total += 1
        return
    else:
        tmp = lst[index]
        find_total(index + 1, prev + tmp, str(tmp) + prev_str)
        find_total(index + 1, prev, prev_str)


find_total(0, 0, "")
print(total)