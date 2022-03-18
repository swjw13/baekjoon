# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677
# kakao 2018

def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    a1 = set()
    a2 = set()
    repeated_a1 = dict()
    repeated_a2 = dict()

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            src = str1[i] + str1[i + 1]
            if src in a1:
                if src in repeated_a1.keys():
                    repeated_a1[src] += 1
                else:
                    repeated_a1[src] = 1
                src += str(repeated_a1[src])
                a1.add(src)
            else:
                a1.add(src)

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            src = str2[i] + str2[i + 1]
            if src in a2:
                if src in repeated_a2.keys():
                    repeated_a2[src] += 1
                else:
                    repeated_a2[src] = 1
                src += str(repeated_a2[src])
                a2.add(src)
            else:
                a2.add(src)

    if len(a1) == 0 and len(a2) == 0:
        answer = 1
    else:
        answer = len(a1.intersection(a2)) / len(a1.union(a2))
    return int(answer * 65536)


