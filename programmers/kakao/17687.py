# https://programmers.co.kr/learn/courses/30/lessons/17687
# n진수 게임

def solution(n, t, m, p):
    answer = ''

    change = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    for i in range(10):
        change[i] = i

    def decChange(num):
        changed = ""
        while num != 0:
            changed = str(change[num % n]) + changed
            num //= n
        return changed

    all = "0"
    for i in range(1, t * m):
        all += decChange(i)

    for i in range(t):
        answer += all[p + m * i - 1]

    return answer

a = 2
b = 4
c = 2
d = 1
print(solution(a, b, c, d))