# https: // programmers.co.kr / learn / courses / 30 / lessons / 17686
# 파일명 정렬
import re


def solution(files):
    tmp = []

    def extract(file: str):
        pattern = r'\d+'
        lst = re.findall(pattern, file)
        idx = file.find(lst[0])

        head = file[:idx]

        ans = [head, lst[0], file[idx + len(lst[0]):]]
        return ans

    for i in range(len(files)):
        tmp.append(extract(files[i]) + [i])

    tmp.sort(key=lambda x: (x[0].lower(), int(x[1]), x[3]))

    answer = []
    for i in tmp:
        answer.append(i[0] + i[1] + i[2])
    return answer


a = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(a))
