from itertools import product


def solution(users, emoticons):
    answer = []

    for i in product([1, 2, 3, 4], repeat=len(emoticons)):

        res = [0, 0]
        for user in users:
            count = 0
            for perc in range(len(emoticons)):
                if i[perc] * 10 >= user[0]:
                    count += emoticons[perc] * (10 - i[perc]) // 10
            if count >= user[1]:
                res[0] += 1
            else:
                res[1] += count
        answer.append(res)

    answer.sort(key=lambda x: (x[0], x[1]), reverse=True)

    return answer[0]