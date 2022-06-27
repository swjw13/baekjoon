# https://www.acmicpc.net/problem/11478
# 서로 다른 부분 문자열의 개수

word = input()
length = len(word)
idx = 0
ans = set()
for i in range(length):
    for j in range(i, length):
        ans.add(word[i:j + 1])

print(len(ans))