# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888
# 2019 kakao

def solution(record):
    answer = []

    cache = []
    persons = {}

    for r in record:
        action = r.split()
        if action[0] == "Enter":
            id = action[1]
            name = action[2]
            cache.append(["Enter", id])
            persons[id] = name

        elif action[0] == "Leave":
            id = action[1]
            cache.append(["Leave", id])

        else:
            id = action[1]
            name = action[2]
            persons[id] = name

    for action, id in cache:
        if action == "Enter":
            answer.append("{}님이 들어왔습니다.".format(persons[id]))
        elif action == "Leave":
            answer.append("{}님이 나갔습니다.".format(persons[id]))
        # else:
        #     pass
    return answer


a = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(a))
