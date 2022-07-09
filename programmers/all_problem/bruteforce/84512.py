# https://programmers.co.kr/learn/courses/30/lessons/84512
# 모음사전

def solution(word):
    tmp = ["A", "E", "I", "O", "U"]
    dictionary = []
    for a in range(5):
        dictionary.append(tmp[a])
        for b in range(5):
            dictionary.append(tmp[a] + tmp[b])
            for c in range(5):
                dictionary.append(tmp[a] + tmp[b] + tmp[c])
                for d in range(5):
                    dictionary.append(tmp[a] + tmp[b] + tmp[c] + tmp[d])
                    for e in range(5):
                        dictionary.append(tmp[a] + tmp[b] + tmp[c] + tmp[d] + tmp[e])

    # dictionary.sort()

    return dictionary.index(word) + 1

a = "UUUUU"
print(solution(a))