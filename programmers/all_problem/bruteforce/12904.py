# https://school.programmers.co.kr/learn/courses/30/lessons/12904
# 가장 긴 팰린드롬

def solution(s):
    answer = 0
    length = len(s)
    if length == 1:
        return 1
    else:
        for i in range(0, (length - 1) * 2 + 1):
            cnt = 0
            if i % 2 == 0:
                start_idx = i // 2
                end_idx = start_idx + 1
                while start_idx >= 0 and end_idx < length and s[start_idx] == s[end_idx]:
                    cnt += 2
                    start_idx -= 1
                    end_idx += 1
            else:
                start_idx = i // 2 - 1
                end_idx = i // 2 + 1
                cnt += 1
                while start_idx >= 0 and end_idx < length and s[start_idx] == s[end_idx]:
                    cnt += 2
                    start_idx -= 1
                    end_idx += 1
            answer = max(answer, cnt)

        return answer

a = "a"
print(solution(a))
