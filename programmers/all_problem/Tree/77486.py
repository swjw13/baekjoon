# https://programmers.co.kr/learn/courses/30/lessons/77486
# 다단계 칫솔 판매

from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []

    tree = {}
    for i in range(len(enroll)):
        if referral[i] == "-":
            tree[enroll[i]] = "minho"
        else:
            tree[enroll[i]] = referral[i]

    total = defaultdict(int)
    for i in range(len(amount)):
        cash = amount[i] * 100
        cur_seller = seller[i]
        while True:
            if cur_seller == "minho":
                total['minho'] += cash
                break
            elif cash < 10:
                total[cur_seller] += cash
                break
            else:
                total[cur_seller] += (cash - (cash // 10))
                cash = cash // 10
                cur_seller = tree[cur_seller]

    for i in enroll:
        answer.append(total[i])

    return answer

a =["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
b =["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
c =["young", "john", "tod", "emily", "mary"]
d =[12, 4, 2, 5, 10]

print(solution(a,b,c,d))