#https://www.acmicpc.net/problem/2525
# 오븐 시계

import sys
input = sys.stdin.readline

H, M = list(map(int, input().split()))
H_todo = int(input())

M += H_todo
if M >= 60:
    H += M // 60
    M %= 60

if H >= 24:
    H = H % 24

print(H, M)