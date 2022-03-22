# 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064
# 2019 kakao

from collections import defaultdict


def solution(user_id, banned_id):
    answer = []

    def matched(str1, str2):
        if len(str1) != len(str2):
            return False
        else:
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    if str2[i] != "*":
                        return False
            return True


    # 각 ban id마다 해당하는 id 가져오기
    banned_list = defaultdict(set)
    total_ban_id = len(banned_id)
    for ban in banned_id:
        for users in user_id:
            if matched(users, ban):
                banned_list[ban].add(users)

    lst = []
    for i in banned_id:
        lst.append(banned_list[i])

    def find_list(level, max_level, prevs):
        if level == max_level:
            if prevs not in answer:
                answer.append(prevs)
            return
        else:
            for i in lst[level]:
                if i in prevs:
                    continue
                new_prev = prevs.union({i})
                find_list(level + 1, max_level, new_prev)

    find_list(0, total_ban_id, set())

    return len(answer)
