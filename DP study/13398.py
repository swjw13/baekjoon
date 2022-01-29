import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

end = 0
total = 0
ability = 1
mx = -sys.maxsize
tmp = 0
idx = 0

while True:
    if end == n:
        print(mx)
        break
    total += lst[end]
    if total > mx:
        mx = total

    if lst[end] >= 0:
        end += 1
    else:
        if ability == 1:
            total -= lst[end]
            if end == 0:
                lst[end] = 0
            tmp = lst[end]
            ability = 0
            end += 1
        else:
            total -= lst[end]
            if total + lst[end] < 0:
                if total + tmp < 0:
                    tmp = 0
                    ability = 1
                    total = 0
                    end += 1
                else:
                    total += tmp
                    tmp = lst[end]
                    end += 1
            else:
                if total + tmp < 0:
                    total += lst[end]
                    end += 1
                else:
                    ans1 = min(tmp, lst[end])
                    ans2 = max(tmp, lst[end])
                    tmp = ans1
                    total += ans2
                    end += 1
