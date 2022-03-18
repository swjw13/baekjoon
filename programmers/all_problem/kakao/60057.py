# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057
# 2020 kakao

def solution(s):
    mn = 9999

    if(len(s)) == 1:
        mn = 1

    for i in range(1, len(s)):
        idx = 0
        total_length = 0
        while idx < len(s):
            if len(s[idx:]) < i:
                total_length += len(s[idx:])
                idx += 1000000
            else:
                src = s[idx:idx + i]
                idx += i
                total_length += i

                if s[idx:].startswith(src):
                    count = 1
                    while s[idx:].startswith(src):
                        idx += i
                        count += 1
                    total_length += len(str(count))

        mn = min(mn, total_length)

    return mn

