def solution(m, musicinfos):
    answer = None

    def extract(st, answer):
        target = m
        start_time, end_time, title, body = st.split(",")
        b = []
        body_split = []
        tmp = 1
        while tmp < len(body):
            if body[tmp] in "ABCDEFG":
                body_split.append(body[:tmp])
                body = body[tmp:]
                tmp = 1
            else:
                tmp += 1
        body_split.append(body)

        tmp = start_time.split(":")
        start_min = int(tmp[0]) * 60 + int(tmp[1])
        tmp = end_time.split(":")
        end_min = int(tmp[0]) * 60 + int(tmp[1])

        for i in range(end_min - start_min):
            b.append(body_split[i % len(body_split)])
        l1 = len(b)

        target_split = []
        tmp = 1
        while tmp < len(target):
            if target[tmp] in "ABCDEFG":
                target_split.append(target[:tmp])
                target = target[tmp:]
                tmp = 1
            else:
                tmp += 1
        target_split.append(target)
        l2 = len(target_split)

        tmp = False
        for i in range(l1 - l2 + 1):
            if b[i:i + l2] == target_split:
                tmp = True
                break

        if tmp:
            if answer is None:
                return [end_min - start_min, title]
            else:
                if end_min - start_min > answer[0]:
                    return [end_min - start_min, title]
                else:
                    return "1"
        else:
            return "1"

    for i in musicinfos:
        tmp = extract(i, answer)
        if tmp != "1":
            answer = tmp

    if answer is None:
        return "(None)"
    else:
        return answer[1]


a = "ABCDEFG"
b = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(a, b))
