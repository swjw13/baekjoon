# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258
# kakao 2020

from collections import defaultdict


def solution(gems):
    answer = []

    gem_dict = defaultdict(int)
    gem_prev = set()
    max_count = len(set(gems))

    for i in range(len(gems)):
        g = gems[i]
        gem_dict[g] = i
        gem_prev.add(g)
        if len(gem_prev) == max_count:
            if not answer:
                tmp = min(gem_dict.values())
                g_tmp = gems[tmp]
                answer = [tmp + 1, i + 1]
                gem_prev.remove(g_tmp)
            else:
                prev_length = answer[1] - answer[0]
                tmp = min(gem_dict.values())
                g_tmp = gems[tmp]
                new_length = i - tmp
                if prev_length > new_length:
                    answer = [tmp + 1, i + 1]
                    gem_prev.remove(g_tmp)

    return answer

