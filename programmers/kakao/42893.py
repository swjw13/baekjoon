import re
from collections import defaultdict


def solution(word, pages):
    answer = 0
    word = word.lower()

    index_dict = dict()
    index_tmp = 0
    linked_dict = defaultdict(set)
    count_dict = dict()
    total = set()

    for i in pages:
        exp1 = r"<meta[^>]+/>"
        meta = re.search(exp1, i).group()

        exp2 = r'https://[^"]+'
        my_url = re.search(exp2, meta).group()
        if my_url not in index_dict.keys():
            index_dict[my_url] = index_tmp
            index_tmp += 1

        exp3 = r'<a href=[^>]+>'
        hrefs = re.findall(exp3, i)
        linked = []
        for page in hrefs:
            linked.append(re.search(exp2, page).group())
        linked_dict[my_url].update(set(linked))

        i = i.lower()
        exp4 = r'<[^>]+>'
        word_extracted = re.sub(exp4, " ", i)
        word_extracted = re.sub(r"[^a-z]+"," ", word_extracted)

        exp5 = r'[^a-z]' + word.lower() + r'[^a-z]'
        count_dict[my_url] = len(re.findall(exp5, word_extracted))

        total.add(my_url)

    max_value = 0
    for i in total:
        tmp = count_dict[i]
        for connected in total:
            if i in linked_dict[connected]:
                tmp += count_dict[connected] / len(linked_dict[connected])
        if tmp > max_value:
            answer = index_dict[i]
            max_value = tmp
        elif tmp == max_value:
            answer = min(answer, index_dict[i])

    return answer