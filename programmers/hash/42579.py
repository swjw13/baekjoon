# 베스트 엘범
# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    count_by_genre = dict()
    in_genre = dict()

    for i in range(len(genres)):
        g = genres[i]
        if g in count_by_genre.keys():
            count_by_genre[g] += plays[i]
        else:
            count_by_genre[g] = plays[i]

        if g in in_genre.keys():
            in_genre[g].append((plays[i], i))
        else:
            in_genre[g] = [(plays[i], i)]

    sorted_genre = sorted(count_by_genre.items(), key=lambda x: x[1], reverse=True)

    for i, _ in sorted_genre:
        in_genre[i].sort(key=lambda x: (x[0], -x[1]), reverse=True)
        if len(in_genre[i]) == 1:
            answer.append(in_genre[i][0][1])
        else:
            for j in range(2):
                answer.append(in_genre[i][j][1])

    return answer


a = ["classic", "pop", "classic", "classic", "pop"]
b = [500, 600, 150, 800, 2500]
print(solution(a, b))
