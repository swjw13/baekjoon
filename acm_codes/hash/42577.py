# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book: list[str]) -> bool:
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].find(phone_book[i]) == 0:
            answer = False
            break
    return answer


