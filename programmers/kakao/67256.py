# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256
# kakao 2020

def solution(numbers, hand):
    answer = ''

    def get_distance(pos_one, pos_two):
        return abs(pos_one[0] - pos_two[0]) + abs(pos_one[1] - pos_two[1])

    left_pos = (3, 0)
    right_pos = (3, 2)
    pos = {0: (3, 1)}

    a = [i for i in range(1, 10)]
    for i in range(9):
        pos[a[i]] = (i // 3, i % 3)

    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            left_pos = pos[i]
        elif i in [3, 6, 9]:
            answer += "R"
            right_pos = pos[i]
        else:
            number_pos = pos[i]
            left_dist = get_distance(left_pos, number_pos)
            right_dist = get_distance(right_pos, number_pos)

            if left_dist < right_dist:
                answer += "L"
                left_pos = number_pos
            elif left_dist > right_dist:
                answer += "R"
                right_pos = number_pos
            else:
                if hand == "right":
                    answer += "R"
                    right_pos = number_pos
                else:
                    answer += "L"
                    left_pos = number_pos

    return answer
