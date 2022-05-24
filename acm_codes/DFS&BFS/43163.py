# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):

    def strcmp(src, target):
        ans = 0
        for i in range(len(src)):
            if src[i] != target[i]:
                ans += 1
        if ans == 1:
            return True
        else:
            return False

    answer = 0

    visited = set()
    queue = deque([(begin, 0)])
    visited.add(begin)
    while queue:
        cur_word, count = queue.popleft()
        if cur_word == target:
            answer = count
            break
        for i in words:
            if i not in visited and strcmp(cur_word, i):
                queue.append((i, count + 1))
                visited.add(i)


    return answer

