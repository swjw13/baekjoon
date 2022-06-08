# https://programmers.co.kr/learn/courses/30/lessons/12920
# 선입 선출 스케쥴링

from collections import defaultdict


def solution(n, cores):
    heap = [[0, i] for i in range(len(cores))]
    while n > 1:
        cur_core = heap[0]
        heap[0] = heap.pop()
        idx = 0
        while True:
            length = len(heap)
            left = None
            if 2 * idx + 1 < length:
                left = heap[2 * idx + 1]

            right = None
            if 2 * idx + 2 < length:
                right = heap[2 * idx + 2]

            top = heap[idx]

            if left is None and right is None:
                break

            elif left is None:
                if top[0] > right[0] or (top[0] == right[0] and top[1] > right[1]):
                    heap[idx], heap[2 * idx + 2] = heap[2 * idx + 2], heap[idx]
                    idx = 2 * idx + 2
                else:
                    break

            elif right is None:
                if top[0] > left[0] or (top[0] == left[0] and top[1] > left[1]):
                    heap[idx], heap[2 * idx + 1] = heap[2 * idx + 1], heap[idx]
                    idx = 2 * idx + 1
                else:
                    break

            else:
                if left[0] < right[0]:
                    if top[0] > left[0] or (top[0] == left[0] and top[1] > left[1]):
                        heap[idx], heap[2 * idx + 1] = heap[2 * idx + 1], heap[idx]
                        idx = 2 * idx + 1
                    else:
                        break
                elif left[0] == right[0]:
                    if left[1] > right[1]:
                        if top[0] > right[0] or (top[0] == right[0] and top[1] > right[1]):
                            heap[idx], heap[2 * idx + 2] = heap[2 * idx + 2], heap[idx]
                            idx = 2 * idx + 2
                        else:
                            break
                    else:
                        if top[0] > left[0] or (top[0] == left[0] and top[1] > left[1]):
                            heap[idx], heap[2 * idx + 1] = heap[2 * idx + 1], heap[idx]
                            idx = 2 * idx + 1
                        else:
                            break
                else:
                    if top[0] > right[0] or (top[0] == right[0] and top[1] > right[1]):
                        heap[idx], heap[2 * idx + 2] = heap[2 * idx + 2], heap[idx]
                        idx = 2 * idx + 2
                    else:
                        break
        heap.append([cur_core[0] + cores[cur_core[1]], cur_core[1]])
        idx = len(heap) - 1

        while ((idx - 1) // 2 >= 0) and idx >= 0:
            if heap[(idx - 1) // 2][0] > heap[idx][0] or (
                    heap[(idx - 1) // 2][0] == heap[idx][0] and heap[(idx - 1) // 2][1] > heap[idx][1]):
                heap[(idx - 1) // 2], heap[idx] = heap[idx], heap[(idx - 1) // 2]
                idx = (idx - 1) // 2
            else:
                break
        n -= 1

    return heap[0][1] + 1


a = 6
b = [1, 2, 3]
print(solution(a, b))
