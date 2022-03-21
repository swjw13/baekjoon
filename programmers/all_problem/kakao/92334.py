# 신고 결과 받기
# 2022 kakao
# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []

    user_alert_list = {i: set() for i in id_list}
    user_get_list = {i: set() for i in id_list}

    for i in report:
        fr, to = i.split()
        user_alert_list[fr].add(to)
        user_get_list[to].add(fr)

    for users in id_list:
        tmp = 0
        for a in user_alert_list[users]:
            if len(user_get_list[a]) >= k:
                tmp += 1
        answer.append(tmp)

    return answer