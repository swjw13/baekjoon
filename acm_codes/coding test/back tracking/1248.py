# 숫자 맞추는 문제
# https://www.acmicpc.net/problem/1248

import sys
input = sys.stdin.readline

N = int(input())
summary = []
summary_total = list(input())[:-1]

index = 0
length = N

# 각 부호들을 index 에 맞게 정리를 해줌
# (ex summary의 index 1 은 1번째 숫자로부터의 모든 결과)
while length > 0:
    summary.append(summary_total[index: index + length])
    index += length
    length -= 1


# 백트래킹(결국 bruteforce)
# 각 윗 단계의 결과들을 가져와서 부호와 모든 부호와 맞는 경우만 다음 단계로 전달을 한다.
# 결과가 하나라도 나오면 exit으로 끝을 내줌
# 마지막 숫자부터 앞으로 하나씩 체크를 해주는 방법 사용
def find_number(row, prev, prev_length):
    if prev_length == N:
        for i in prev:
            print(i, end=' ')
        sys.exit()

    if summary[row][0] == "+":
        available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    elif summary[row][0] == "0":
        available_numbers = [0]
    else:
        available_numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

    for nums in available_numbers:
        tmp = True
        total = nums
        for i in range(prev_length):
            total += prev[i]
            if not ((total < 0 and summary[row][1 + i] == "-") or
                    (total > 0 and summary[row][1 + i] == "+") or
                    (total == 0 and summary[row][1 + i] == "0")):
                tmp = False
                break
        if not tmp:
            continue
        else:
            new_prev = tuple([nums] + list(prev))
            find_number(row - 1, new_prev, prev_length + 1)


find_number(N - 1, (), 0)
