# https://www.acmicpc.net/problem/1284
# 호수판 넓이

import sys
input = sys.stdin.readline

word_between = {"0":4, "1": 2}
for i in range(2, 10):
    word_between[str(i)] = 3

while True:
    num = int(input())
    if num == 0:
        break
    cnt = 1
    for i in str(num):
        cnt += (word_between[i] + 1)
    print(cnt)