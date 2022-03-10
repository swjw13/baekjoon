# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1

    cloth = dict()
    for line in clothes:
        if line[1] in cloth.keys():
            cloth[line[1]] += 1
        else:
            cloth[line[1]] = 1

    for num in cloth.values():
        answer *= (num + 1)
    answer -= 1

    return answer

a = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(a))