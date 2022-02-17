# LCD 테스트
# https://www.acmicpc.net/problem/2290

import sys

input = sys.stdin.readline

s, n = input().split()
s = int(s)

for number_each in n:
    print(end=' ')
    if number_each in "23567890":
        for _ in range(s):
            print("-", end='')
    else:
        for _ in range(s):
            print(end=' ')
    print(end=' ')
    print(end=' ')

print()

for _ in range(s):
    for number_each in n:
        if number_each in "56":
            print("|", end="")
            for _ in range(s + 1):
                print(end=" ")
        elif number_each in "1237":
            for _ in range(s + 1):
                print(end=' ')
            print("|", end="")
        else:
            print("|", end="")
            for _ in range(s):
                print(end=' ')
            print("|", end="")
        print(end=' ')

    print()

for number_each in n:
    print(end=' ')
    if number_each in "2345689":
        tmp = "-"
    else:
        tmp = ' '
    for _ in range(s):
        print(tmp, end='')
    print(end=' ')
    print(end=' ')

print()

for _ in range(s):
    for number_each in n:
        if number_each in "2":
            print("|", end="")
            for _ in range(s + 1):
                print(end=' ')
        elif number_each in "134579":
            for _ in range(s + 1):
                print(end=' ')
            print("|", end="")
        else:
            print("|", end="")
            for _ in range(s):
                print(end=' ')
            print("|", end="")
        print(end=' ')

    print()

for number_each in n:
    print(end=' ')
    if number_each in "2356890":
        for _ in range(s):
            print("-", end='')
    else:
        for _ in range(s):
            print(end=' ')
    print(end=' ')
    print(end=' ')
