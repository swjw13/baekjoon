# https://programmers.co.kr/learn/courses/30/lessons/17684
# 압축

def solution(msg):
    answer = []

    word_number = dict()
    word_set = set()
    words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        word_number[words[i]] = i + 1
        word_set.add(words[i])

    word_num_count = 27
    start_idx = 0
    while start_idx < len(msg):
        end_idx = start_idx + 1
        while True:
            if end_idx == len(msg):
                answer.append(word_number[msg[start_idx:]])
                start_idx = end_idx
                break
            if msg[start_idx:end_idx] in word_set and msg[start_idx:end_idx + 1] not in word_set:
                answer.append(word_number[msg[start_idx:end_idx]])
                word_number[msg[start_idx:end_idx + 1]] = word_num_count
                word_num_count += 1
                word_set.add(msg[start_idx:end_idx + 1])
                start_idx = end_idx
            else:
                end_idx += 1

    return answer

a = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(a))