# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258
# kakao 2020

from collections import defaultdict


def solution(gems):
    mn = None
    mx = None

    gem_dict = defaultdict(int)
    gem_prev = set()
    max_count = len(set(gems))

    for i in range(len(gems)):
        g = gems[i]
        gem_dict[g] = i
        gem_prev.add(g)
        if len(gem_prev) == max_count:
            if not mn:
                tmp = min(gem_dict.values())
                g_tmp = gems[tmp]
                mn = tmp + 1
                mx = i + 1
                gem_prev.remove(g_tmp)
            else:
                prev_length = mx - mn
                tmp = min(gem_dict.values())
                new_length = i - tmp
                if prev_length > new_length:
                    g_tmp = gems[tmp]
                    mn = tmp + 1
                    mx = i + 1
                    gem_prev.remove(g_tmp)

    return [mn, mx]