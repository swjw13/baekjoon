# 추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676
# 2018 kakao

def solution(lines):
    answer = 0

    def change_time_to_milli(time):
        ans = 0.0
        tmp = time.split(":")
        sec = tmp[2].split(".")
        ans += int(sec[1]) + int(sec[0]) * 1000
        ans += int(tmp[1]) * 60 * 1000 + int(tmp[0]) * 60 * 60 * 1000
        return ans

    logs = []
    for i in lines:
        tmp = i.split()
        end_time = change_time_to_milli(tmp[1])
        passed_time = float(tmp[2][:-1]) * 1000
        start_time = end_time - passed_time + 1
        start_time = max(0.0, start_time)
        logs.append([start_time, end_time])

    print(logs)

    for i in logs:
        cnt = 0
        for j in logs:
            if not (j[1] < i[0] or j[0] > i[0] + 1000):
                cnt += 1
        answer = max(answer, cnt)

        cnt = 0
        for j in logs:
            if not (j[1] < i[1] or j[0] > i[1] + 1000):
                cnt += 1
        answer = max(answer, cnt)

    return answer


a = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(a))
