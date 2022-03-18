# 주식 가격
# https://programmers.co.kr/learn/courses/30/lessons/42584
# 오큰수 개념 확실하게 알기

def solution(prices):
    length = len(prices)
    answer = [0 for _ in range(length)]
    stack = []

    for i in range(length - 1):
        cur_val = prices[i]
        cur_idx = i
        while len(stack) != 0 and stack[-1][0] > cur_val:
            (val, idx) = stack.pop()
            answer[idx] = cur_idx - idx

        stack.append((cur_val, cur_idx))

    while stack:
        (val, idx) = stack.pop()
        answer[idx] = length - idx - 1

    return answer

a = [1,2,3,2,3]
print(solution(a))