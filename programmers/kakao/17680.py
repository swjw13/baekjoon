# https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3
# 캐시


from collections import deque

def solution(cacheSize, cities):
    answer = 0

    cache = deque()
    for i in cities:
        i = i.lower()
        if i in cache:
            answer += 1
            cache.remove(i)
            cache.append(i)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.append(i)
                cache.popleft()
            else:
                cache.append(i)
    return answer

a = 2
b = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(a, b))