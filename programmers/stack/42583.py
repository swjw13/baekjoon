# 다리를 지나가는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    total_truck = len(truck_weights)
    end = []
    middle = deque([0 for _ in range(bridge_length)])
    answer = 0

    while len(end) != total_truck:
        if middle[0] != 0:
            end.append(middle[0])
            middle[0] = 0

        if len(truck_weights) == 0:
            tmp = 0
            while tmp < len(middle) and middle[tmp] == 0:
                tmp += 1
            if tmp == len(middle):
                answer += 1
                continue
            else:
                middle.rotate(-tmp)
                answer += tmp
        else:
            if sum(middle) + truck_weights[0] <= weight:
                middle.rotate(-1)
                tmp = truck_weights.popleft()
                middle[-1] = tmp
                answer += 1

            else:
                tmp = 0
                while middle[tmp] == 0:
                    tmp += 1
                middle.rotate(-tmp)
                answer += tmp
    return answer

a = 2
b = 10
c = [7,4,5,6]
print(solution(a,b,c))