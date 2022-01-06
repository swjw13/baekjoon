N = int(input())

def hannum(num):
    if len(num) == 1:
        return True
    elif len(num) == 2:
        return True
    elif len(num) == 4:
        return False
    else:
        if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
            return True
        else:
            return False

total = 0
for i in range(N):
    if hannum(str(i+1)):
        total += 1

print(total)