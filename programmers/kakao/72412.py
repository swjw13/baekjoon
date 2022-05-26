# 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412
# kakao 2021

from bisect import bisect_left

def solution(info, query):
    answer = []

    participant_info = dict()
    for language in ["cpp", "java", "python", "-"]:
        for part in ["backend", "frontend", "-"]:
            for prev in ["junior", "senior", "-"]:
                for food in ["chicken", "pizza", "-"]:
                    participant_info[str(language) + str(part) + str(prev) + str(food)] = []

    for infos in info:
        language, part, prev, food, point = infos.split()
        for a in [language, "-"]:
            for b in [part, "-"]:
                for c in [prev, "-"]:
                    for d in [food, "-"]:
                        participant_info[a + b + c + d].append(int(point))

    for i in participant_info.keys():
        participant_info[i].sort()

    for q in query:
        lst = q.split()

        final_query = participant_info[lst[0] + lst[2] + lst[4] + lst[6]]
        answer.append(len(final_query) - bisect_left(final_query, int(lst[7])))


    return answer
