# https://programmers.co.kr/learn/courses/30/lessons/72414
# 광고 삽입
# kakao 2021
# sliding window algorithm

import sys


def solution(play_time, adv_time, logs):
    def time_to_second(time):
        hh, mm, ss = time.split(":")
        return int(hh) * 3600 + int(mm) * 60 + int(ss)

    def second_to_time(total_sec):
        hour = str(total_sec // 3600)
        if len(hour) == 1:
            hour = "0" + hour
        minute = str((total_sec % 3600) // 60)
        if len(minute) == 1:
            minute = "0" + minute
        second = str(total_sec % 60)
        if len(second) == 1:
            second = "0" + second
        return "{}:{}:{}".format(hour, minute, second)

    play_time = time_to_second(play_time)
    adv_time = time_to_second(adv_time)

    lst = [[0 for _ in range(play_time + 1)] for _ in range(2)]
    for time in logs:
        start, end = time.split("-")
        lst[0][time_to_second(start)] += 1
        lst[1][time_to_second(end)] += -1

    cur_person = 0
    total_time = 0
    max_time = 0

    tmp_time = sys.maxsize

    start = 0

    for end in range(len(lst[0])):
        total_time += cur_person
        cur_person += (lst[0][end] + lst[1][end])

        if end - start == adv_time:
            if total_time > max_time:
                tmp_time = start
                max_time = total_time
            cur_person -= (lst[0][start] + lst[1][start])
            start += 1

    return second_to_time(tmp_time)


a = "99:59:59"
b = "25:00:00"
c = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(a, b, c))
