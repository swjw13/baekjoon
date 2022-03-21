# 크레인 인형뽑기
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0

    basket = []
    length = 0
    n = len(board)

    def find_row(line):
        tmp = 0
        while tmp < n and board[tmp][line] == 0:
            tmp += 1
        return tmp

    for i in moves:
        row = find_row(i - 1)

        if row == n:
            continue
        else:
            basket.append(board[row][i - 1])
            length += 1
            board[row][i - 1] = 0
 
            if length > 1 and basket[-1] == basket[-2]:
                answer += 2
                basket.pop()
                basket.pop()
                length -= 2

    return answer


a = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
b = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(a, b))
