def solution(numbers, target):
    answer = 0
    length = len(numbers)

    def find_target(index, total):
        global answer
        if index == length:
            if total == target:
                return 1
            else:
                return 0
        else:
            a = find_target(index + 1, total - numbers[index])
            b = find_target(index + 1, total + numbers[index])
            return a + b

    answer = find_target(0, 0)

    return answer

