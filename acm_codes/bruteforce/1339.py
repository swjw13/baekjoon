# https://www.acmicpc.net/problem/1339
# 단어 수학

from collections import defaultdict

N = int(input())
max_length = 0
words = []

weights = defaultdict(int)

for _ in range(N):
    tmp = input()

    c = 1
    for i in range(len(tmp) - 1, -1, -1):
        weights[tmp[i]] += c
        c *= 10

    words.append(tmp)

weights = list(weights.items())
weights.sort(key=lambda x: x[1], reverse=True)

wordTo_num = dict()
idx = 9
for word, _ in weights:
    wordTo_num[word] = idx
    idx -= 1

answer = 0
for word in words:
    tmp = ""
    for char in word:
        tmp += str(wordTo_num[char])
    answer += int(tmp)

print(answer)