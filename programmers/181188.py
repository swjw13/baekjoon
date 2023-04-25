def solution(targets):
    answer = 0
    targets.sort(key=lambda x: (x[1], x[0]))

    last_e = 0

    for t in targets:
        if last_e <= t[0]:
            answer += 1
            last_e = t[1]

    return answer
