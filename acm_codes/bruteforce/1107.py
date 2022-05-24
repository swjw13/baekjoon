# 리모컨 문제
# https://www.acmicpc.net/problem/1107

import sys
from itertools import product

input = sys.stdin.readline

target_number = int(input())
M = int(input())
broken_button = []
if M != 0:
    broken_button = input().split()
original_button = ["{}".format(i) for i in range(10)]


def check_available(number):
    for i in str(number):
        if i in broken_button:
            return False
    return True


tmp = abs(100 - target_number)
visited = [False for _ in range(1000001)]
number_length = len(str(target_number))
available_numbers = list(set(original_button) - set(broken_button))
available_numbers_without_zero = list(set(available_numbers) - set("0"))

for i in product(available_numbers, repeat=number_length - 1):
    word = "".join(i)

    if number_length == 1:
        available_numbers_without_zero = available_numbers

    for j in available_numbers_without_zero:
        number = int(j + word)
        if number < 1000001 and not visited[number]:
            tmp = min(tmp, abs(number - target_number) + number_length)
            visited[number] = True

if number_length != 1:
    for i in product(available_numbers, repeat=number_length - 2):
        word = "".join(i)
        if number_length == 2:
            available_numbers_without_zero = available_numbers
        for j in available_numbers_without_zero:
            number = int(j + word)
            if number < 1000001 and not visited[number]:
                tmp = min(tmp, abs(number - target_number) + number_length - 1)
                visited[number] = True

if number_length < 6:
    for i in product(available_numbers, repeat=number_length):
        word = "".join(i)
        for j in available_numbers_without_zero:
            number = int(j + word)
            if number < 1000001 and not visited[number]:
                tmp = min(tmp, abs(number - target_number) + number_length + 1)
                visited[number] = True

print(tmp)
