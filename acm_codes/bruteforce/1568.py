# https://www.acmicpc.net/problem/1568
# 새

N = int(input())
turn = 0
cur_number = 1
while N > 0:
    if cur_number > N:
        cur_number = 1
    N -= cur_number
    cur_number += 1
    turn += 1
print(turn)