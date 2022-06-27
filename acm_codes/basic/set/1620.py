# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
name_to_num = dict()
num_to_name = dict()

for i in range(1, N + 1):
    tmp = input().strip()
    name_to_num[tmp] = i
    num_to_name[i] = tmp

for _ in range(M):
    tmp = input().strip()
    if tmp[0] in "1234567890":
        print(num_to_name[int(tmp)])
    else:
        print(name_to_num[str(tmp)])
