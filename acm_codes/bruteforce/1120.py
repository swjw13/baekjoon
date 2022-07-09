# https://www.acmicpc.net/problem/1120
# 문자열

import sys
input = sys.stdin.readline

def diff(str1, str2):
    length = len(str1)
    cnt = 0
    for i in range(length):
        if str1[i] != str2[i]:
            cnt += 1
    return cnt


a, b = input().split()
ans = sys.maxsize
if len(a) == len(b):
    ans = diff(a, b)
else:
    a_length = len(a)
    b_length = len(b)
    for i in range(b_length - a_length + 1):
        ans = min(ans, diff(a, b[i: i + a_length]))
print(ans)