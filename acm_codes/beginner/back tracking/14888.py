N = int(input())
nums = list(map(int, input().split()))
plus = list(map(int, input().split()))

tmp = nums.pop(0)
max = 0
min = 1000000000

l = dict()
l['+'] = plus[0]
l['-'] = plus[1]
l['*'] = plus[2]
l['//'] = plus[3]


def math(prev, turn, trash):
    global max
    global min
    if turn == N:
        return
    else:
        for i in trash:
            if trash[i] != 0:
                add_num = eval(str(prev) + i + str(nums[turn]))
                trash[i] -= 1
                if add_num > max:
                    max = add_num
                    # print(str(prev) + i + str(nums[turn]))
                if add_num < min:
                    min = add_num
                math(add_num, turn + 1, trash)
                # trash[i] += 1


            # if plus[i] != 0:
            #     add_num = eval(str(prev) + l[i] + str(nums[turn]))
            #     plus[i] -= 1
            #     if add_num > max:
            #         max = add_num
            #         print(str(prev) + l[i] + str(nums[turn]))
            #     if add_num < min:
            #         min = add_num
            #     math(add_num, turn + 1)
            #     plus[i] += 1


math(tmp, 0, l)
print(max)
print(min)
