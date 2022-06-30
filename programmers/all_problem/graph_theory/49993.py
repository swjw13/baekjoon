# https://programmers.co.kr/learn/courses/30/lessons/49993
# 스킬 트리

from collections import defaultdict

def solution(skill, skill_trees):
    answer = 0
    length = len(skill)

    for s in skill_trees:
        tree = defaultdict(set)
        in_count = defaultdict(int)
        for i in range(length - 1):
            tree[skill[i]].add(skill[i + 1])
            in_count[skill[i + 1]] += 1

        idx = 0
        l = len(s)
        while idx != l:
            word = s[idx]
            if in_count[word] != 0:
                break
            else:
                for connected_point in tree[word]:
                    in_count[connected_point] -= 1
                idx += 1
        if idx == l:
            answer += 1


    return answer