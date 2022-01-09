words = []
N = int(input())
for _ in range(N):
    word = input()
    words.append(word)

words.sort(key=lambda x:(len(x), x))

print(words[0])
for i in range(1,N):
    if words[i-1] == words[i]:
        continue
    print(words[i])