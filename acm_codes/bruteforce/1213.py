# https://www.acmicpc.net/problem/1213
# 팰린드롬
import sys
input = sys.stdin.readline

name = input().strip()
even_word = []
odd_word = []
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if i in name:
        cnt = str(name).count(i)
        if cnt % 2 == 1:
            odd_word.append(i)
            cnt -= 1
        while cnt > 0:
            even_word.append(i)
            cnt -= 2

word = ""
if len(odd_word) > 1:
    word = "I'm Sorry Hansoo"
    even_word = []
elif len(odd_word) == 1:
    word = odd_word[0]
else:
    word = ""

even_word.reverse()
for i in even_word:
    word = i + word + i
print(word)