# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060
# kakao 2020

from collections import defaultdict


def solution(words, queries):
    answer = []

    def bi_left(st):
        start = 0
        end = len(st) - 1
        ans = -1
        while end >= start:
            mid = (start + end) // 2
            if st[mid] == "?":
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def bi_right(st):
        start = 0
        end = len(st) - 1
        ans = -1
        while end >= start:
            mid = (start + end) // 2
            if st[mid] == "?":
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans

    word_dict = defaultdict(set)
    for i in words:
        s = len(i)
        word_dict[s].add(i)

    for i in queries:
        l = len(i)
        word_list = word_dict[l]
        count = 0
        if i.count("?") == l:
            count = len(word_list)
        else:
            if i[0] == "?":
                tmp = bi_right(i)
                for word in word_list:
                    s = tmp + 1
                    if word[s:] == i[s:]:
                        count += 1
            else:
                tmp = bi_left(i)
                for word in word_list:
                    if word[:tmp] == i[:tmp]:
                        count += 1

        answer.append(count)

    return answer
