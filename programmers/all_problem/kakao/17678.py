# 셔틀버스
# https://programmers.co.kr/learn/courses/30/lessons/17678
# kakao 2018

from bisect import bisect_right


def solution(n, t, m, timetable):
    answer = ''

    timetable.sort()

    for i in range(n):
        cur_hour = str(9 + (i * t) // 60)
        cur_minute = str((i * t) % 60)
        if len(cur_hour) == 1:
            cur_hour = "0" + cur_hour
        if len(cur_minute) == 1:
            cur_minute = "0" + cur_minute

        cur_time = cur_hour + ":" + cur_minute

        # 이번 버스를 탄다고 가정
        people_ready = bisect_right(timetable, cur_time)
        if people_ready < m:
            answer = cur_time
        else:
            cut_time = timetable[m - 1]
            cut_hour, cut_minute = cut_time.split(":")
            if int(cut_minute) == 0:
                must_hour = int(cut_hour) - 1
                must_minute = 59
            else:
                must_hour = int(cut_hour)
                must_minute = int(cut_minute) - 1

            must_hour = str(must_hour)
            if len(must_hour) == 1:
                must_hour = "0" + must_hour
            must_minute = str(must_minute)
            if len(must_minute) == 1:
                must_minute = "0" + must_minute
            answer = must_hour + ":" + must_minute

        # 다음 버스를 탄다고 가정
        if people_ready < m:
            timetable = timetable[people_ready:]
        else:
            timetable = timetable[m:]

    return answer

