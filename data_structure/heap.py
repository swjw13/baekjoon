a = [[10, 1], [9, 1], [8, 1], [7, 1], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0]]

for _ in range(6):
    tmp = a[0]
    a[0] = a.pop()
    idx = 0
    while True:
        left = None
        top = a[idx]
        if 2 * idx + 1 < len(a):
            left = a[2 * idx + 1]

        right = None
        if 2 * idx + 2 < len(a):
            right = a[2 * idx + 2]

        if left is None and right is None:
            break

        elif left is None:
            if top[0] < right[0] or (top[0] == right[0] and top[1] > right[1]):
                a[idx], a[2 * idx + 2] = a[2 * idx + 2], a[idx]
                idx = 2 * idx + 2
            else:
                break

        elif right is None:
            if top[0] < left[0] or (top[0] == left[0] and top[1] > left[1]):
                a[idx], a[2 * idx + 1] = a[2 * idx + 1], a[idx]
                idx = 2 * idx + 1
            else:
                break
        else:
            if left[0] < right[0]:
                if top[0] < right[0] or (top[0] == right[0] and top[1] > right[1]):
                    a[idx], a[2 * idx + 2] = a[2 * idx + 2], a[idx]
                    idx = 2 * idx + 2
                else:
                    break
            elif left[0] == right[0]:
                if left[0] < right[0]:
                    if top[0] < left[0] or (top[0] == left[0] and top[1] > left[1]):
                        a[idx], a[2 * idx + 1] = a[2 * idx + 1], a[idx]
                        idx = 2 * idx + 1
                    else:
                        break
                else:
                    if top[0] < right[0] or (top[0] == right[0] and top[1] > right[1]):
                        a[idx], a[2 * idx + 2] = a[2 * idx + 2], a[idx]
                        idx = 2 * idx + 2
                    else:
                        break
            else:
                if top[0] < left[0] or (top[0] == left[0] and top[1] > left[1]):
                    a[idx], a[2 * idx + 1] = a[2 * idx + 1], a[idx]
                    idx = 2 * idx + 1
                else:
                    break
    print(tmp)
    print(a)
