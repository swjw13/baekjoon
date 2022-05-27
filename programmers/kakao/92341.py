# https://programmers.co.kr/learn/courses/30/lessons/92341
# 주차 요금 계산

from collections import defaultdict
import math
def solution(fees, records):
    answer = []

    def time_split(time_str):
        tmp = time_str.split(":")
        return int(tmp[0]) * 60 + int(tmp[1])

    parking = dict()
    time_passes = defaultdict(int)

    for i in records:
        tmp = i.split()
        if tmp[2] == "IN":
            time_in = time_split(tmp[0])
            parking[(tmp[1])] = time_in
        else:
            time_in = parking[tmp[1]]
            time_out = time_split(tmp[0])
            time_passes[tmp[1]] += (time_out - time_in)
            parking.pop(tmp[1])

    last_time = time_split("23:59")
    for i in parking.keys():
        time_in = parking[i]
        time_passes[i] += last_time - time_in

    b = list(time_passes.keys())
    b.sort()

    for i in b:
        time = time_passes[i]
        if time > fees[0]:
            fee = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
        else:
            fee = fees[1]
        answer.append(fee)

    return answer

a = [180, 5000, 10, 600]
b = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(a, b))
