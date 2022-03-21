# 추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676
# 2018 kakao
# 미해결

def solution(lines):
    answer = 0
    lines_changed = []

    def change_time_format(time_str):
        res = 0
        hour, minute, second = time_str.split(":")
        res += float(hour) * 3600
        res += float(minute) * 60
        res += float(second)

        return res * 1000

    start = 0
    end = change_time_format("24:00:00.000") - 1

    for i in lines:
        date, time, sec = i.split()
        end_time = change_time_format(time)
        start_time = end_time - float(sec[:-1]) * 1000 + 1
        lines_changed.append([start_time, end_time])

    print(lines_changed)

    while True:
        if start > end:
            break
        mid = (start + end) // 2

        not_started = 0
        continuing = 0
        finished = 0

        for times in lines_changed:
            if times[1] < mid - 500:
                not_started += 1
            elif times[0] > mid + 500:
                finished += 1
            elif mid - 500 <= times[0] and times[1] <= mid + 500:
                continuing += 1
            elif times[0] <= mid - 500 <= times[1]:
                not_started += 1
                continuing += 1
            else:
                continuing += 1
                finished += 1
        answer = max(answer, continuing)

        print("start: {}, end: {}, not_started: {}, continuing: {}, finished: {}".format(start, end, not_started, continuing, finished))
        print("mid: {}".format(mid))
        if not_started > finished:
            end = mid - 1
        else:
            start = mid + 1

    return answer


a = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]
print(solution(a))
